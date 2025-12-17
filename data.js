async function runData(){
  document.getElementById("data-output").innerText=JSON.stringify(await (await fetch(`${API}/data/simulate`)).json(),null,2);
}
