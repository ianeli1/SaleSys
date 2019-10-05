btn = document.getElementById("loginbtn");

function showLogin(){
  document.getElementById("pzero").innerHTML = "Changed!";
}

btn.addEventListener("click",showLogin());
