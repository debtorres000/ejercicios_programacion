##Clasificacion del tipo de vehiculo
#Declaracion de variables
#Tipo_vehiculo=cadena Horas_estancia=entero Importe=real 
Tipo_vehiculo=input("Cual es el tipo de vehiculo? Automovil, Motocicleta, Camioneta o Camion").lower()
Horas_estancia=int(input("Cual es el tiempo de estancia del vehiculo en horas?"))
match Tipo_vehiculo:
    case "automovil" :
        Importe=Horas_estancia*15
        print("El tiempo de permanencia del vehiculo es:",Horas_estancia,"horas")
        print("El cobro por el tiempo de permanencia del vehiculo es:$",Importe,"pesos")
    case "motocicleta":
        Importe=Horas_estancia*10
        print("El tiempo de permanencia del vehiculo es:",Horas_estancia,"horas")
        print("El cobro por el tiempo de permanencia del vehiculo es:$",Importe,"pesos")
    case "camioneta":
        Importe=Horas_estancia*20
        print("El tiempo de permanencia del vehiculo es:",Horas_estancia,"horas")
        print("El cobro por el tiempo de permanencia del vehiculo es:$",Importe,"pesos")
    case "camion":
        Importe=Horas_estancia*30
        print("El tiempo de permanencia del vehiculo es:",Horas_estancia,"horas")
        print("El cobro por el tiempo de permanencia del vehiculo es:$",Importe,"pesos")
    case _:
        print("Tipo de vehiculo no valido")
