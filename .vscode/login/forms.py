###########################################
#
#   Modulo para creacion de formularios
#       de LogIN.
#
###########################################

from django import forms

class LoginForm(forms.Form):

    nombre   = forms.CharField(label="Nombre",required=True)
    contraseña = forms.CharField(label="Contraseña",required=True)

