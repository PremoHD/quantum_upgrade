async function runLogistics(){
  document.getElementById("logistics-output").innerText=JSON.stringify(await (await fetch(`${API}/logistics/routes`)).json(),null,2);
}
