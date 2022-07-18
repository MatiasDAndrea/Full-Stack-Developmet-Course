data_type = {
    "numero": int,
    "nombre": str,
    "apellido": str,
    "dni": str,
    "tipo": str,
    "direccion": dict,
    "transacciones": dict
}

a = "asd"

print(isinstance(a,data_type["apellido"]))