async function runLegal(){
  document.getElementById("legal-output").innerText=JSON.stringify(await (await fetch(`${API}/legal/workflow`)).json(),null,2);
}
