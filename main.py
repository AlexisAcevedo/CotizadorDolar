import flet as ft
from dollar_service import DollarService
from dollar_card import DollarCard

async def main(page: ft.Page):
    # CONFIGURACIÓN DE VENTANA 
    page.title = "Monitor Dólar Argentina"
    page.theme_mode = ft.ThemeMode.DARK
    
    # Configurar dimensiones
    page.window.width = 400
    page.window.height = 1060
    
    
    # Forzar actualización de la ventana antes de agregar contenido
    page.update()
    
    page.scroll = ft.ScrollMode.AUTO 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # --- Elementos de la UI ---
    
    # Título y fecha de actualizacion
    titulo = ft.Text("Cotizaciones en vivo", size=24, weight=ft.FontWeight.BOLD)
    txt_fecha = ft.Text("Cargando...", size=14, color=ft.Colors.GREY_500)

    header = ft.Column(
        controls=[titulo, txt_fecha],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5
    )

    # Loader
    loader = ft.ProgressBar(width=200, color=ft.Colors.BLUE_200)

    # Contenedor de tarjetas
    contenedor_tarjetas = ft.Column(spacing=10)

    # Servicio
    servicio = DollarService()

    # Lógica actualizacion
    async def actualizar_cotizaciones(e):
        if "btn_actualizar" in locals() and btn_actualizar:
            btn_actualizar.disabled = True
        
        contenedor_tarjetas.controls.clear()
        contenedor_tarjetas.controls.append(loader)
        page.update()

        # Llamada al servicio
        datos, fecha_actualizada = await servicio.get_cotizaciones()

        contenedor_tarjetas.controls.remove(loader)
        txt_fecha.value = fecha_actualizada

        if datos:
            for dolar in datos:
                tarjeta = DollarCard(
                    nombre=dolar["nombre"],
                    compra=dolar["compra"],
                    venta=dolar["venta"]
                )
                contenedor_tarjetas.controls.append(tarjeta)
        else:
             contenedor_tarjetas.controls.append(
                ft.Text("Error de conexión", color="red")
            )
        
        if "btn_actualizar" in locals() and btn_actualizar:
            btn_actualizar.disabled = False
        
        page.update()

    # Botón actualizar
    btn_actualizar = ft.Button(
        content=ft.Row(
            [ft.Icon(ft.Icons.REFRESH, size=20), ft.Text("Actualizar", size=16)],
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

    # Armado final
    page.add(
        header,
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        contenedor_tarjetas,
        ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
        btn_actualizar
    )

    await actualizar_cotizaciones(None)

ft.run(main)