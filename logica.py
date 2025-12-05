"""

=========================
CALCULADORA V4.0 (MODULAR)
=========================

"""

#print("--- Calculadora v4.0 (Modular) ---")

#Creacion de la lista para la memoria de la calculadora
#historial = []

# ====================
# ZONA DE HERRAMIENTAS
# ====================

"""
    INFORMACION def
¿Como escribir una funcion?

Estructura:
def == le indica a python la creacion de una nueva herramienta
nombre_algo == es el nombre de la herramienta
(algo) == parámetros o argumentos 
            - son las entradas de la maquina
            - variables que solo existen dentro de la funcion
            - recibe los datos que se le envian desde afuera
                -si los datos vienen de afuera, este parametro indica qué valor va a tomar
            - pueda quedar como () no necesita datos para trabajar, la funcion en su cuerpo los pide (como la funcion sistema 2x2)
sintaxis:

def nombre_algo(algo):
    #cuerpo de la funcion
"""

    #INFORMACION IMPORTANTE !!!!
    # MODIFICACION DEL CODIGO PARA HACERLO APP
    #SE VAN A BORRAR TODOS LOS PRINT E INPUT'S


"""
def pedir_Numero(texto):
    
    Solicita un número al usuario repetidamente hasta obtener un float válido.
    Parámetros: texto (str) - El mensaje a mostrar.
    Retorna: float
    
    Es una funcion con un () relleno porque en la posteridad se introduce este valor
    'texto' es nuestro valor de entrada:
        - Está en el parametro de la funcion, y es el receptor de datos
            - Entra en juego para cualquier valor de entrada
        - Cuando se recibe el valor mediante 'input(texto)':
            -La función usa 'texto' para mostrar el mensaje, y guarda lo que el usuario teclea en 'entrada
        -Se verifica si 'entrada' es un numero:
            -sino, entonces manda un error y se llama a 'except ValueError' 
    
    while True: #Evalua la introduccion de un numero
        try:
            #Logica para asegurarse que se introduce un numero
            entrada = input(texto) #Entrada generica para cualquier numero
            n = float(entrada) #Se espera recibir un numero decimal, sino entonces entra 'except'
            return n
        except ValueError: #Sino es un numero lo indica con un print, y se repite hasta que reciba un numero
            print(f"Error {entrada} no es un numero. Intentalo de nuevo")
"""
            
def calcular_aritmetica(operador, n1, n2):
    #Logica para elegir el operador
    #Igual es una funcion con () relleno ya que en el cuerpo principal se crean estos valores

    """
        INFORMACION match
    ¿Como escribir un 'match'?

    Estructura:
    match == es el nombre de la funcion
                - reemplaza muchos ' if's '
    parametro == es el parametro a evaluar
    case "algo" == si el parametro se encuentra en algun caso, se ejecuta ese caso
    case _: == equivalente a 'default' en C
    return None == en dado caso que no se cumpla ninguno retorna un None para no romper con la logica del programa
    Sintaxis:

    match parametro:
        case "...":
            #cuerpo de este case
        case "2...":
            #cuerpo de este case
        case "3...":
            #cuerpo de este case
        case _:
            return None #equivalente a 'default'
    """
    match operador:
        case "+":
            return n1+n2
        case "-":
            return  n1-n2
        case "*":
            return n1*n2
        case "/":
            if n2 == 0:
                #print("Error critico: Division entre cero.")
                return "Error: Div entre 0"
            return n1/n2
        case _:
            #equivalente a 'default' en C
            return None

def resolver_sistema_2x2(a1,b1, c1,  a2, b2, c2):
    #Solicita 6 coeficientes y resuelve por Cramer
    #Retorna un string formateado con la solucion o None
    #EL PARENTESIS NO NECESITA PARAMETROS, SE CREAN DENTRO DE LA FUNCION

    #print("\n--- Sistema de ecuaciones 2x2 (Cramer) ---")
    #print("Forma: ax + by = c")

    """
    #Inputs solo necesarios para esta funcion y en esta funcion (he aqui la ausencia de parametros en el parentesis de la funcion)
    print("-> Ecuacion 1:")
    #Se manda a llamar a pedir_numero(texto)
    
    a1 = pedir_Numero(" a1 (x): ")
    b1 = pedir_Numero(" b1 (y): ")
    c1 = pedir_Numero(" c1 (res): ")

    print("-> Ecuacion 2:")
    a2 = pedir_Numero(" a2 (x): ")
    b2 = pedir_Numero(" b2 (y): ")
    c2 = pedir_Numero(" c2 (res): ")
    """
    #1. Determinante del sistema (D)

    det_sistema = (a1*b2) - (a2*b1)

    #Validacion del determinante (si son rectas paralelas/coincidentes)
    if det_sistema == 0:
        #print("Error: Determinante (D) es 0, sin solucion unica")
        return None
    
    #2. Determinante de incognitas

    det_x = (c1*b2) - (c2*b1)
    det_y = (a1*c2) - (a2*c1)

    #3. Obtención de resultados
    x = det_x / det_sistema
    y = det_y / det_sistema

    #Antes de devolver los valores se formatea el texto

    return f" x = {x: .2f}, y = {y: .2f} "


