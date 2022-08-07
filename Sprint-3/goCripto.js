let accountData
let apiInfo
let dolarDict  = {}

async function fetchJSON(url){
    
    /*
    fetchJSON() se encarga de obtener la informacion del JSON.
   */
  const response = await fetch(url);
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

        cardBody += `<option value="${el.id}">${el.id}</option>`
    })

    cardElement.innerHTML = cardBody
}

async function precios(){

    /* 
        Precios() se encarga de generar las tarjetas con los valores
        de las criptos actuales y valores actuales del dolar.
        Realiza el llamado a dos APIs  
    */

    apiInfo = await fetchJSON("https://api.binance.com/api/v3/ticker/price")
    const element = document.getElementById("precios")

    let regex1 = /BTCUSDT/
    let regex2 = /ETHUSDT/
    let regex3 = /BNBUSDT/

    let body = ""
    let k = 0

    for (let i=0;i<apiInfo.length;i++){

        let regCheck1 = regex1.test(apiInfo[i].symbol)
        let regCheck2 = regex2.test(apiInfo[i].symbol)
        let regCheck3 = regex3.test(apiInfo[i].symbol)


        if (regCheck1 | regCheck2 | regCheck3){


            let value = Number(apiInfo[i].price).toFixed(2)
            let coin = apiInfo[i].symbol.replace("USDT","")
            k += 1
            body +=`<div class="card p-1 border-2 border-primary"><h4 class="AccountNumber text-nowrap ">${coin}</h4><h5 class="text-nowrap">${value} USD</h5></div>`
        }

        if (k==3){

            element.innerHTML = body
            break
        }
    }

    let dolarAPI = await fetchJSON("http://www.dolarsi.com/api/api.php?type=valoresprincipales")
    const dolarElement = document.getElementById("FirstRow")
    cards = ""
    let allowedDolars = {
        "Dolar Oficial":"",
        "Dolar Blue":"",
        "Dolar Contado con Liqui":"",
        "Dolar Bolsa":"",
    }
    dolarAPI.map(el=>{

        
        nombre = el.casa.nombre
        venta = el.casa.venta.replace(",",".")
        compra = el.casa.compra.replace(",",".")

       if (/*allowedDolars.hasOwnProperty(nombre)*/true){
            dolarDict[nombre] = {"venta":venta,"compra":compra}
            cards += `<div class="card p-1 border-2 border-success"><h5>${nombre}</h5><ul><li>Compra: $${compra}</li><li>Venta: $${venta}</li></ul></div>`
       }
    })
    dolarElement.innerHTML = cards
    console.log(dolarDict["Dolar Blue"]["venta"])
}



function conversion(){

    /*
        conversion() se encarga de realizar la conversion entre monedas.
    */
    
    const inputValue = document.getElementById("inputValue")
    const inputCoin = document.getElementById("inputCoin")

    const outputValue = document.getElementById("outputValue")
    const outputCoin = document.getElementById("outputCoin")
    
    

    apiInfo.push({
        "symbol":"ARSUSDT",
        "price":dolarDict["Dolar Blue"]["venta"]
    })
    
    if (inputCoin.value != "" & outputCoin.value != ""){

        let regex1 = new RegExp(`${outputCoin.value}${inputCoin.value}`)
        let regex2 = new RegExp(`${inputCoin.value}${outputCoin.value}`)

        const actualCoin = Number(inputValue.value)
        data = apiInfo

        data.forEach(el=>{
            if (regex2.test(el.symbol)){
                
                const coef = Number(el.price)
                outputValue.value = actualCoin*coef.toFixed(8)
            }
            else if (regex1.test(el.symbol)){

                const coef = Number(1/el.price)
                outputValue.value = actualCoin*coef.toFixed(8)

            }else if (inputCoin.value == outputCoin.value){

                const coef = 1
                outputValue.value = actualCoin*coef
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


function plotAccount(){

    /*
        plotAccount() se encarga de imprimir en pantalla el resumen
        de cuenta.
        Ademas Actualiza el campo moneda para la cuenta Seleccionada.
    */

    const element = document.getElementById("Cuentas")
    const list = document.getElementById("accountResume")
    let coins = document.getElementById("inputCoin")
    let valueCoin = coins.value

    let head = "<h2>Resumen de Cuenta</h2>"
    let body = ""
    let moneda = "<option selected></option>"
    

    for (let i=0;i<accountData.length;i++){
 
        if(accountData[i].id == element.value){

            for (let key in accountData[i].dinero){

                body += `<li>${key}: ${accountData[i].dinero[key]}</li>`
                moneda += `<option value="${key}">${key}</option>`
            }
            list.innerHTML = `${head}<ul>${body}</ul>`
            coins.innerHTML = moneda
            break
        }
        list.innerHTML = body
        
    }
}


function buy(){

    /*
        La funcion buy() simula la compra o intercambio
        de monedas.
    */

    const account = document.getElementById("Cuentas")

    const inputValue = Number(document.getElementById("inputValue").value)
    const inputCoin = document.getElementById("inputCoin").value

    const outputValue = Number(document.getElementById("outputValue").value)
    const outputCoin = document.getElementById("outputCoin").value

    // Transferencia entre monedas
    for (let i=0;i<accountData.length;i++){

        if (accountData[i].id == account.value){

            const ownPropCheckIn = accountData[i].dinero.hasOwnProperty(inputCoin)
            const ownPropCheckOut = accountData[i].dinero.hasOwnProperty(outputCoin)

            if (ownPropCheckIn & accountData[i].dinero[inputCoin]>=inputValue ){

                //Se efectua la compra
                accountData[i].dinero[inputCoin] -= inputValue

                if (ownPropCheckOut){

                    accountData[i].dinero[outputCoin] += outputValue
                }
                else {

                    accountData[i].dinero[outputCoin] = outputValue
                }

                fetch("Cuentas.json",{

                    method:"POST",
                    body: JSON.stringify(accountData)
                })
                plotAccount()

            }
            else if (!ownPropCheckIn){

                alert("Usted no tiene este tipo de moneda")
                
            }
            else if (ownPropCheckIn & accountData[i].dinero[inputCoin]<inputValue ){

                alert("Usted no dispone de la cantidad estipulada")
                
            }

            break
        }

    }
}

init()
precios()
//define tiempo de refresco de 10 segundos//
setInterval(precios,10000)

