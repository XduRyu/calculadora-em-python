import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window_width = 100
    page.window_height = 200



    todos_valores=""
    
    resultado_texto = ft.Text(value="0", size=28, color="white", text_align="right")

    def entrar_valores(e):
        nonlocal todos_valores
        todos_valores+= str(e.control.text)
        resultado_texto.value = todos_valores
        page.update() 

    def limpar_tela(e):
        nonlocal todos_valores
        todos_valores = ""
        resultado_texto.value = "0"
        page.update()

    def calcular(e):
        nonlocal todos_valores
        try:
            todos_valores = todos_valores.replace('%', '/100')
            resultado_texto.value = str(eval(todos_valores))
            
            todos_valores = resultado_texto.value
        except: 
            resultado_texto.value= "Error"
            todos_valores= ""
        page.update() 

    def apagar_ultimo_caractere():
        nonlocal todos_valores
        todos_valores = todos_valores[:-1]
        resultado_texto.value = todos_valores if todos_valores else "0"
        page.update()


    
    tela = ft.Container(
        content=resultado_texto,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment= ft.alignment.center_right
    
    
    )


    # estilizacao dos botoes
    estilo_numeros = {
    "height": 60,
    "bgcolor": "#4d4d4d",
    "color": "white",
    "expand": 1,
    }
    estilo_operadores = {
    "height": 60,
    "bgcolor": "#FF9500",
    "color": "white",
    "expand": 1,
    }
    estilo_limpar = {
    "height": 60,
    "bgcolor": "#FF3B30",
    "color": "white",
    "expand": 1,
    }
    estilo_equal = {
    "height": 60,
    "bgcolor": "#34C759",
    "color": "white",
    "expand": 1,
    }


    grelha_de_botoes=[

        [
            ("C",estilo_limpar,limpar_tela),
            ("%",estilo_operadores,entrar_valores),
            ("/",estilo_operadores,entrar_valores),
            ("*",estilo_operadores,entrar_valores)
        ],  

        [
            ("7",estilo_numeros,entrar_valores),
            ("8",estilo_numeros,entrar_valores),
            ("9",estilo_numeros,entrar_valores),
            ("-",estilo_operadores,entrar_valores)
        ],

        [
            ("4",estilo_numeros,entrar_valores),
            ("5",estilo_numeros,entrar_valores),
            ("6",estilo_numeros,entrar_valores),
            ("+",estilo_operadores,entrar_valores)
        ],  

        [
            ("1",estilo_numeros,entrar_valores),
            ("2",estilo_numeros,entrar_valores),
            ("3",estilo_numeros,entrar_valores),
            ("=",estilo_equal, calcular)
        ],  

        [
            ("0", {**estilo_numeros, "expand":2},entrar_valores),
            (".",estilo_numeros, entrar_valores),
            ("⌫", estilo_operadores, lambda e: apagar_ultimo_caractere())

        ],     


    ]


    botoes=[]

    for linha in grelha_de_botoes:
        linha_control= []
        for texto, estilo, handler in linha:
            btn = ft.ElevatedButton(
                    text=texto,
                    on_click= handler,
                    **estilo,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=5),
                        padding=0
                    )
                    
            )
            linha_control.append(btn)
        botoes.append(ft.Row(linha_control, spacing=5))    


    
    page.add(
        ft.Column(
            [
                tela,
                ft.Column(botoes,spacing=5)
            
            ]
            )
        )

ft.app(target=main)
