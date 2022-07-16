import json
import sys


try:
    f = open(sys.argv[1],"r")

except IndexError or FileNotFoundError:
    print("Error de ingreso")

