Control_vehiculos = []
contador=1
respuesta=input("Desea ingresar al sistema de control de vehiculos? (si/no): ").lower()
while respuesta=="si" and contador<=15:
    print("1. Registrar un vehiculo")
    print("2. Registrar la salida de un vehiculo")
    print("3. Consultar  la placa de vehiculos registrados")
    print("4. Mostrar cuantos vehiculos estan estacionados")
    print("5. Mostrar cuantos espacios estan disponibles")
    print("6. Salir")
    op=input("Seleccione una opcion: ") 
    match op:
        case "1":
            placa=input("Ingrese la placa del vehiculo: ")
            Control_vehiculos.append(placa)
            print("Vehiculo registrado")
        case "2":
            placa=input("Ingrese la placa del vehiculo que sale: ")
            if placa in Control_vehiculos:
                Control_vehiculos.remove(placa)
                print("Vehiculo retirado")
            else:
                print("Vehiculo no encontrado")
        case "3":
            if len(Control_vehiculos)==0:
                print("No hay vehiculos registrados")
            else:
                print("Placas de vehiculos registrados: ")
                for placa in Control_vehiculos:
                        print(placa)
        case "4":
            print("Cantidad de vehiculos estacionados: ", len(Control_vehiculos))
        case "5":
            print("Espacios disponibles: ", 15 - len(Control_vehiculos))
        case "6":
            print("Saliendo del sistema...")
        case _:
            print("Opcion no valida")
    contador+=1
    respuesta=input("Desea continuar en el sistema de control de vehiculos? (si/no): ").lower()
