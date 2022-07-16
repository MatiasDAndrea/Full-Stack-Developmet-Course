from cgitb import html
import codecs
import webbrowser
import Cliente




f=open("ITBANK.html","w")

html_template =f"""
<html>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
<head>Transacciones</head>
<body>
<div class="row">
            <div class="col-12">
                
                <select class="form-select" aria-label="Default select example" id="Cuentas" onchange="plotAccount()">
                {Cliente.Black.tipe}
                </select>
            </div>
        </div>

        <div class="row">
            <div class="col-12">
                <ul id="accountResume"></ul>
            </div>
        </div>

"""
f.write(html_template)
f.close()
#file=codecs.open("ITBANK.html","r","utf-8")
webbrowser.open("ITBANK.html")
#print.(file.read())
