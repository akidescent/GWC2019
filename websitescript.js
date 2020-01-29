
function makeBigger(x) {
    x.style.width = "400px";
    x.style.height = "400px";
}

function normalImg(x) {
  x.style.width = "200px";
  x.style.height = "200.px";
}

function showHideSection(x) {
  var x = document.getElementById(x);
  if (x.style.display == "none"){
    x.style.display = "block";
    document.getElementById("Hide Bio").innerHTML=("Hide Bio");
  }
  else{
    x.style.display = "none";
    document.getElementById("Show Bio").innerHTML=("Show Bio");
  }

}
