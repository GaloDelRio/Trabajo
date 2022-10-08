
# Variables constantes 

iva=.76 
lista_cambios=[]


# Funciones

def ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales):
    operacion=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    return operacion

def texto_chistoso(resultado):
    if resultado > 0:
        print ("Tienes",resultado, "pesos, te gustaria invertir en NFTEC?")
    else:
        print (("Tienes",resultado,"pesos, eres pobre bienvenido a LATAM"))

def agregar_ingresos (resultado):
    i=0
    pregunta=str(input("¿Te gustaría agregar dinero?   y/n"))
        while i!=1:
        if pregunta=="y":
            respesta_pregunta=float(input("¿Cuanto dinero te gustaría agregar?"))
            lista_cambios.append(resultado)
            resultado=resultado+respesta_pregunta
            print("Actualmente tienes",resultado)
            lista_cambios.append(resultado)
        elif pregunta=="n":
            print("tu saldo para el mes es de", resultado)
            print(lista_cambios)
            i=i+1

def meses ():
    pregunta2=str(input("¿Te gustaría revisar aguno de los cabios que realizaste?"  y/n))
    if pregunta2 = "y"
        print(lista_meses)
    elif print("Gracias por utilizar el programa")
        break
    



# Menu

opcion = str(input("¿Quieres usar dolares o pesos?"))
if(opcion == "pesos"):
    ingreso_mensual = float(input("ingresa el ingreso mensual"))
    gastos_constante = float(input("ingresa gastos contantes o servicios del mes"))
    gastos_adicionales = float(input("ingresa gastos adicionales promedio"))
    resultado=ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales)
    lista_cambios.append(resultado)
    texto_chistoso(resultado)
    agregar_ingresos (resultado)
    lista_meses=["primer mes",resultado],["segundo mes",resultado*2],["tercer mes",resultado*3],["cuarto mes",resultado*4],["quinto mes",resultado*5],["sexto mes",resultado*6]
    meses()
