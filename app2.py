from flask import Flask, request

app = Flask(__name__)

@app.route("/info")
def info():
    return "Esta es mi aplicación Flask!"

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    mensaje_recibido = data.get("mensaje")
    return f"Recibí tu mensaje: {mensaje_recibido}"

if __name__ == "__main__":
    app.run(debug=True, port=5001)