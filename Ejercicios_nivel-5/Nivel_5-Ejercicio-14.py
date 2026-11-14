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

#Mostrar el estado final del estacionamiento
print("Estado final del estacionamiento:")
for fila in Control_vehiculos:
    print(fila)
    