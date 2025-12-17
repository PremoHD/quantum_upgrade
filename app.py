from flask import Flask, jsonify
from flask_cors import CORS
from qiskit import QuantumCircuit, Aer, execute
from pqcrypto.sign import sphincs
import yfinance as yf
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns
import itertools, random, numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# Quantum Single Qubit
@app.route('/quantum/simulate')
def simulate_qubit():
    qc = QuantumCircuit(1,1); qc.h(0); qc.measure(0,0)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result().get_counts()
    return jsonify(result)

# Blockchain post‑quantum key
@app.route('/blockchain/hash')
def blockchain_hash():
    pk, sk = sphincs.generate_keypair()
    return jsonify({
        "public_key": list(pk),
        "signature_sample": list(sphincs.sign(b"Test", sk))[:20]
    })

# Finance: Portfolio optimization
@app.route('/finance/portfolio')
def finance_portfolio():
    tickers = ["AAPL","GOOG","MSFT","TSLA","BTC-USD"]
    data = yf.download(tickers, period="1y")['Adj Close']
    mu = expected_returns.mean_historical_return(data)
    S = risk_models.sample_cov(data)
    ef = EfficientFrontier(mu,S)
    ef.max_sharpe()
    return jsonify(ef.clean_weights())

# Finance risk simulation
@app.route('/finance/risk')
def finance_risk():
    tickers = ["AAPL","GOOG","MSFT","TSLA","BTC-USD"]
    data = yf.download(tickers, period="1y")['Adj Close'].pct_change().dropna()
    results=[]
    for _ in range(3000):
        w=np.random.rand(len(tickers)); w/=sum(w)
        ret=np.dot(w, data.mean())*252
        vol=np.sqrt(np.dot(w.T, np.dot(data.cov()*252,w)))
        results.append({'return':float(ret),'volatility':float(vol)})
    return jsonify(results)

# Consulting schedule
@app.route('/consulting/schedule')
def consulting_schedule():
    slots=["9AM","11AM","2PM"]; assignments={}
    for c in ["Alice","Bob","Charlie"]:
        bit=list(execute(QuantumCircuit(1,1).h(0).measure_all(inplace=False), Aer.get_backend('qasm_simulator'), shots=1).result().get_counts().keys())[0]
        assignments[c]=slots[int(bit,2)%len(slots)]
    return jsonify(assignments)

# Legal workflow
@app.route('/legal/workflow')
def legal_workflow():
    steps=["Draft","File","Review","Approval"]; out={}
    for s in steps:
        bit=list(execute(QuantumCircuit(1,1).h(0).measure_all(inplace=False), Aer.get_backend('qasm_simulator'), shots=1).result().get_counts().keys())[0]
        out[s]=int(bit,2)+1
    return jsonify(out)

# Data/AI simulation
@app.route('/data/simulate')
def data_simulate():
    df=pd.DataFrame({'customer':range(200),'value':np.random.rand(200)*200})
    df['trend']=np.random.rand(200)
    return jsonify(df.sort_values('trend',ascending=False).head(10).to_dict('records'))

# Logistics route
@app.route('/logistics/routes')
def route_optimization():
    locs=['A','B','C','D','E']
    sampled=random.sample(list(itertools.permutations(locs)), 100)
    best=min(sampled,key=lambda p: sum(random.randint(10,30) for _ in p))
    return jsonify({"best_path":best})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
