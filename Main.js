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
    en Home.
    */

    const data = await fechtJSON("Cuentas.json")
    const cardElement = document.getElementById("AccountCards")
    let cardBody =""

    data.forEach(el=>{

        /*
            Se crea una lista en donde cada elemento contiene
            el tipo de moneda y el monto actual de la cuenta.
       */

        let list = ""
        for (let key in el.dinero){

           list += `<li>${key}: ${el.dinero[key]}</li>`
        }

        /*
            Como todas las cards son iguales a excepcion de su contenido
            se agregan como inner text para facilitar su creacion en cadena.
        */

        cardBody += `<div class='text-nowrap card m-2 h-100'><div class='card body p-2 border-2 border-primary'><h4 class='AccountNumber'>${el.id}</h4><h6>${el.tipoCuenta}</h6><ul>${list}</ul></div></div>`
    })

    cardElement.innerHTML = cardBody
}

init()