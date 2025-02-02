total_PRL=0 #Inicialización 
precio_PRL = int (input("Ingrese precio (0 para terminar):"))
while(precio_PRL != 0):
    total_PRL = total_PRL + precio_PRL
    precio_PRL = int (input("Ingrese precio (0 para terminar):"))
#Mostrar sumatoria total de todos los precios
print("total de la venta sin descuento: $",total_PRL)    
#Descuentos
descuento7_PRL=total_PRL * 7 / 100
descuento12_PRL=total_PRL * 12 / 100
#Si compra es mayor a $50.000
if(total_PRL <  50000):
    #Aplicar descuento del 7 %
    print("Se realizo un descuento del 7%")
    print("total a pagar: $",total_PRL - descuento7_PRL)
else:#En caso contrario
    #Aplicar descuento del 12 %
    print("Se realizo un descuento del 12%")
    print("total a pagar: $",total_PRL - descuento12_PRL)
print("Gracias...")

