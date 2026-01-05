import flet as ft
from dollar_service import DollarService
from dollar_card import DollarCard

async def main(page: ft.Page):
    #Configuración de la Ventana
    page.title = "Monitor Dólar Argentina"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 1040 
    page.scroll = ft.ScrollMode.AUTO 
    
    #Centramos el contenido horizontalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    monedas_favoritas = ["Oficial", "Blue", "Cripto", "Tarjeta"]

    #Elementos de la UI
    
    #Título
    titulo = ft.Row(
        controls=[
            ft.Text("Cotizaciones en vivo", size=24, weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    #Loader visual
    loader = ft.ProgressBar(width=200, color=ft.Colors.BLUE_200)

    # Contenedor donde pondremos todas las tarjetas
    contenedor_tarjetas = ft.Column(spacing=10)

    # Instanciamos servicio una sola vez
    servicio = DollarService()

    async def actualizar_cotizaciones(e):
        #Preparamos la UI: Limpiamos lista y mostramos loader
        btn_actualizar.disabled = True #Desactivamos botón para evitar spam de clicks
        contenedor_tarjetas.controls.clear()
        contenedor_tarjetas.controls.append(loader)
        page.update()

        #Obtenemos datos frescos
        datos = await servicio.get_cotizaciones()

        #Quitamos el loader
        contenedor_tarjetas.controls.remove(loader)

        #Llenamos con las nuevas tarjetas
        for dolar in datos:
            nombre_actual = dolar["nombre"]
            if nombre_actual in monedas_favoritas:
                tarjeta = DollarCard(
                    nombre=nombre_actual,
                    compra=dolar["compra"],
                    venta=dolar["venta"]
                )
                contenedor_tarjetas.controls.append(tarjeta)
        
        #Reactivamos el botón
        btn_actualizar.disabled = False
        page.update()

    #Botón de Actualizar
    btn_actualizar = ft.ElevatedButton(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.REFRESH, size=20),
                ft.Text("Actualizar", size=16)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        ),
        width=280, 
        height=50,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        on_click=actualizar_cotizaciones
    )

    #Armado de la Página
    page.add(
        titulo,
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        contenedor_tarjetas,
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        btn_actualizar
    )

    #Primera carga automática al abrir la app
    await actualizar_cotizaciones(None)

ft.app(target=main)