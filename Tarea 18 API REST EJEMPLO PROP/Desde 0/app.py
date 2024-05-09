from flask import Flask, render_template, request, jsonify
from calculadora import realizar_operacion
from database import obtener_historial_compuesto, obtener_historial_unico, guardar_operacion_compuesta, guardar_operacion_unica

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    historial_compuesto = obtener_historial_compuesto()
    historial_unico = obtener_historial_unico()
    return render_template('index.html', historial_compuesto=historial_compuesto, historial_unico=historial_unico)


@app.route('/actualizar_historial_compuesto', methods=['GET'])
def actualizar_historial_compuesto():
    historial_compuesto = obtener_historial_compuesto()
    return jsonify(historial_compuesto)

@app.route('/actualizar_historial_unico', methods=['GET'])
def actualizar_historial_unico():
    historial_unico = obtener_historial_unico()
    return jsonify(historial_unico)


@app.route('/calcular', methods=['POST'])
def calcular():
    operacion = request.form['operacion']
    num1 = float(request.form.get('num1', 0))
    num2 = float(request.form.get('num2', 0))
    num3 = float(request.form.get('num3', 0))
    resultado = realizar_operacion(operacion, num1, num2, num3)
    
    if operacion in ['factorial', 'raizCuadrada', 'logaritmo', 'sin', 'cos', 'tan', 'e', 'sinh', 'cosh', 'tanh']:
        guardar_operacion_unica(operacion, num3, resultado)
    else:
        guardar_operacion_compuesta(operacion, num1, num2, resultado)
    
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)