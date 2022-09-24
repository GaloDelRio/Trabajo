
from ast import If


iva=.76
i=0

def pesos(ingreso_mensual, gastos_constante,gastos_adicionales):
    operacion=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    if operacion > 0:
        print ("Tienes",operacion, "pesos, te gustaria invertir en NFTEC?")
    else:
        print (("Tienes",operacion,"pesos, eres pobre bienvenido a LATAM"))

        

def dolares(ingreso_mensual, gastos_constante,gastos_adicionales):
    operacion=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    if operacion > 0:
        print ("Tienes",operacion, "pesos, te gustaria invertir en NFTEC?")
    else:
        print (("Tienes",operacion,"pesos, eres pobre bienvenido a LATAM"))

def agregar_dinero():
    operación2=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    while i==0:
        pregunta=str(input("¿Te gustaría agregar dinero?   y/n"))
        if pregunta=="y":
            preguta2=float(input("¿Cuanto dinero te gustaría agregar?"))
            operación2=operación2+preguta2
            print(operación2)
        if pregunta=="n":
            print("Gracias por utilizar la aplicación :)")
            break



opcion = str(input("¿Quieres usar dolares o pesos?"))
if(opcion == "pesos"):
    ingreso_mensual = float(input("ingresa el ingreso mensual"))
    gastos_constante = float(input("ingresa gastos contantes o servicios del mes"))
    gastos_adicionales = float(input("ingresa gastos adicionales promedio"))
    pesos(ingreso_mensual, gastos_constante,gastos_adicionales)
    operación2=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    while i==0:
        pregunta=str(input("¿Te gustaría agregar dinero?   y/n"))
        if pregunta=="y":
            preguta2=float(input("¿Cuanto dinero te gustaría agregar?"))
            operación2=operación2+preguta2
            print(operación2)
        if pregunta=="n":
            print("Gracias por utilizar la aplicación :)")
            break

elif (opcion == "dolares"):
    ingreso_mensual = int(input("ingresa el ingreso mensual"))
    gastos_constante = int(input("ingresa gastos contantes o servicios del mes"))
    gastos_adicionales = int(input("ingresa gastos adicionales promedio"))
    dolares(ingreso_mensual, gastos_constante,gastos_adicionales)
    operación2=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    while i==0:
        pregunta=str(input("¿Te gustaría agregar dinero?   y/n"))
        if pregunta=="y":
            preguta2=float(input("¿Cuanto dinero te gustaría agregar?"))
            operación2=operación2+preguta2
            print(operación2)
        if pregunta=="n":
            print("Gracias por utilizar la aplicación :)")
            break
