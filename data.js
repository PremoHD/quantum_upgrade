const API = window.location.hostname.includes("github")
  ? "https://YOUR-CODESPACE-URL"
  : "http://127.0.0.1:5000";
async function runData(){
  document.getElementById("data-output").innerText=JSON.stringify(await (await fetch(`${API}/data/simulate`)).json(),null,2);
}
