// Get the modal
var modal,span

// When the user clicks on the button, open the modal
function clickmodal(id) {
span=document.getElementsByClassName(id)[0];
modal=document.getElementById(id);
console.log(span)
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function cerrar() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}