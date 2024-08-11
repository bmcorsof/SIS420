import csv
import random


random.seed(42)


n = 100  


estaturas = [round(random.uniform(1.5, 2.0), 2) for _ in range(n)]


def generar_peso(estatura):
    ruido = random.uniform(-5, 5)
    return round(100 * (estatura - 1.5) + ruido, 2)

pesos = [generar_peso(estatura) for estatura in estaturas]

with open('datos_generados.csv', 'w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Estatura', 'Peso'])
    for estatura, peso in zip(estaturas, pesos):
        writer.writerow([estatura, peso])

print("Datos generados y guardados en 'datos_generados.csv'")
