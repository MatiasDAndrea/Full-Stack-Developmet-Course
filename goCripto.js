let accountData

async function fechtJSON(url){
    
    /*
    fetchJSON() se encarga de obtener la informacion del JSON.
   */
  const response = await fetch(url)
  return response.json()
}

async function init(){

    /*
    init() se encarga de inicializar las cuentas existentes
    en el desplegable
    */

    accountData = await fechtJSON("Cuentas.json")
    const cardElement = document.getElementById("Cuentas")
    let cardBody ="<option selected>Seleccionar Cuenta</option>"

    accountData.forEach(el=>{

        cardBody += `<option value="1">${el.id}</option>`
    })

    cardElement.innerHTML = cardBody
}


function asd(){

    let endpoint = "https://api.binance.com/api/v3/ticker/price"
    fetch(endpoint)
        .then(el=>el.json())
        .then(data=>plotValues(data))

}

function plotValues(data){
    
    /* 
    plotValues(data) se encarga de modificar el codigo HTML
    y plotear el valor de las criptomonedas mas relevantes.
    */
   let body=""
   let regex = /USDT\b/

   data.forEach(el=>{
        if (regex.test(el.symbol) && el.price >=10){
            body += `<tr><td>${el.symbol}</td><td>${el.price}</td></tr>`
        }
   })
   
   document.getElementById("CriptoValues").innerHTML = body
}

console.log(init())
