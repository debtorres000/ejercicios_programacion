#Tiempo de permanencia del vehiculo y el cobro por hora
#Declaracion de variables
#Cobro=real Tiempo=entero
Tiempo=int(input("Cual es el tiempo de permanencia del vehiculo en horas?"))    
if Tiempo<=1 and Tiempo>0:
    Cobro=Tiempo*15
elif Tiempo>0:
    Cobro=Tiempo*15
else:
    print("El tiempo de permanencia del vehiculo no puede ser negativo")
    
print("El tiempo de permanencia del vehiculo es:",Tiempo,"horas")
print("El cobro por el tiempo de permanencia del vehiculo es:$",Cobro,"pesos")
    

    