const API = window.location.hostname.includes("github")
  ? "https://YOUR-CODESPACE-URL"
  : "http://127.0.0.1:5000";
async function runConsult(){
  document.getElementById("consulting-output").innerText=JSON.stringify(await (await fetch(`${API}/consulting/schedule`)).json(),null,2);
}
