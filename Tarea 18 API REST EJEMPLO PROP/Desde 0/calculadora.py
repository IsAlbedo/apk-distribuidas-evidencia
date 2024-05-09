import math

def realizar_operacion(operacion, num1, num2, num3):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        return num1 / num2
    elif operacion == 'potencia':
        return num1 ** num2
    elif operacion == 'modulo':
        return num1 % num2
    elif operacion == 'factorial':
        return math.factorial(int(num3))
    elif operacion == 'raizCuadrada':
        return math.sqrt(num3)
    elif operacion == 'logaritmo':
        return math.log(num3)
    elif operacion == 'sin':
        return math.sin(num3)
    elif operacion == 'cos':
        return math.cos(num3)
    elif operacion == 'tan':
        return math.tan(num3)
    elif operacion == 'e':
        return math.exp(num3)
    elif operacion == 'sinh':
        return math.sinh(num3)
    elif operacion == 'cosh':
        return math.cosh(num3)
    elif operacion == 'tanh':
        return math.tanh(num3)