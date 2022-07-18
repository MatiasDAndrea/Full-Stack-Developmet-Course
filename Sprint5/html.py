from cgitb import html
import codecs
import webbrowser

class HTML:

    def crear_html(self,reporte):

        nombre= reporte.get("nombre")
        numero_cuenta= reporte.get("numero")
        dni=reporte.get("DNI")
        transaccion=reporte.get("Transaccion")
        html_trasaccion=""
        for x in transaccion:
            html_trasaccion+=f"""
            <h1>Transacciones</h1>
            <h3>{x["fecha"]}</h3>
            <h3>{x["Tipo Operacion"]}</h3>
            <h3>{x["Estado"]}</h3>
            <h3>{x["Monto"]}</h3>
            <h3>{x["Razon"]}</h3>
            """
        f=open("ITBANK.html","w")


        html_template =f"""
        <html>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <head>transacciones</head>
        <body>
        <h1>Cliente:Nombre: {nombre}</h1>
        <h1>Número de cuenta: {numero_cuenta}</h1>
        <h1>DNI: {dni}</h1>
        <h3>{html_trasaccion}</h3>
        </body>
        """
        f.write(html_template)
        f.close()
        webbrowser.open("ITBANK.html")
        
