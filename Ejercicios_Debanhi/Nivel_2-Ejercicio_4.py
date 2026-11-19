##Calcular la tarifa adecuada a pagar por el tiempo de permanencia del vehiculo 
#Declaracion de variables
#Tiempo_estadia=entero Cobro=real
Tiempo_estadia=int(input("Cual es el tiempo de permanencia del vehiculo en horas"))
if Tiempo_estadia<=2 and Tiempo_estadia>0:
    Cobro=Tiempo_estadia*20
elif Tiempo_estadia>2 and Tiempo_estadia<=5:
    Cobro=Tiempo_estadia*18
elif Tiempo_estadia>5:
    Cobro=Tiempo_estadia*15
else:
    print("El tiempo de permanencia del vehiculo no puede ser negativo")

print("El tiempo de permanencia del vehiculo es:",Tiempo_estadia,"horas")
print("El cobro por el tiempo de permanencia del vehiculo es:$",Cobro,"pesos")
