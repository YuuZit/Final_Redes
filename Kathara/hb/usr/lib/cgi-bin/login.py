#!/usr/bin/env python3
import os
import sys
from urllib.parse import parse_qs

# Cabecera HTTP obligatoria
print("Content-Type: text/html; charset=utf-8\n")

metodo = os.environ.get("REQUEST_METHOD", "GET")

# Obtener los datos crudos según el método HTTP
if metodo == "POST":
    try:
        largo = int(os.environ.get("CONTENT_LENGTH", 0))
    except ValueError:
        largo = 0
    datos_crudos = sys.stdin.read(largo)
else:
    datos_crudos = os.environ.get("QUERY_STRING", "")

# Parsear parámetros (user=valor&pass=valor)
parametros = parse_qs(datos_crudos)
usuario = parametros.get("user", [""])[0]
clave = parametros.get("pass", [""])[0]

# Generar respuesta HTML
print("<html><body>")
print(f"<p>Método HTTP utilizado: <b>{metodo}</b></p>")

if usuario == "admin" and clave == "1234":
    print("<h1 style='color:green;'>Login correcto</h1>")
    print(f"<p>Bienvenido al sistema, {usuario}.</p>")
else:
    print("<h1 style='color:red;'>Login incorrecto</h1>")
    print("<p>Credenciales inválidas.</p>")

print("<br><a href='/'>Volver al formulario</a>")
print("</body></html>")
