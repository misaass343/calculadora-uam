import flet as ft
# Importamos tus funciones de logica.py
from logica import calcular_aritmetica, resolver_sistema_2x2, resolver_sistema_3x3

def main(page: ft.Page):
    # Configuración de la ventana
    page.title = "Calculadora Ingeniería V4"
    page.window_width = 450
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.LIGHT

    # ==========================================
    # 1. PESTAÑA ARITMÉTICA (Ejemplo Guía)
    # ==========================================
    
    # a) Crear los controles (Inputs)
    # Usamos ref para tener una referencia directa al control si lo necesitamos
    txt_n1 = ft.TextField(label="Número 1", width=100, text_align="center")
    txt_n2 = ft.TextField(label="Número 2", width=100, text_align="center")
    
    # Dropdown para elegir operación
    dd_operacion = ft.Dropdown(
        width=80,
        value="+", # Valor por defecto
        options=[
            ft.dropdown.Option("+"),
            ft.dropdown.Option("-"),
            ft.dropdown.Option("*"),
            ft.dropdown.Option("/"),
        ]
    )
    
    # Texto donde saldrá el resultado
    lbl_res_basica = ft.Text(value="Resultado: ", size=20, weight="bold")

    # b) La función que conecta el botón con la lógica
    def click_basica(e):
        try:
            # 1. Obtener datos de la pantalla
            v1 = float(txt_n1.value)
            v2 = float(txt_n2.value)
            op = dd_operacion.value
            
            # 2. Llamar a TU cerebro (logica.py)
            res = calcular_aritmetica(op, v1, v2)
            
            # 3. Mostrar resultado
            if res is None:
                lbl_res_basica.value = "Error Matemático"
                lbl_res_basica.color = "red"
            else:
                lbl_res_basica.value = f"Resultado: {res}"
                lbl_res_basica.color = "black"
                
        except ValueError:
            lbl_res_basica.value = "Error: Ingresa solo números"
            lbl_res_basica.color = "red"
        
        # IMPORTANTE: Actualizar la página para ver cambios
        page.update()

    # c) El botón
    btn_basica = ft.ElevatedButton("Calcular", on_click=click_basica)

    # d) Empaquetado (Layout)
    # Row = Fila (Horizontal) | Column = Columna (Vertical)
    contenido_basica = ft.Column([
        ft.Text("Operaciones Básicas", size=20),
        ft.Row([txt_n1, dd_operacion, txt_n2], alignment=ft.MainAxisAlignment.CENTER),
        btn_basica,
        ft.Divider(), # Una linea divisoria
        lbl_res_basica
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)


    # ==========================================
    # 2. ZONA DE RETO: SISTEMA 2x2
    # ==========================================
    # Aquí es donde tú programas.
    # Tienes que replicar la lógica de arriba pero para 6 inputs.
    
    # PISTA 1: Crea 6 TextFields. Nómbralos in_a1, in_b1, in_c1, etc.
    # PISTA 2: Usa ft.Row para ponerlos bonitos (ej: [in_a1, texto_x, in_b1, texto_y...])
    
    # --- ESCRIBE TU CÓDIGO AQUÍ ---

    # a) Entrada de todos los numeros

    #Encabezados

    ancho_num = 60
    ancho_sig = 20

    encabezados_2x2 = ft.Row(
        [
            ft.Text("x", width=ancho_num, text_align="center", weight="bold"),
            ft.Text("", width=ancho_sig),
            ft.Text("y", width=ancho_num, text_align="center", weight="bold"),
            ft.Text("", width=ancho_sig),
            ft.Text("Res", width=ancho_num, text_align="center", weight="bold"),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    in_a1 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)
    in_b1 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)
    in_c1 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)

    in_a2 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)
    in_b2 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)
    in_c2 = ft.TextField(width=60, height=40, text_size=14, text_align="center", content_padding=10)

    # Texto donde se imprime el resultado del sistema
    lbl_res_sist_2x2 = ft.Text(value="Resultado del sistema 2x2:", size=20, weight="bold")
    
    # b) Funcion para conectar los botones con la logica

    def click_sistema_2x2(e):
        try:    
            # 1. Obtener datos de la pantalla
            x1 = float(in_a1.value)
            y1 = float(in_b1.value)
            r1 = float(in_c1.value)

            x2 = float(in_a2.value)
            y2 = float(in_b2.value)
            r2 = float(in_c2.value)

            # 2. Llamar a la funcion desde logica (resolver_sis_2x2)

            res_sistema_2x2 = resolver_sistema_2x2(x1, y1, r1, x2, y2, r2)

            # 3. Mostrar resultado

            if res_sistema_2x2 is None:
                lbl_res_sist_2x2.value = "Error Matematico: Determinante es 0"
                lbl_res_sist_2x2.color = "red"
            else:
                lbl_res_sist_2x2.value = f"Resultado: {res_sistema_2x2}"
                lbl_res_sist_2x2.color = "black"
        except ValueError:
            lbl_res_sist_2x2.value = f"Error: Ingresa solo números"
            lbl_res_sist_2x2.color = "red"
        
        #Actualizar pagina
        page.update()

    # c) Boton para realizar la operacion
    btn_sistema_2x2 = ft.ElevatedButton("Calcular", on_click=click_sistema_2x2)


    # d) Empaquetado

    fila_ec1 = ft.Row(
        [in_a1, ft.Text("x +"), in_b1, ft.Text("y ="), in_c1],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila_ec2 = ft.Row(
        [in_a2, ft.Text("x +"), in_b2, ft.Text("y ="), in_c2],
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Contenido en pantalla

    contenido_2x2 = ft.Column(
        [
        ft.Text("Sistema de Ecuaciones 2x2", size=20),
        encabezados_2x2,
        fila_ec1, #agregamos fila 1
        fila_ec2, #agregamos fila 2
        ft.Divider(),
        btn_sistema_2x2,
        lbl_res_sist_2x2,
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
        

    # ------------------------------


    # ==========================================
    # 3. PESTAÑA SISTEMA 3x3 (Futuro)
    # ==========================================

    # a) Entrada de todos los numeros

    #Encabezados

    ancho_sig3 = 20

    encabezados_3x3 = ft.Row(
        [
            ft.Text("x", width=45, text_align="center", weight="bold"),
            ft.Text("", width=ancho_sig3),
            ft.Text("y", width=45, text_align="center", weight="bold"),
            ft.Text("", width=ancho_sig3),
            ft.Text("z", width=45, text_align="center", weight="bold"),
            ft.Text("=", width=20, text_align="center"), # Espacio para el signo igual
            ft.Text("Res", width=45, text_align="center", weight="bold"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    ancho_texto_3x3 = 55
    text_size_3x3 = 12
    largo_size_3x3 = 45



    in3_a1 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_b1 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_c1 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_d1 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)

    in3_a2 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_b2 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_c2 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_d2 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)

    in3_a3 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_b3 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_c3 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)
    in3_d3 = ft.TextField(width=ancho_texto_3x3, height=largo_size_3x3, text_size=text_size_3x3, text_align="center", content_padding=10)

    #Texto donde se imprime el resultado
    lbl_res_sist_3x3 = ft.Text(value="Resultado del sistema 3x3", size=20, weight="bold")

    #Funcion para conectar los botones con la logica

    def click_ssitema_3x3(e):
        try:
            # 1. Obtener datos de la pantalla
            x1 = float(in3_a1.value)
            y1 = float(in3_b1.value)
            z1 = float(in3_c1.value)
            r1 = float(in3_d1.value)

            x2 = float(in3_a2.value)
            y2 = float(in3_b2.value)
            z2 = float(in3_c2.value)
            r2 = float(in3_d2.value)

            x3 = float(in3_a3.value)
            y3 = float(in3_b3.value)
            z3 = float(in3_c3.value)
            r3 = float(in3_d3.value)

            # 2. Llamar a la funcion de logica

            res_sistema_3x3 = resolver_sistema_3x3(x1, y1, z1, r1,  x2, y2, z2, r2,  x3, y3, z3, r3)

            # 3. Mostrar resultado

            if res_sistema_3x3 is None:
                lbl_res_sist_3x3.value = "Error Matematico: Determinante es 0"
                lbl_res_sist_3x3.color = "red"
            else:
                lbl_res_sist_3x3.value = f"Resultado: {res_sistema_3x3}"
                lbl_res_sist_3x3.color = "black"
        except ValueError:
            lbl_res_sist_3x3.value = f"Error: Ingresa solo números"
            lbl_res_sist_3x3.color = "red"

        page.update()

    # PLUS: Funcion para limpiar las casillas
    def limpiar_3x3(e):
        # 1. Limpiamos cada fla
        #Fila 1
        in3_a1.value = ""; in3_b1.value = ""; in3_c1.value = ""; in3_d1.value = ""
        #Fila 2
        in3_a2.value = ""; in3_b2.value = ""; in3_c2.value = ""; in3_d2.value = ""
        #Fila 3
        in3_a3.value = ""; in3_b3.value = ""; in3_c3.value = ""; in3_d3.value = ""

        # 2. Reiniciamos el texto del resultado

        lbl_res_sist_3x3.value = "Resultado 3x3:"
        lbl_res_sist_3x3.color = "black"

        # 3. Colocamos el cursor en la primera casilla
        in3_a1.focus()

        # 4. Actualizamos
        page.update()

    # c) Boton para realizar la operacion
    btn_sistema_3x3 = ft.ElevatedButton("Calcular", on_click=click_ssitema_3x3)
    
    # PLUS 2: boton de borrado
    btn_borrar_3x3 = ft.ElevatedButton("Limpiar", on_click=limpiar_3x3, color="red")

    #Fila de botones para poner los DOS botones
    fila_botones_3x3 = ft.Row(
        [btn_sistema_3x3, btn_borrar_3x3],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # d) Empaquetado
    fila_3ec1 = ft.Row(
        [in3_a1, ft.Text("x +"), in3_b1, ft.Text("y +"), in3_c1, ft.Text("z ="), in3_d1],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila_3ec2 = ft.Row(
        [in3_a2, ft.Text("x +"), in3_b2, ft.Text("y +"), in3_c2, ft.Text("z ="), in3_d2],
        alignment=ft.MainAxisAlignment.CENTER
    )

    fila_3ec3 = ft.Row(
        [in3_a3, ft.Text("x +"), in3_b3, ft.Text("y +"), in3_c3, ft.Text("z ="), in3_d3],
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Contenido en pantalla
    contenido_3x3 = ft.Column(
        [
        ft.Text("Sistema de Ecuaciones 3x3", size=20),
        ft.Divider(),
        encabezados_3x3,
        fila_3ec1,
        fila_3ec2,
        fila_3ec3,
        ft.Divider(),
        fila_botones_3x3,
        lbl_res_sist_3x3,
        ], 
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # ==========================================
    # ARMADO DE PESTAÑAS
    # ==========================================
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Básicas", content=contenido_basica),
            ft.Tab(text="Sistema 2x2", content=contenido_2x2),
            ft.Tab(text="Sistema 3x3", content=contenido_3x3),
        ],
        expand=1,
    )

    page.add(t)

ft.app(target=main)
