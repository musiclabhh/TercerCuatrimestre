from flask import Flask

app = Flask(__name__)

# Esta es la ruta principal
@app.route('/')
def home():
    return "<h1>¡Servidor Flask Funcionando!</h1><p>Configuración completada con éxito.</p>"

# Esta es una ruta de prueba adicional
@app.route('/prueba')
def prueba():
    return "<h1>Esta es otra página de prueba</h1>"

if __name__ == '__main__':
    # El parámetro host='0.0.0.0' ayuda a que sea más estable en Mac
    app.run(debug=True, port=5000)