def solicitar_calificaciones():
    while True:  # Iniciar un bucle infinito que se rompe solo cuando todas las calificaciones son válidas
        calificaciones = input("Ingrese las calificaciones separadas por comas (ej. 1,2,3): ")
        calificaciones_str_list = calificaciones.split(',')
        calificaciones_int_list = []
        valido = True

        for calificacion_str in calificaciones_str_list:
            try:
                calificacion_int = int(calificacion_str.strip())  # Intentar convertir a entero
                calificaciones_int_list.append(calificacion_int)
            except ValueError:
                print(f"Error: '{calificacion_str}' no es una calificación válida. Por favor, intente de nuevo.")
                valido = False  # Marcar la entrada como inválida y romper el ciclo for
                break

        if valido:
            return calificaciones_int_list

def main():
    calificaciones = solicitar_calificaciones()
    print("Calificaciones ingresadas: ", calificaciones)

if __name__ == "__main__":
    main()