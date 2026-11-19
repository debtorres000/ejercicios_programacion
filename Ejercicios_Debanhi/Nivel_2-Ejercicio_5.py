##Calcular un descuento sobre el importe
#declaracion de variables
#Importe=real Numero_visitas=entero Total=real
Numero_visitas=int(input("Cual es el numero de visitas del cliente?"))
Importe=float(input("Cual es el importe a pagar por el cliente?"))
if Numero_visitas>=10:
    Importe=Importe*.90
    print("El cliente tiene un descuento del 10% por ser cliente frecuente y el importe a pagar es de: $",Importe,"pesos")
else:
    print("El cliente no tiene descuento y el importe a pagar es de: $",Importe,"pesos")
    
    

