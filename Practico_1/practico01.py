import csv
import random

random.seed(42)

n = 100

def generar_estatura():
    return round(random.uniform(1.30, 2.11), 2)

def generar_peso(estatura):
    if estatura < 1.50:
        return round(random.uniform(40, 60), 2)
    elif estatura < 1.80:
        return round(random.uniform(50, 80), 2)
    elif estatura < 2.00:
        return round(random.uniform(60, 100), 2)
    else:
        return round(random.uniform(90, 130), 2)

estaturas = [generar_estatura() for _ in range(n)]
pesos = [generar_peso(estatura) for estatura in estaturas]

with open('datos_generados.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Estatura', 'Peso'])
    for estatura, peso in zip(estaturas, pesos):
        writer.writerow([estatura, peso])

print("Datos generados y guardados en 'datos_generados.csv'")
