import aleatorios

def main():
    lista = aleatorios.generar_numeros()
    print("Lista original: ")
    aleatorios.mostrar_lista(lista)

    lista_ordenada = aleatorios.ordenar_lista(lista)
    print("Lista ordenada: ")
    aleatorios.mostrar_lista(lista_ordenada)

if __name__ == "__main__":
    main()