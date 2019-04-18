var reference
var price
var stock
window.onload = function(event) {
var ref=document.getElementById("id_Referencia")
ref.setAttribute("value",reference);
ref.setAttribute("style","display:none");// here was the desabled
}


function set_ref(ref){
reference=ref;
}

function set_attributes(){
stock=document.getElementById("id_CantidadInv").value;
document.getElementById("disable").setAttribute("style","display:none");
document.getElementById("id_Cantidad").setAttribute("onfocusout","set_total()");
var stockISBN=document.getElementById("id_ISBN");
stockISBN.setAttribute("id","Stock_ISBN");
var id_ISBN=document.getElementById("id_ISBN");
id_ISBN.selectedIndex=stockISBN.selectedIndex;
id_ISBN.setAttribute("style","display:none");//here was the desabled
var labels= document.getElementById("Informacion_pedido");
labels.getElementsByTagName("P")[0].setAttribute("style","display:none");
labels.getElementsByTagName("P")[1].setAttribute("style","display:none");
labels.getElementsByTagName("P")[3].setAttribute("style","display:none");
labels.getElementsByTagName("P")[4].setAttribute("style","display:none");

}

function set_total(){
var to_sell=document.getElementById("id_Cantidad").value;
var left=stock-to_sell;
if (left<0){
alert("Lo sentimos no contamos con la cantidad de ejemplares para su pedido, favor de indicar otra cantidad o ponerse en contacto con nosotros");
document.getElementById("id_CantidadInv").setAttribute("value",stock);
document.getElementById("boton").disabled=true;

}else{
document.getElementById("id_CantidadInv").setAttribute("value",left);
document.getElementById("boton").disabled=false;
document.getElementById("id_Total").value=(price*to_sell)
}
}

function set_price(bprice){
price=bprice
}