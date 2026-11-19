##Capacidad maxima de 30 vehiculos e informar si es posible registrar un vehiculo o no
##Declaracion de variables
#Respuetsta=cadena Tipo_vehiculo=cadena Horas_estancia=entero Importe=real Placa=cadena
#Numero_atendidos=entero Cantidad_Motocicletas=entero Cantidad_Automoviles=entero Cantidad_Camionetas=entero Cantidad_Camiones=entero Importe_total=real
Numero_atendidos=1
Cantidad_Motocicletas=0
Cantidad_Automoviles=0
Cantidad_Camionetas=0
Cantidad_Camiones=0
Importe_total=0
Respuesta=input("Desea registrar un vehiculo? si/no").lower()
while Respuesta=="si" and Numero_atendidos<=30:
    Numero_atendidos=Numero_atendidos+1
    Tipo_vehiculo=input("Cual es el tipo de vehiculo? Automovil, Motocicleta, Camioneta o Camion").lower()
    Horas_estancia=int(input("Cual es el tiempo de estancia del vehiculo en horas?"))
    Placa=input("Cual es la placa del vehiculo?")
    match Tipo_vehiculo:
        case "automovil" :
            print
            Importe=Horas_estancia*15
            Cantidad_Automoviles=Cantidad_Automoviles+1
        case "motocicleta":
            Cantidad_Motocicletas=Cantidad_Motocicletas+1
            Importe=Horas_estancia*10
        case "camioneta":
            Cantidad_Camionetas=Cantidad_Camionetas+1
            Importe=Horas_estancia*20
        case "camion":
            Cantidad_Camiones=Cantidad_Camiones+1
            Importe=Horas_estancia*30
        case _:
            print("Tipo de vehiculo no valido")
    print("-----------------------------------")
    print("Resumen de registro del vehiculo")
    print("Tipo de vehiculo:",Tipo_vehiculo)
    print("Placa del vehiculo:",Placa)
    print("Tiempo de permanencia del vehiculo:",Horas_estancia,"horas")
    print("El cobro por el tiempo de permanencia del vehiculo es:$",Importe,"pesos")
    print("-----------------------------------")
    print("Aun hay capacidad para registrar vehiculos, se han atendido",Numero_atendidos-1,"vehiculos")
    Importe_total=Importe_total+Importe
    Respuesta=input("Desea registrar otro vehiculo? si/no").lower()

if Numero_atendidos>30:
    print("No es posible registrar otro vehiculo, se ha alcanzado la capacidad maxima de 30 vehiculos")
    
print("-------------------------------------------")
print("Resumen de registro de los vehiculos")
print("Numero de vehiculos atendidos:",Numero_atendidos)
print("Cantidad de motocicletas:",Cantidad_Motocicletas)
print("Cantidad de automoviles:",Cantidad_Automoviles)
print("Cantidad de camionetas:",Cantidad_Camionetas)
print("Cantidad de camiones:",Cantidad_Camiones)
print("Importe total:",Importe_total)
