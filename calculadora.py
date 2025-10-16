# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potenciacion(base, exponente):
    return base ** exponente

def radicacion(base, indice):
    if indice == 0:
        return "Error: índice de raíz cero"
    return base ** (1 / indice)

def porcentaje(total, porcentaje):
    return (total * porcentaje) / 100

def modulo(a, b):
    if b == 0:
        return "Error: División por cero"
    return a % b

def factorial(n):
    if n < 0:
        return "Error: factorial de número negativo"
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

def promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def cm_a_pulgadas(cm):
    return cm / 2.54

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32


if __name__ == "__main__":
    print("Suma 5 + 3 =", suma(5, 3))
    print("Resta 10 - 4 =", resta(10, 4))
    print("Multiplicación 6 * 7 =", multiplicacion(6, 7))
    print("División 8 / 2 =", division(8, 2))
    print("Potenciación 2^3 =", potenciacion(2, 3))
    print("Radicación raíz cúbica de 27 =", radicacion(27, 3))
    print("Porcentaje 20% de 150 =", porcentaje(150, 20))
    print("Módulo 10 % 3 =", modulo(10, 3))
    print("Factorial 5! =", factorial(5))
    print("Promedio [2,4,6,8] =", promedio([2,4,6,8]))
    print("10 cm a pulgadas =", cm_a_pulgadas(10))
    print("25°C a °F =", celsius_a_fahrenheit(25))