def resolver_sistema_3x3(a1,b1, c1, d1,  a2, b2, c2, d2,  a3, b3, c3, d3):

    #print("\n--- Sistema de ecuaciones 3x3 (Cramer) ---")
    #print("Forma: ax + by + cz = d")

    ##print("-> Ecuacion 1:")
    #Se manda a llamar a pedir_numero(texto)
    """
    a1 = pedir_Numero(" a1 (x): ")
    b1 = pedir_Numero(" b1 (y): ")
    c1 = pedir_Numero(" c1 (z): ")
    d1 = pedir_Numero(" d1 (res): ")

    print("-> Ecuacion 2:")
    a2 = pedir_Numero(" a2 (x): ")
    b2 = pedir_Numero(" b2 (y): ")
    c2 = pedir_Numero(" c2 (z): ")
    d2 = pedir_Numero(" d2 (res): ")

    print("-> Ecuacion 3:")
    a3 = pedir_Numero(" a3 (x): ")
    b3 = pedir_Numero(" b3 (y): ")
    c3 = pedir_Numero(" c3 (z): ")
    d3 = pedir_Numero(" d3 (res): ")
    """
    #Simplificando logica

    def det_3(h1, h2, h3,  h4, h5, h6,  h7, h8, h9):
        #Sarrus generica
        pos = (h1*h5*h9) + (h4*h8*h3) + (h7*h2*h6)
        neg = (h7*h5*h3) + (h1*h6*h8) + (h4*h2*h9)

        return pos - neg

    #Calculo con Sarrus generica
    det_sistema = det_3(a1, b1, c1,  a2, b2, c2,  a3, b3, c3)

    #Evaluacion determinante
    if det_sistema == 0:
        print("Error: Determinante (D) es 0, sin solucion unica")
        return None
    
    #Determinante X (Reemplazamos A con D)
    det_x = det_3(d1, b1, c1,  d2, b2, c2,  d3, b3, c3)

    #Determinante Y (Reemplazamos B con D)
    det_y = det_3(a1, d1, c1,  a2, d2, c2,  a3, d3, c3)

    #Determinante Z (Reeplazamos C con D)
    det_z = det_3(a1, b1, d1,  a2, b2, d2,  a3, b3, d3)

    #Obtencion de resultados

    x = det_x/det_sistema
    y = det_y/det_sistema
    z = det_z/det_sistema

    #Texto formateado

    return f" x = {x: .2f}, y = {y: .2f}, z = {z: .2f}"
    """

                    OBSOLETO


    #1. Determinante del sistema

    det_sistema = (a1*b2*c3 + a2*b3*c1 + a3*b1*c2) \
                - (a3*b2*c1 + a1*b3*c2 + a2*b1*c3)

    #Validacion del determinante

    if det_sistema == 0:
        print("Error: Determinante (D) es 0, sin solucion unica")
        return None
    
    #2. Determinante de incognitas
    
    det_x = (d1*b2*c3 + d2*b3*c1 + d3*b1*c2) - (d3*b2*c1 + d1*b3*c2 + d2*b1*c3)

    det_y = (a1*d2*c3 + a2*d3*c1 + a3*d1*c2) - (a3*d2*c1 + a1*d3*c2 + a2*d1*c3)

    det_z = (a1*b2*d3 + a2*b3*d1 + a3*b1*d2) - (a3*b2*d1 + a1*b3*d2 + a2*b1*d3)

    #Obtencion de resultados

    x = det_x/det_sistema
    y = det_y/det_sistema
    z = det_z/det_sistema

    #Texto formateado

    return f" x = {x: .2f}, y = {y: .2f} z = {z: .2f}"
    """
#--- Zona Principal ---
"""
while True:
    #Limpiar consola
    print("\n" + "="*40) #Imprime 40 '=' para hacer una division visual

    #Se decide qué operación se desea realizar
    print("Qué operacion desea realizar")
    print("\nOpciones: +, -, *, /, sis2, sis3: ")

    #1. Se decide qué hacer

    operador = input("Introduzca operacion:").strip().lower()
    resultado = None #Se inicializa la variable 'resultado'

    #Camino A: Sistema de Ecuaciones 2x2

    if operador == "sis2":
        resultado = resolver_sistema_2x2()

    #Camino B: Sistema de Ecuaciones 3x3

    elif operador == "sis3":
        resultado = resolver_sistema_3x3()

    #Camino C: Aritmetica Basica
    elif operador in ["+", "-", "*", "/"]:
        #Solo pedimos estos numeros si entramos en este camino
        n1 = pedir_Numero("Ingresa el primer numero: ")
        n2 = pedir_Numero("Ingresa el segundo numero: ")

        #Uso de la funcion calculadora_aritmetica
        #Operador y ambos numeros ya definidos
        resultado = calcular_aritmetica(operador, n1, n2)

    #Camino D: Error de entrada
    else:
        print("Operador no valido, intente de nuevo")

    #2. Salida y guardado
    if resultado is not None:
        print(f"Resultado: {resultado}")
        #Agregamos el resultado anterior a la lista
        historial.append(f"[{operador.upper()}] {resultado}")
        #print(f"El resultado es: {resultado}")
    
    #3. Control del ciclo
    repeticion = input("\n¿Desea otra operación? (s/n): ")
    if repeticion.strip().lower() in ["n", "no"]:
        print("\n--- Historial de sesion ---")
        for i, item in enumerate(historial, 1):
            print(f"{i}. {item}")
        print("Cerrando sistema...")
        break
"""