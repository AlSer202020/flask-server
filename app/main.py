from flask import Flask, render_template

# Inicializamos la aplicación
app = Flask(__name__)


# Ruta 1: Devuelve un HTML muy básico
@app.route("/")
def home():
    # return """
    #     <h1>¡Hola desde Flask en Docker!!!!</h1>
    #     <p>Este es tu primer servidor Python funcionando.</p>
    # """
    return render_template("index.html")


@app.route("/saludo/<name>")
def saludo(name):
    # return f"<h1>Bienvenido a Flask, {name}</h1>"
    return


@app.route("/multiplicar/<int:n1>/<int:n2>")
def multiplicar(n1, n2):
    return f"<p>Multiplicar {n1} x {n2} da resultado {n1 * n2}"


@app.route("/catalogo/<int:id_product>")
def catalogo(id_product):
    productos = [
        {"nombre": "Teclado Mecánico", "precio": 49.99, "disponible": True},
        {"nombre": "Ratón Óptico", "precio": 19.99, "disponible": False},
        {"nombre": "Monitor 4K", "precio": 299.99, "disponible": True},
    ]
    return render_template(
        "catalogo.html", nombre="algo", id=id_product, lista_productos=productos
    )


if __name__ == "__main__":
    # host='0.0.0.0' es VITAL en Docker para que el servidor sea accesible desde fuera del contenedor
    # debug=True hará que el servidor se reinicie automáticamente si cambias este archivo
    app.run(host="0.0.0.0", port=5000, debug=True)
