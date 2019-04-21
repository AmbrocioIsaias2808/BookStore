  var finaltotal;
  var reference;
  var nom;
  paypal.Buttons({
    createOrder: function(data, actions) {
      return actions.order.create({
        purchase_units: [{
        "description": "Referencia de Pago: "+reference+"\nLibro:"+nom+" ",
          amount: {
            value: finaltotal
          }
        }]

      });
    },
    onApprove: function(data, actions) {
      return actions.order.capture().then(function(details) {
          location.href ="/Pago_Exitoso/REF="+reference+"/"+nom+"/";
        return fetch('/paypal-transaction-complete', {
          method: 'post',
          headers: {
            'content-type': 'application/json'
          },
          body: JSON.stringify({
            orderID: data.orderID
          })
        });
      });
    }
  }).render('#paypal-button-container');


function set_data(total,ref,nombre){
finaltotal=total;
reference=ref;
nom=nombre;
}