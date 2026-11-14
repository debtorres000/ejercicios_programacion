#Identificacion de la fila con mayor cantidad de espacios ocupados
#declaracion de variables
#mayor_ocupados=entero fila_mayor=entero total_espacios=entero ocupados=entero libres=entero
mayor_ocupados = 0

Control_vehiculos = [[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]]
pregunta=input("Te gustaria registrar un vehiculo o la salida de un vehiculo? (si/no): ").lower()
while pregunta=="si":
    print("1. Registrar un vehiculo")
    print("2. Registrar la salida de un vehiculo")
    op=input("Seleccione una opcion: ") 
    match op:
        case "1":
            fila=int(input("Ingrese la fila donde desea estacionar el vehiculo (0-3): "))
            columna=int(input("Ingrese la columna donde desea estacionar el vehiculo (0-4): "))
            if Control_vehiculos[fila][columna]==0:
                Control_vehiculos[fila][columna]=1
                print("Vehiculo registrado en la fila", fila, "y columna", columna)
            else:
                print("El espacio ya esta ocupado")
        case "2":
            fila=int(input("Ingrese la fila del vehiculo que sale (0-3): "))
            columna=int(input("Ingrese la columna del vehiculo que sale (0-4): "))
            if Control_vehiculos[fila][columna]==1:
                Control_vehiculos[fila][columna]=0
                print("Vehiculo retirado de la fila", fila, "y columna", columna)
            else:
                print("No hay vehiculo en ese espacio")
        
    pregunta=input("Desea continuar en el sistema de control de vehiculos? (si/no): ").lower()

total_espacios = 0
ocupados = 0
libres = 0

for fila in Control_vehiculos:
    for espacio in fila:
        total_espacios += 1
        if espacio == 1:
            ocupados += 1
        else:
            libres += 1
    print(f"Espacios libres en la fila {Control_vehiculos.index(fila) + 1}: {libres}")
    libres = 0  #Reincio el contador para la siguiente fila
    if ocupados > mayor_ocupados:
        mayor_ocupados = ocupados
        fila_mayor = Control_vehiculos.index(fila) 
        ocupados = 0  # Reinicio el contador de ocupados para la siguiente fila

print("La fila con mayor cantidad de espacios ocupados tiene:", mayor_ocupados, "espacios ocupados y es la fila número:", fila_mayor)

        