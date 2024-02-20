import flet as ft
from obtenerAMC import obtenerAccidenteMasComun

colonia = ""

def main(page: ft.Page):
    def reproducirAudio():
        audio = ft.Audio(
            src="assets/mensaje.mp3", autoplay=True
        )
        page.overlay.append(audio)
        page.update()

    def obtenerColonia(e):
        global colonia
        colonia = textColonia.value
        print(colonia)
        obtenerAccidenteMasComun(colonia)
        reproducirAudio()
        return colonia
    
    page.appbar = ft.AppBar(
        title=ft.Text("Proyecto PLN"),
        bgcolor=ft.colors.GREEN_400,
    )
    page.window_width = 720
    page.window_height = 1280
    

    textColonia = ft.TextField(
                    label="Colonia", 
                    border_color=ft.colors.WHITE, 
                    color=ft.colors.WHITE, 
                    focused_bgcolor=ft.colors.WHITE)
    boton =  ft.IconButton(
                    icon=ft.icons.PLAY_ARROW,
                    icon_color="blue400",
                    icon_size=40,
                    tooltip="Ejecutar",
                    on_click=obtenerColonia
                )
    columna = ft.Column(spacing=0, controls=[
        ft.Row([
            textColonia,
            boton,
        ])
    ])

    contenedorPrincipal = ft.Container(columna, width=720, height=1280)
    print(textColonia.value)
    page.add(contenedorPrincipal)
    
    

ft.app(target=main, assets_dir="./assets/")