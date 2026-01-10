import flet as ft
from ui.app import CotizadorApp

async def main(page: ft.Page):
    app = CotizadorApp(page)
    await app.iniciar()

ft.run(main)
