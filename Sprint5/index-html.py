from cgitb import html
import codecs
import webbrowser
from main import __init__

d= __init__.__get__["reporte":""]

f=open("ITBANK.html","w")

html_template =f"""
<html>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<head>Transacciones</head>
<body>
<h1>{d}</h1>
</body>
"""
f.write(html_template)
f.close()
#file=codecs.open("ITBANK.html","r","utf-8")
webbrowser.open("ITBANK.html")
#print.(file.read())
