# NIVEL 6. Integración de listas y matrices
# Ejercicios 17, 18 y 19
FILAS = 4
COLUMNAS = 5

estacionamiento = [
    ["LIBRE", "LIBRE", "LIBRE", "LIBRE", "LIBRE"],
    ["LIBRE", "LIBRE", "LIBRE", "LIBRE", "LIBRE"],
    ["LIBRE", "LIBRE", "LIBRE", "LIBRE", "LIBRE"],
    ["LIBRE", "LIBRE", "LIBRE", "LIBRE", "LIBRE"]
]

# [placa, tipo, hora_entrada, hora_salida, permanencia, importe]
registros = []

# Tipos de vehículo y sus tarifas por hora (misma posición en cada lista)
tipos = ["Motocicleta", "Automóvil", "Camioneta", "Camión"]
tarifas = [10, 15, 20, 30]

#vehiculos de cada tipo
ingresos_por_tipo = [0, 0, 0, 0]

opcion = ""

while opcion != "6":
    print("ESTACIONAMIENTO")
    print("1. Registrar ingreso")
    print("2. Consultar dónde está una placa")
    print("3. Registrar salida y cobrar")
    print("4. Ver distribución actual")
    print("5. Reporte de jornada")
    print("6. Salir")
    opcion = input("Elige una opción: ")
#Registrar ingreso
    if opcion == "1":
        print("Registrar ingreso")
        fila = int(input("Fila (1 a " + str(FILAS) + "): ")) - 1
        columna = int(input("Columna (1 a " + str(COLUMNAS) + "): ")) - 1

        if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
            print("Esa posición no existe.")
        elif estacionamiento[fila][columna] != "LIBRE":
            print("Ese espacio ya está ocupado. Elige otro.")
        else:
            placa = input("Placa del vehículo: ").upper()

            # Filtro repetidas
            repetida = False
            for f in range(FILAS):
                for c in range(COLUMNAS):
                    if estacionamiento[f][c] == placa:
                        repetida = True

            if repetida:
                print("Esa placa ya está dentro del estacionamiento.")
            else:
                print("Tipo de vehículo:")
                for i in range(len(tipos)):
                    print(i + 1, "-", tipos[i], "($" + str(tarifas[i]) + " por hora)")
                tipo = int(input("Elige el tipo (1 a 4): "))

                if tipo < 1 or tipo > 4:
                    print("Tipo de vehículo no válido")
                else:
                    hora_entrada = int(input("Hora de entrada (0 a 23): "))

                    if hora_entrada < 0 or hora_entrada > 23:
                        print("Hora no válida")
                    else:
                        # Guardar placa en matriz
                        estacionamiento[fila][columna] = placa
                        # Guardar en registros
                        registros.append([placa, tipos[tipo - 1], hora_entrada, "—", "—", "—"])
                        # Suma a contador
                        print("Vehículo", placa, "registrado en fila", fila + 1, "columna", columna + 1)
#Buscar placa
    elif opcion == "2":
        print("Consultar placa")
        placa = input("Placa a buscar: ").upper()

        encontrada = False
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if estacionamiento[f][c] == placa:
                    print("La placa", placa, "está en la fila", f + 1, "columna", c + 1)
                    encontrada = True

        if not encontrada:
            print("La placa", placa, "no se encuentra dentro del estacionamiento")
#Registrar salida y cobrar
    elif opcion == "3":
        print("Registrar salida")
        placa = input("Placa del vehículo que sale: ").upper()

        #Buscar placa
        fila_enc = -1
        col_enc = -1
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if estacionamiento[f][c] == placa:
                    fila_enc = f
                    col_enc = c

        if fila_enc == -1:
            print("Esa placa no está dentro del estacionamiento.")
        else:
            ## Encontrar registro en lista sin salida
            for i in range(len(registros)):
                if registros[i][0] == placa and registros[i][3] == "—":
                    pos = i

            hora_salida = int(input("Hora de salida (0 a 23): "))

            if hora_salida < registros[pos][2] or hora_salida > 23:
                print("La hora de salida no es válida")
            else:
                ### Calcular permanencia
                permanencia = hora_salida - registros[pos][2]
                if permanencia < 1:
                    permanencia = 1
                #### Buscar tarifa según tipo
                tarifa = 0
                for i in range(len(tipos)):
                    if tipos[i] == registros[pos][1]:
                        tarifa = tarifas[i]

                importe = permanencia * tarifa

                #Completar registro
                registros[pos][3] = hora_salida
                registros[pos][4] = permanencia
                registros[pos][5] = importe

                #Libera lugar
                estacionamiento[fila_enc][col_enc] = "LIBRE"

                print("COMPROBANTE DE SALIDA")
                print("Placa:", placa)
                print("Tipo:", registros[pos][1])
                print("Hora de entrada:", registros[pos][2])
                print("Hora de salida:", hora_salida)
                print("Permanencia:", permanencia, "hora(s)")
                print("Importe a pagar: $" + str(importe))
                print("El espacio fila", fila_enc + 1, "columna", col_enc + 1, "quedó libre.")
#Ver distribucion
    elif opcion == "4":
        print("Distribución actual del estacionamiento")
        for f in range(FILAS):
            for c in range(COLUMNAS):
                print(estacionamiento[f][c], end="\t")
            print()
#Reporte
    elif opcion == "5":
        print("REPORTE DE JORNADA")

        #conteo de ocupados
        print("\nVehículos que permanecen dentro:")
        ocupados = 0
        for f in range(FILAS):
            for c in range(COLUMNAS):
                if estacionamiento[f][c] != "LIBRE":
                    print("-", estacionamiento[f][c], "(fila", f + 1, "columna", str(c + 1) + ")")
                    ocupados = ocupados + 1
        if ocupados == 0:
            print("Ninguno.")

        #espacios libres y ocupados
        libres = FILAS * COLUMNAS - ocupados
        print("\nEspacios ocupados:", ocupados)
        print("Espacios libres:", libres)

        #total de vehículos atendidos
        print("\nTotal de vehículos atendidos:", len(registros))

        #ingresos generados
        ingresos = 0
        for registro in registros:
            if registro[3] != "—":
                ingresos = ingresos + registro[5]
        print("Ingresos generados: $" + str(ingresos))

        #tipo de vehiculo con más ingresos
        if len(registros) == 0:
            print("Tipo de vehículo con más ingresos: aún no hay registros")
        else:
            mayor_tipo = 0
            for i in range(len(tipos)):
                if ingresos_por_tipo[i] > ingresos_por_tipo[mayor_tipo]:
                    mayor_tipo = i
            print("Tipo de vehículo con más ingresos:", tipos[mayor_tipo],
                  "(" + str(ingresos_por_tipo[mayor_tipo]) + " vehículos)")

        #fila con mayor ocupacioln
        fila_mayor = 0
        mayor_ocupacion = -1
        for f in range(FILAS):
            contador = 0
            for c in range(COLUMNAS):
                if estacionamiento[f][c] != "LIBRE":
                    contador = contador + 1
            if contador > mayor_ocupacion:
                mayor_ocupacion = contador
                fila_mayor = f
        print("Fila con mayor ocupación: fila", fila_mayor + 1,
              "(" + str(mayor_ocupacion) + " vehículos)")

        #tabla con registros del día
        print("\nRegistros del día:")
        print("Placa\tTipo\t\tEntrada\tSalida\tPermanencia\tImporte")
        for registro in registros:
            print(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5], sep="\t")
#Salir
    elif opcion == "6":
        print("Se ha finalizado el programa. ¡Hasta mañana!")

    else:
        print("Opción no válida. Elige un número del 1 al 6.")