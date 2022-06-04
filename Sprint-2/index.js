let arr=[] //[Nombre, dinero, numReferencia]
let order

function addCards(reference, nombre, dinero){

    /*
    addCards se encarga de crear codigo HTML para generar 
    los perfiles nuevos de las personas que ingresan al sistema
    Cada nuevo perfil lleva un numero de referencia unico
    */

    /*
    Se crean un conjunto de elementos, asignando clases segun bootstrap
    a cada uno de los elementos creados
    */
    const styles = [
        "bg-primary",
        "bg-secondary",
        "bg-success",
        "bg-danger",
        "bg-warning",
        "bg-info",
        "bg-light",
        "bg-dark",
    ]

    const random = Math.round(Math.random()*7)
    
    let fDiv = document.createElement("div")
    fDiv.classList.add("row", "border","m-2",`${styles[random]}`,"rounded")
    fDiv.id = (`First${reference}`)
 
    let sDiv = document.createElement("div")
    sDiv.classList.add("col-12", "border","rounded")
    sDiv.id = (`Second${reference}`)

    let tDiv = document.createElement("div")
    tDiv.classList.add("card")
    tDiv.id = (`Third${reference}`)

    let nameText = document.createElement("h2")
    nameText.id = (`nameText${reference}`)
    nameText.innerHTML = nombre

    let dineroText = document.createElement("h3")
    dineroText.id = (`dineroText${reference}`)
    dineroText.innerHTML = `Pago: \$${dinero}`

    let saldoText = document.createElement("h3")
    saldoText.id = (`saldoText${reference}`)
   

    let deleteButton = document.createElement("button")
    deleteButton.id = (`deleteButton${reference}`)
    deleteButton.onclick = deleteCard
    deleteButton.innerHTML = "Delete"

    /*
    Se adjuntan los elementos para formar la estructura deseada
   */
    const element  = document.getElementById("Cards")
    element.appendChild(fDiv)

    const fElement = document.getElementById(`First${reference}`)
    fElement.appendChild(sDiv)

    const sElement = document.getElementById(`Second${reference}`)
    sElement.appendChild(nameText)
    sElement.appendChild(dineroText)
    sElement.appendChild(saldoText)
    sElement.appendChild(deleteButton)

}


function add(){

    /* 
    Cada vez que se ingresa una nueva persona, la funcion add()
    le asigna un numero de referencia al nuevo usuario y crea su perfil de 
    cuenta.
    */

    const name  = document.getElementById("Nombre").value
    const money = document.getElementById("Pago").value
    let key = false
    

    /*
    Bloque de codigo para filtrar informacion ingresada por el usuario
    */
 
    arr = arr.map((el)=>{
        
        if (el[0].toLowerCase() == name.toLowerCase()){

            let htmlMoney = document.getElementById(`dineroText${el[2]}`)
            let actualMoney = Number(htmlMoney.innerHTML.match(/\d/g).join(''))
        
            htmlMoney.innerHTML = `Pago: \$${actualMoney + Number(money)}`
            key = true //Marco que hubo un nombre ya existente en la lista

            return [el[0], Number(el[1])+Number(money), el[2]]

        }else{
            return el
        }
    })

    if (!key){  

        if (order==undefined){
            order=0
        }
        else {
            order+=1
        }

        arr.push([name, money, order])
        addCards(order, name, money)
    }
    
}


function deleteCard(){

    /*
    La funcion delete() se encarga de eliminar, segun disposicion del usuario,
    aquellos elementos que no quiere que pertenezcan a la lista.
    Actua tanto sobre arr como sobre el codigo HTML
    */

    /*
    Busco el boton que fue presionado y me encargo de borrar
    ese bloque de HTML.
    */
    const reference = this.id.match(/\d/g).join('')
    const element  = document.getElementById("Cards")
    const removeId = document.getElementById(`First${reference}`)
    element.removeChild(removeId)

    /*
    Elimino del array el elemento especifico
    */
    
    arr = arr.filter((el)=>{

        return el[2] != reference
    })
}

function calcularSaldos(){

    /*
    calcularSaldos() se encarga de tomar el arr ingresado hasta el momento
    y calcular el saldo, a favor o en contra, segun el monto que pago.
   */
    
    const cantidadPersonas = arr.length

    if (cantidadPersonas!=0){
        const saldoPago = Number(document.getElementById("totalPago").value)
        
        let totalPersona = saldoPago/cantidadPersonas

        arr.forEach((el)=>{

            let ref = el[2]
            const htmlObject = document.getElementById(`saldoText${ref}`)

            if ((el[1]-totalPersona)<0){
                htmlObject.innerHTML = `Aun debe pagar: \$${Math.abs(Math.round(el[1]-totalPersona))}`
            }else {
                htmlObject.innerHTML = `Le deben pagar: \$${Math.round(el[1]-totalPersona)}`
            }
        })
    } else{
        prompt("El numero de participantes debe ser mayor a cero!")
    }
}

function refresh(){

    /*
    La funcion refresh() elimina todos los usuarios creados
   */
    const element = document.getElementById("Cards")
    arr = []
    element.replaceChildren()
    console.log(arr)
    
}