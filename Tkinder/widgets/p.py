
import time


inicio = time.time()

def fibonacci(numeroIngresado):
    if (numeroIngresado <= 0):
        return 0
    elif (numeroIngresado == 1):
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, numeroIngresado + 1):
            flag = a 
            a = b
            b = flag + b 
        return b
print(fibonacci(1000))
fin = time.time()

# Calcula el tiempo transcurrido
tiempo_transcurrido = round(fin - inicio, 10)



print(f"El algoritmo tardó {tiempo_transcurrido} segundos en ejecutarse.")


inicioR = time.time()

def fibonacciRecursivo(numeroUsuario, a=0, b=1):
    if (numeroUsuario == 0):
        return a
    else:
        return fibonacciRecursivo(numeroUsuario - 1, b, a + b)

print(fibonacciRecursivo(990))
finR = time.time()

# Calcula el tiempo transcurrido
tiempo_transcurridoR = round(finR - inicioR, 10)

print(f"El algoritmo recursivo tardó {tiempo_transcurridoR} segundos en ejecutarse.")