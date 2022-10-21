"""
Proyecto python
Simulador organizador de finanzas.
El programa realiza una serie de preguntas las cuales estan dirijidas para
poder evaluar los ingresos y egresos del usuario, dando varias reguntas clave para poder realizar 
calculos y obtener distos valores jugando con el valor mensual.
"""
# Variables constantes 

iva=.76 
lista_cambios=[]


"""
================== Funciones =====================================
"""

def meses(resultado):
    """
    (uso de listas, matrices, operadores, ciclos for)
    recibe: resultado
    crea una matriz
    devuelve: dos listas, una de la cantidad de meses y otra de los ingresos en los respectivos meses
    """
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
        print(lista_meses)

def ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales):
    """
    (uso de operadores)
    recibe: el ingreso mensual, los gastos constantes, gastos adicionales
    La funcion toma el ingreso mensual y le descuenta los gastos constantes 
    los cuales son afectados por el iva, ademas de reducir los gastos adicionales .
    devuelve: El ingreso mensual neto 
    """
    operacion=ingreso_mensual-(gastos_constante*iva)-gastos_adicionales
    return operacion

def texto_chistoso(resultado):
    """
    (uso de boleanos, condicionales)
    recibe: el resultado/ingreso neto
    Hace una comparación para saber si el ingreso es positivo o negattivo.
    devuelve: un texto para saber si el ingreso es positivo o negatino
    """
    if resultado > 0:
        print ("Tienes",resultado, ", te gustaria invertir en NFTEC?")
    else:
        print (("Tienes",resultado,", eres pobre bienvenido a LATAM"))

def agregar_ingresos (resultado):
    """
    (uso de ciclos while, condicionales, listas)
    recibe: el resultado/ingreso neto
    funcion auxiliar que sirve para agregar dinero en caso de que el ingreso neto no sea la cantidad deseada
    o que se quieran realizar ciertos cambios 
    devuelve: una lista de cambios además de imprimir el ingreso neto modificado
    """
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
    """
    (uso de listas, condicionales)
    recibe: la lista de cambios
    funcion auxiliar qe sirve para revisar la lista de cambios para buscar algun error 
    si es deseado
    devuelve: un lista de cambios si es deseado
    """
    pregunta2=str(input("¿Te gustaría revisar alguno de los cambios que realizaste?  y/n \n"))
    if pregunta2 == "y":
        print(lista_cambios)



"""
================== Menu =====================================
"""

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
elif (opcion == "dolares"):
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

"""

============================ Error 1 =====================================


Sub-Competencia: 
	componente: usa la forma más a apropiada al problema para guardar los datos (listas, variable, tipo de dato, etc...) (avance 6)  (listas)

Error original: Solo imprimia una lista en vez de hacer algo con la misma

	lista de cambio=[]:
		print (lista de cambios) 

Cambio realizado: utile las listas con otras aplicaciones

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
    
pregunta2=str(input("¿Te gustaría revisar alguno de los cambios que realizaste?  y/n \n"))
    if pregunta2 == "y":
        print(lista_cambios)


Líneas de código donde se ve la corrección: 66 a 85 y 87 a 98

============================ Error 2 =====================================


Sub-Competencia: 
	Aplica funciones de manera adecuada para segmentar el código y mantener reusabilidad y modularidad (avance 2)

Error original: "Observaciones:
el Menu no esta biene estructurado.
"			

Cambio realizado: agrege el comparativo dolares además de ajustar las funciones
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
	elif (opcion == "dolares"):
        ingreso_mensual = float(input(f"ingresa el ingreso mensual: \n"))
        gastos_constante = float(input(f"ingresa gastos contantes o servicios del mes: \n"))
        gastos_adicionales = float(input(f"ingresa gastos adicionales promedio: \n"))
        resultado=ingreso_mensual_total (ingreso_mensual,gastos_constante,gastos_adicionales)
        lista_cambios.append(resultado)
        texto_chistoso(resultado)
        agregar_ingresos (resultado)
        cambios(lista_cambios)
        meses(resultado)

Líneas de código donde se ve la corrección: 105 a 125

   """     

