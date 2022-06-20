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

        cardBody += `<option value="${el.id}">${el.id}</option>`
    })

    cardElement.innerHTML = cardBody
}


async function precios(){
    
    /* 
        precios() se encarga de generar las tarjetas con los valores
        de las criptos actuales
    */
    let apiInfo = await fetchJSON("https://api.binance.com/api/v3/ticker/price")

    let regex1 = /BTCUSDT/
    let regCheck1 = regex1.test(apiInfo[i].symbol)

    let regex2 = /ETHUSDT/
    let regCheck2 = regex2.test(apiInfo[i].symbol)

    let regex3 = /BNBUSDT/
    let regCheck3 = regex3.test(apiInfo[i].symbol)

    for (let i=0;i<apiInfo.length;i++){

        if (regCheck1 | regCheck2 | regCheck3){

            let value = apiInfo[i].price
            let coin = apiInfo[i].symbol

            <div class="card-fluid m-2 h-100">
            <div class="card body p-2 border-2 border-primary">
                <h4 class="AccountNumber" style="overflow-wrap: break-word">Visa xxxx-2000</h4>
                <h6>Tarjeta de Credito</h6>
                <h6>Vencimiento __/__</h6><hr>
                <ul>
                    <li>8000,00 $</li>
                    <li>9000,00 U$s</li>
                </ul>
            </div>
            </div>


        }

    }

    
    





    console.log(apiInfo)

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
    */

    const element = document.getElementById("Cuentas")
    const list = document.getElementById("accountResume")

    let head = "<h2>Resumen de Cuenta</h2>"
    let body = ""
    

    for (let i=0;i<accountData.length;i++){
 
        if(accountData[i].id == element.value){

            for (let key in accountData[i].dinero){

                body += `<li>${key}: ${accountData[i].dinero[key]}</li>`
            }
            list.innerHTML = `${head}<ul>${body}</ul>`
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
