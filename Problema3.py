class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14159 * self.radio ** 2

def main():
    while True:
        try:
            radio = float(input("Ingrese el radio del círculo: "))
            if radio >= 0:
                circulo = Circulo(radio)
                area = circulo.calcular_area()
                print(f"El área del círculo con radio {circulo.radio} es: {area}")
                break
            else:
                print("El radio debe ser un número positivo")
        except ValueError:
            print("No fue posible crear el círculo con el radio proporcionado. Intente de nuevo")

if __name__ == "__main__":
    main()