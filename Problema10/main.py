from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado

def pedir_dato_numerico(prompt, tipo=float):
    while True:
        try:
            return tipo(input(prompt))
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

def pedir_datos_figura(figura):
    if figura == "rectangulo":
        largo = pedir_dato_numerico("Ingrese el largo del rectángulo: ")
        ancho = pedir_dato_numerico("Ingrese el ancho del rectángulo: ")
        return largo, ancho
    else:  # circulo o cuadrado
        medida = pedir_dato_numerico(f"Ingrese el {'radio' if figura == 'circulo' else 'lado'}: ")
        return medida,

def calcular_area(opcion):
    try:
        if opcion == 1:  # Círculo
            radio, = pedir_datos_figura("circulo")
            if radio <= 0:
                raise ValueError("El radio debe ser un valor positivo")
            circulo = Circulo(radio)
            print(f"El área del círculo es: {circulo.calcular_area()}")
        elif opcion == 2:  # Rectángulo
            largo, ancho = pedir_datos_figura("rectangulo")
            if largo <= 0 or ancho <= 0:
                raise ValueError("El largo y el ancho deben ser valores positivos")
            rectangulo = Rectangulo(largo, ancho)
            print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
        elif opcion == 3:  # Cuadrado
            lado, = pedir_datos_figura("cuadrado")
            if lado <= 0:
                raise ValueError("El lado debe ser un valor positivo")
            cuadrado = Cuadrado(lado)
            print(f"El área del cuadrado es: {cuadrado.calcular_area()}")
    except ValueError as e:
        print(e)

def main():
    while True:
        try:
            print("\nMenú:")
            print("1. Calcular el área de un círculo")
            print("2. Calcular el área de un rectángulo")
            print("3. Calcular el área de un cuadrado")
            print("4. Salir")
            opcion = pedir_dato_numerico("Seleccione una opción: ", int)

            if opcion == 4:
                print("Hasta luego!")
                break
            elif opcion in [1, 2, 3]:
                calcular_area(opcion)
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        except Exception as e:
            print(f"Se ha producido un error: {e}")

if __name__ == "__main__":
    main()