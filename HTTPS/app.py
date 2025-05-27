lfrom flask import Flask, request
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    ahora = datetime.now().hour # obtiene la hora actual

    if ahora < 12:
        saludo = "¡Buenos días!"
    elif ahora < 18:
        saludo = "¡Buenas tardes!"
    else:
        saludo = "¡Buenas noches!"

    saludo_de_retorno = ""
    if request.method == "POST" and "saludo" in request.form:
        saludo_de_retorno = "<p>¡Hello There!</p>" #mensaje de retorno del botón

    return f"""
    <html>
        <head><title>App con Juego</title></head>
        <body>
            <h1>{saludo}</h1> 
            <p>Son las {datetime.now().strftime('%H:%M')}.</p>

            <form method="POST">
                <button type="submit" name="saludo">Saludar de regreso</button>
            </form>
            {saludo_de_retorno}

            <hr>

            <h2>🎲 Juego: Adivina el número (1 al 5)</h2>
            <form method="POST" action="/juego">
                <input type="number" name="numero" min="1" max="5" required>
                <button type="submit">Intentar</button>
            </form>
        </body>
    </html>
    """

@app.route("/juego", methods=["POST"])
def juego():
    numero_real = random.randint(1, 5) #genera un numero random
    try:
        numero_usuario = int(request.form.get("numero"))
    except (ValueError, TypeError):
        return "<p>Ingresa un número válido.</p><a href='/'>Volver</a>"

    if numero_usuario == numero_real:
        resultado = "🎉 ¡Adivinaste!"
    else:
        resultado = f"❌ No era {numero_usuario}, era {numero_real}."

    return f"""
    <html>
        <body>
            <h2>Resultado del juego</h2>
            <p>{resultado}</p>
            <a href="/">Volver</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
