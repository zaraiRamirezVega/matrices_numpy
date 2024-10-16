"""Desarrollar un algoritmo que calcule el numero de dias entre dos fechas dadas """

from datetime import datetime

def calcular_dias(fecha1_str, fecha2_str):
    fecha1 = datetime.strptime(fecha1_str, '%d-%m')
    fecha2 = datetime.strptime(fecha2_str, '%d-%m')
    if fecha1 >= fecha2:
        raise ValueError("La segunda fecha debe ser mayor que la primera.")
    return (fecha2 - fecha1).days

def main():
    while True:
        fecha1 = input("Ingresa la primera fecha (DD-MM): ")
        fecha2 = input("Ingresa la segunda fecha (DD-MM): ")
        try:
            dias = calcular_dias(fecha1, fecha2)
            print(f'Número de días entre {fecha1} y {fecha2}: {dias}')
            break
        except (ValueError, TypeError):
            print("Fecha no válida. Asegúrate de ingresar el formato correcto (DD-MM) y que la segunda fecha sea mayor.")

if __name__ == "__main__":
    main()
