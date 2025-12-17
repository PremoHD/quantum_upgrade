async function runBlock(){
  let res=await fetch(`${API}/blockchain/hash`);
  document.getElementById("blockchain-output").innerText=JSON.stringify(await res.json(),null,2);
}
