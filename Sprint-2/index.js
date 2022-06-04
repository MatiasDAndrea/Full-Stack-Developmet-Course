let arr=[]
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
    
    let fDiv = document.createElement("div")
    fDiv.classList.add("row", "border")
    fDiv.id = (`First${reference}`)
 
    let sDiv = document.createElement("div")
    sDiv.classList.add("col-12", "border")
    sDiv.id = (`Second${reference}`)

    let tDiv = document.createElement("div")
    tDiv.classList.add("card")
    tDiv.id = (`Third${reference}`)

    let nameText = document.createElement("h2")
    nameText.id = (`nameText${reference}`)
    nameText.innerHTML = nombre

    let dineroText = document.createElement("h2")
    dineroText.id = (`dineroText${reference}`)
    dineroText.innerHTML = dinero

    /*
    Se adjuntan los elementos para formar la estructura deseada
   */
    const element  = document.getElementById("Main")
    element.appendChild(fDiv)

    const fElement = document.getElementById(`First${reference}`)
    fElement.appendChild(sDiv)

    const sElement = document.getElementById(`Second${reference}`)
    sElement.appendChild(nameText)
    sElement.appendChild(dineroText)

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
            htmlMoney.innerHTML = `${Number(htmlMoney.innerHTML) + Number(money)}`
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