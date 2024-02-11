class Alumno:
    def __init__(self, nombre_alumno, num_registro):
        self.nombre = nombre_alumno
        self.numero_registro = num_registro
        self.edad = None
        self.notas = []

    def Display(self):
        return print(f"Nombre: {self.nombre}\nNúmero de registro: {self.numero_registro}")

    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, nota):
        self.notas.append(nota)

def ingreso_nota():
    try:
        nota = float(input("Ingrese una nota entre 0 y 10: "))
        assert nota <= 10 and nota >= 0, "Nota fuera de rango"
        return nota
    except:
        print("Nota invalida, intente de nuevo")
        return ingreso_nota()

def main():
    alumno = Alumno("Anthony Mendoza", 4)
    alumno.setAge(19)
    alumno.setNota(ingreso_nota())
    alumno.Display()

if __name__ == "__main__":
    main()