def solicitar_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            numerador, denominador = map(int, fraccion.split('/'))

            if denominador == 0:
                raise ZeroDivisionError("El denominador no puede ser 0")
            if numerador > denominador:
                raise ValueError("El numerador no puede ser mayor que el denominador")
            
            # Si llegamos aquí, las entradas son válidas
            return numerador, denominador

        except ValueError:
            # Este bloque captura tanto errores de conversión como la condición numerador > denominador
            print("Por favor, asegúrese de que X e Y sean números enteros y X <= Y")
        except ZeroDivisionError as e:
            print("Error:", e)

def calcular_porcentaje(numerador, denominador):
    resultado = round((numerador / denominador) * 100)
    if resultado < 1:
        return "E"
    elif resultado > 99:
        return "F"
    else:
        return f"{resultado}%"

def main():
    numerador, denominador = solicitar_fraccion()
    resultado = calcular_porcentaje(numerador, denominador)
    print(f"Cantidad de combustible en el tanque: {resultado}")

if __name__ == "__main__":
    main()