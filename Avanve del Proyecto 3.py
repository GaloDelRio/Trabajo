print("ingresa el ingreso mensual")
a=float(input())

print("ingresa gastos contantes o servicios del mes")
b=float(input())

print("ingresa gastos adicionales promedio")
c=float(input())

iva=.76

def gastos_del_mes(a,b,c):
    operacion=a-(b*iva)-c
    if operacion > 0:
        return print ("Tienes",operacion, "pesos, te gustaria invertir en NFTEC?")
    else:
        return print (("Tienes",operacion,"pesos, eres pobre bienvenido a LATAM"))

gastos_del_mes(a,b,c)