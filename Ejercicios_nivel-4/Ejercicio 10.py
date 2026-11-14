Hora = 12
Historial_Placas = []
while Hora < 22:
    print("Registro")
    Hora = float(input("Hora de Entrada:"))
    if Hora >= 22:
        print("Estacionamiento Cerrado")
        print("")
    else:
        Placas = input("Placas:")
        Historial_Placas.append(Placas)
        Nombre = input("Nombre del Propietario:")
        print("")
        print("Resumen")
        print("Nombre del Propietario",Nombre)
        print("Placa del Vehiculo:", Placas)
        print("Hora registrada:", Hora)
        print("")
print("Historial De Placas")
for i in Historial_Placas:
    print(i)