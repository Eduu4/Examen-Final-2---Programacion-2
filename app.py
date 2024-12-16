class Vehiculo:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Color: {self.color}"

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

    def frenar(self):
        print(f"El vehículo {self.marca} {self.modelo} está frenando.")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, color, numero_puertas, tipo_combustible):
        super().__init__(marca, modelo, año, color)
        self.numero_puertas = numero_puertas
        self.tipo_combustible = tipo_combustible

    def abrir_maletero(self):
        print(f"El maletero del {self.marca} {self.modelo} se está abriendo.")


# Crear objetos de la clase Coche
coche1 = Coche("Toyota", "Corolla", 2020, "Blanco", 4, "Gasolina")
coche2 = Coche("Hyundai", "Tucson", 2021, "Negro", 4, "Diesel")

# Llamar a los métodos en los objetos
print(coche1)
coche1.arrancar()
coche1.frenar()
coche1.abrir_maletero()

print("\n" + str(coche2))
coche2.arrancar()
coche2.frenar()
coche2.abrir_maletero()