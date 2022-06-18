let accountData

async function fetchJSON(url){
    
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

    accountData = await fetchJSON("Cuentas.json")
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
        if (regex.test(el.symbol) & el.price >=10){
            body += `<tr><td>${el.symbol}</td><td>${el.price}</td></tr>`
        }
   })
   
   document.getElementById("CriptoValues").innerHTML = body
}

async function conversion(){

    /*
        conversion() se encarga de realizar la conversion entre monedas.
    */
    
    const inputValue = document.getElementById("inputValue")
    const inputCoin = document.getElementById("inputCoin")

    const outputValue = document.getElementById("outputValue")
    const outputCoin = document.getElementById("outputCoin")

    if (inputCoin.value != "" & outputCoin.value != ""){

        let regex1 = new RegExp(`${outputCoin.value}${inputCoin.value}`)
        let regex2 = new RegExp(`${inputCoin.value}${outputCoin.value}`)
        const actualCoin = Number(inputValue.value)

        data = await fetchJSON("https://api.binance.com/api/v3/ticker/price")
        
        data.forEach(el=>{
            if (regex2.test(el.symbol)){
                
                const coef = Number(el.price)
                outputValue.value = actualCoin*coef.toFixed(8)
            }
            else if (regex1.test(el.symbol)){

                const coef = Number(1/el.price)
                outputValue.value = actualCoin*coef.toFixed(8)
            }
        })
    }
}

function flipCoins(){

    /*
        flipCoins() se encarga de invertir los tipos de moneda seleccionados.
        La funcion es llamada al presionar el icono.
   */

    const inputCoin = document.getElementById("inputCoin")
    const outputCoin = document.getElementById("outputCoin")

    let inputValue = inputCoin.value
    let outputValue = outputCoin.value

    inputCoin.value = outputValue
    outputCoin.value = inputValue

    // Llamo a la funcion conversion() para que ejecute la conversion.
    conversion()

}





init()
