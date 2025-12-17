async function runConsult(){
  document.getElementById("consulting-output").innerText=JSON.stringify(await (await fetch(`${API}/consulting/schedule`)).json(),null,2);
}
