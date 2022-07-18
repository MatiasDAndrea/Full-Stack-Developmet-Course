from cgitb import html
import codecs
import webbrowser
import Cliente

f=open("ITBANK.html","w")
html_template =f"""<html>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                <head>Transacciones</head>
                <body>
                <h1>equipo n°7 </h1>
                </body>"""
def __index__():
        f.write(html_template)
        f.close()
        
webbrowser.open("ITBANK.html")

__index__()

