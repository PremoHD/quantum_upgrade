const API = window.location.hostname.includes("github")
  ? "https://YOUR-CODESPACE-URL"
  : "http://127.0.0.1:5000";
const API="http://127.0.0.1:5000";

async function runFinance(){
  let res=await fetch(`${API}/finance/portfolio`);
  let data=await res.json();
  document.getElementById("finance-output").innerText=JSON.stringify(data,null,2);
}
