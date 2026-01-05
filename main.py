import flet as ft
from dollar_service import DollarService
from dollar_card import DollarCard

async def main(page: ft.Page):
    page.title = "Monitor Dólar Argentina"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 920 
    page.scroll = ft.ScrollMode.AUTO 

    monedas_favoritas = ["Oficial", "Blue", "Cripto", "Tarjeta"]

    
    page.add(
        ft.Row(
            controls=[
                ft.Text("Cotizaciones en vivo", size=24, weight="bold")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    # Contenedor donde pondremos todas las tarjetas (Columna)
    contenedor_tarjetas = ft.Column(spacing=10)
    
    # Loader visual
    loader = ft.ProgressBar(width=200, color="blue")
    page.add(loader)

    # 1. Instanciar servicio
    servicio = DollarService()

    # 2. Obtener datos
    datos = await servicio.get_cotizaciones()

    # 3. Eliminar loader
    page.remove(loader)

    # 4. Crear una tarjeta por cada dólar recibido
    for dolar in datos:
        nombre_actual = dolar["nombre"]
        # La API devuelve claves: "nombre", "compra", "venta"
        if nombre_actual in monedas_favoritas:
            tarjeta = DollarCard(
            nombre=nombre_actual,
            compra=dolar["compra"],
            venta=dolar["venta"]
        )
        
            contenedor_tarjetas.controls.append(tarjeta)

    # 5. Agregar el contenedor lleno a la página
    page.add(contenedor_tarjetas)
    page.update()

ft.app(target=main)