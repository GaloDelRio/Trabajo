
# Variables constantes 

from tokenize import PseudoExtras


iva=.76 
lista_cambios=[]


# Funciones

def meses(resultado):
    preugunta4=str(input("¿Te gustaría saber cual sera tu ingreso en los siguientes meses? y/n \n"))
    if preugunta4=="y":
        mes = int(input('Dame los meses: \n'))
        matriz = []
        for x in range(2):
            matriz.append([])
            for y in range(mes):
                if x == 0:
                    matriz[x].append(y+1)
                elif x == 1:
                    matriz[x].append(resultado * matriz[0][y])
        print(matriz)
    else:
        print("Gracias por utilzar el programa")

def ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales):
    operacion=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    return operacion

def texto_chistoso(resultado):
    if resultado > 0:
        print ("Tienes",resultado, "pesos, te gustaria invertir en NFTEC?")
    else:
        print (("Tienes",resultado,"pesos, eres pobre bienvenido a LATAM"))

def agregar_ingresos (resultado):
    i=1
    pregunta = input("¿Te gustaría agregar dinero?   y/n \n")
    while i==1:
        if pregunta=="y":
            respuesta_pregunta=float(input("¿Cuanto dinero te gustaría agregar? \n"))
            resultado=resultado+respuesta_pregunta
            lista_cambios.append(resultado)
            print("Actualmente tienes",resultado)
            pregunta = str(input("¿Te gustaría seguir agregando dinero?   y/n \n"))
        elif pregunta=="n":
            print("tu saldo para el mes es de", resultado)
            i=i+1
        
def cambios (lista_cambios):
    pregunta2=str(input("¿Te gustaría revisar alguno de los cambios que realizaste?  y/n \n"))
    if pregunta2 == "y":
        print(lista_cambios)



# Menu

opcion = str(input(f"¿Quieres usar dolares o pesos?: \n"))
if(opcion == "pesos"):
    ingreso_mensual = float(input(f"ingresa el ingreso mensual: \n"))
    gastos_constante = float(input(f"ingresa gastos contantes o servicios del mes: \n"))
    gastos_adicionales = float(input(f"ingresa gastos adicionales promedio: \n"))
    resultado=ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales)
    lista_cambios.append(resultado)
    texto_chistoso(resultado)
    agregar_ingresos (resultado)
    cambios(lista_cambios)
    meses(resultado)
    


    lista_meses=[["primer mes",resultado],["segundo mes",resultado*2],["tercer mes",resultado*3],["cuarto mes",resultado*4],["quinto mes",resultado*5],["sexto mes",resultado*6]]
    

