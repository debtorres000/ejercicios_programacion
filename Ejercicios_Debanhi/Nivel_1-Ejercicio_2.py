#Registro de hora de entrada y hora de salida del vehiculo calculando el tiempo de permanencia del vehiculo
#Declaracion de variables
#H_e=Real H_s=Real Horas=entero


H_e=float(input("Cual es la hora de entrada del vehiculo?, en formato de 24 horas"))
H_s=float(input("Cual es la hora de salida del vehiculo ?, en formato de 24 horas"))
if H_s>H_e:
    Horas=H_s-H_e 
    print("El tiempo de permanencia del vehiculo es:",Horas,"horas")
else:
    print("La hora de salida del vehiculo no puede ser menor a la hora de entrada del vehiculo")
    
