# Variables iniciales
Hora = 12
Capacidad = 15
Historial_Placas = []
Placas_Dentro = []
Estacionamiento_Cerrado = False

while True:
    print("")
    print("===== ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar vehículos estacionados")
    print("4. Mostrar cantidad de vehículos")
    print("5. Mostrar espacios disponibles")
    print("6. Mostrar historial de placas")
    print("7. Buscar una placa en el historial")
    print("8. Terminar programa")

    Opcion = input("Selecciona una opción: ")

    # OPCIÓN 1: INGRESO
    if Opcion == "1":

        if Estacionamiento_Cerrado:
            print("Estacionamiento cerrado para nuevos ingresos")

        else:
            Hora = float(input("Hora de Entrada: "))

            if Hora >= 22:
                Estacionamiento_Cerrado = True
                print("Estacionamiento Cerrado")

            elif len(Placas_Dentro) >= Capacidad:
                print("Estacionamiento lleno")
                print("No hay espacios disponibles")

            else:
                Placas = input("Placas: ").strip().upper()

                if Placas in Placas_Dentro:
                    print("Este vehículo ya está estacionado")

                else:
                    Nombre = input("Nombre del Propietario: ")

                    Placas_Dentro.append(Placas)
                    Historial_Placas.append(Placas)

                    print("")
                    print("Resumen")
                    print("Nombre del Propietario:", Nombre)
                    print("Placa del Vehiculo:", Placas)
                    print("Hora registrada:", Hora)

    # OPCIÓN 2: SALIDA
    elif Opcion == "2":

        Placas = input("Placa del vehículo que sale: ").strip().upper()

        if Placas in Placas_Dentro:
            Placas_Dentro.remove(Placas)
            print("Salida registrada correctamente")

        else:
            print("La placa no se encuentra en el estacionamiento")

    # OPCIÓN 3: CONSULTAR VEHÍCULOS
    elif Opcion == "3":

        if len(Placas_Dentro) == 0:
            print("No hay vehículos estacionados")

        else:
            print("Vehículos dentro del estacionamiento:")

            for i in Placas_Dentro:
                print(i)

    # OPCIÓN 4: CONTAR VEHÍCULOS
    elif Opcion == "4":

        print("Vehículos estacionados:", len(Placas_Dentro))

    # OPCIÓN 5: ESPACIOS DISPONIBLES
    elif Opcion == "5":

        Disponibles = Capacidad - len(Placas_Dentro)
        print("Espacios disponibles:", Disponibles)

    # OPCIÓN 6: HISTORIAL
    elif Opcion == "6":

        print("Historial de Placas")

        for i in Historial_Placas:
            print(i)

    # OPCIÓN 7: BUSCAR PLACA EN HISTORIAL
    elif Opcion == "7":

        Placa_a_buscar = input("Introducir placa a buscar: ").strip().upper()
        Encontrar = 0

        for i in range(len(Historial_Placas)):

            if Historial_Placas[i] == Placa_a_buscar:
                print("La placa está en el sistema")
                print("La placa está en la posición:", i + 1)
                Encontrar = 1

        if Encontrar == 0:
            print("La placa no se encontró en el sistema")

    # OPCIÓN 8: TERMINAR
    elif Opcion == "8":

        print("Fin del programa")
        break

    else:
        print("Opción no válida")