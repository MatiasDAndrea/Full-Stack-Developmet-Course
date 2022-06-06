let cantidad = 0.00;
let pesos = 0.00;

function Calcular(){

    let integrantes = document.getElementById("integrantes");
    let NPNombre = document.getElementById("nombreId").value;
    let NPPesos = document.getElementById("pesosId").value;

    let nDiv = document.createElement("div");
    nDiv.classList.add("persona__Lista");

    let nNombre = document.createElement("p");
    nDiv.appendChild(nNombre);

    integrantes.appendChild(nDiv);

    nNombre.innerHTML = NPNombre + ": $" + NPPesos;

    if(NPPesos != "")
    {
        pesos = pesos + parseFloat(NPPesos);
    }
    cantidad++;

    let total = document.getElementById("totalId");
    total.innerHTML = "";
    total.innerHTML = '<p>Total: $' + parseFloat(pesos) + '</p>';

    document.getElementById("nombreId").value = "";
    document.getElementById("pesosId").value = "";

    let aporte = document.getElementById("aporteId");
    aporte.innerHTML = "";
    aporte.innerHTML = '<p>A cada uno le toca aportar: $' + pesos/cantidad + '</p>';
}