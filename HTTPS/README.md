# HTTPS App con botón interactivo y juego

Tarea Extra Clase 3 -  Jose Alpizar, Jafet Díaz, Adrian Pereira - Algoritmos y Estructuras de Datos II - ITCR

## Funcionalidades 

- Usa HTTPS con certificados locales
- Saluda al visitante según la hora del día
- Permite responder al saludo con un botón
- Incluye un juego básico de "Adivina el número"

---

## Requisitos

- Python 3
- Pip
- Flask

---

## Instalación

1. Clona o descarga este repositorio.

2. Asegúrate de tener todos los requisitos. 

3. Genera una única vez un certificado SSL autofirmado con el comando:

openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem

## Ejecución

1. Corre la app:

python3 app.py

2. Abre el navegador

https://localhost:5000

3. Interactúa!



