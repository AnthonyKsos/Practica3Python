class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

def pedir_datos():
    while True:
        try:
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            if largo <= 0 or ancho <= 0:
                raise ValueError("El largo y el ancho deben ser números positivos")
            return largo, ancho
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo")

def main():
    largo, ancho = pedir_datos()
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print(f"El área del rectángulo de largo {largo} y ancho {ancho} es: {area}")

if __name__ == "__main__":
    main()