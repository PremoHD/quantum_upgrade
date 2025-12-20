const API = window.location.hostname.includes("github")
  ? "https://YOUR-CODESPACE-URL"
  : "http://127.0.0.1:5000";
async function runLogistics(){
  document.getElementById("logistics-output").innerText=JSON.stringify(await (await fetch(`${API}/logistics/routes`)).json(),null,2);
}
