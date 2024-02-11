import operaciones

def main():
    print(f"Suma: {operaciones.suma(5, 3)}")
    print(f"Resta: {operaciones.resta(10, 2)}")
    print(f"Producto: {operaciones.producto(4, 5)}")
    print(f"División: {operaciones.division(20, 4)}")
    print(f"División por cero: {operaciones.division(20, 0)}")
    print(f"Tipo de dato no válido: {operaciones.suma('a', 3)}")

if __name__ == "__main__":
    main()