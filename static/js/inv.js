

function getComment(id) {
  let xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if(xhttp.readyState == 4 && xhttp.status == 200){
      alert(xhttp.responseText);
    }
  }
  xhttp.open("GET", "get?type=item&attr=comment&id="+id, true);
  xhttp.send(null);
}

function registerItem() {
  let name = document.forms["itemRegist"]["name"].value;
  let amount = document.forms["itemRegist"]["amount"].value;
  let price = document.forms["itemRegist"]["price"].value;
  let comment = document.forms["itemRegist"]["comment"].value;

}
