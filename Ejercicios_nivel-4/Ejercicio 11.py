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
        Nombre = input("Nombre del Propietario")
        print("")
        print("Resumen")
        print("Nombre del Propietario:",Nombre)
        print("Placa del Vehiculo:", Placas)
        print("Hora registrada:", Hora)
        print("")

hist=input("¿Quiere mostrar el historial de placas?")
if hist =="Yes" or hist=="YES" or hist=="yes":
    print("Historial De Placas")
    for i in Historial_Placas:
        print(i)

Busqueda="Yes"
while Busqueda=="Yes" or Busqueda=="YES" or Busqueda=="yes":
    Busqueda=input("¿Quieres buscar una placa?")
    if Busqueda=="Yes" or Busqueda=="YES" or Busqueda=="yes":
        Placa_a_buscar=input("Introducir placa a buscar:")
        Encontrar=0
        for i in range(len(Historial_Placas)):
            if Historial_Placas[i]==Placa_a_buscar:
                print("La placa esta en el sistema")
                print("La placa esta en la posición:", i+1)
                Encontrar=1
        if Encontrar==0:
            print("La placa no se encontro en el sistema")