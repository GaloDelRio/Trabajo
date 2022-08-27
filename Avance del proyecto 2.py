print("ingresa el ingreso mensual")
a=int(input())

print("ingresa gastos contantes del mes")
b=int(input())

print("ingresa gastos adicionales promedio")
c=int(input())

iva=.76

gastos_del_mes=a-(b*iva)-c

if gastos_del_mes > 0:
    print ("Tienes",gastos_del_mes, "pesos, te gustaria invertir en NFTEC?")
else :
    print (("Tienes",gastos_del_mes,"pesos, eres pobre bienvenido a LATAM"))