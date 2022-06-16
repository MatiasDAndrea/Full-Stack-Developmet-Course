
/*
    getAccount() se encarga de obtener de Main.html las cuentas
    existentes del usuario.
*/

function init(){

    /*
    init() se encarga de inicializar los datos relevantes 
    de la HomePage
    */
    fetch("Cuentas.json")
        .then(el=>el.json())
        .then(data=>)

}

let HomeValues
fetch('Main.html')
.then(response=> response.text())
.then(text=> HomeValues=text);

let accounts = document.getElementsByClassName("AccountNumber")
console.log(HomeValues)




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

init()
