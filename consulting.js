const API = window.location.hostname.includes("github")
  ? "https://upgraded-sniffle-97rq4v4vp5p5c69p-8080.app.github.dev"
  : "http://127.0.0.1:5000";
async function runConsult(){
  document.getElementById("consulting-output").innerText=JSON.stringify(await (await fetch(`${API}/consulting/schedule`)).json(),null,2);
}
