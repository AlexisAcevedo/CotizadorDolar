import flet as ft
from services.dollar_service import DollarService
from ui.components.dollar_card import DollarCard


class CotizadorApp:
    """Clase principal de la aplicación de cotizaciones de dólar."""
    
    def __init__(self, page: ft.Page):
        """
        Inicializa la aplicación.
        
        Args:
            page: Instancia de la página de Flet
        """
        self.page = page
        self.servicio = DollarService()
        
        # Referencias a componentes UI
        self.titulo = None
        self.txt_fecha = None
        self.header = None
        self.loader = None
        self.contenedor_tarjetas = None
        self.btn_actualizar = None
        
        # Inicializar UI
        self._configurar_ventana()
        self._crear_componentes()
        self._construir_layout()
    
    def _configurar_ventana(self):
        """Configura las propiedades de la ventana de la aplicación."""
        self.page.title = "Monitor Dólar Argentina"
        self.page.theme_mode = ft.ThemeMode.DARK
        
        # Configurar dimensiones
        self.page.window.width = 400
        self.page.window.height = 1060
        
        # Forzar actualización de la ventana antes de agregar contenido
        self.page.update()
        
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 20
    
    def _crear_componentes(self):
        """Crea todos los componentes de la interfaz de usuario."""
        # Título y fecha de actualización
        self.titulo = ft.Text(
            "Cotizaciones en vivo",
            size=24,
            weight=ft.FontWeight.BOLD
        )
        self.txt_fecha = ft.Text(
            "Cargando...",
            size=14,
            color=ft.Colors.GREY_500
        )
        
        self.header = ft.Column(
            controls=[self.titulo, self.txt_fecha],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        )
        
        # Loader
        self.loader = ft.ProgressBar(width=200, color=ft.Colors.BLUE_200)
        
        # Contenedor de tarjetas
        self.contenedor_tarjetas = ft.Column(spacing=10)
        
        # Botón actualizar
        self.btn_actualizar = ft.Button(
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
            on_click=self.actualizar_cotizaciones
        )
    
    def _construir_layout(self):
        """Ensambla el layout final de la aplicación."""
        self.page.add(
            self.header,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            self.contenedor_tarjetas,
            ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
            self.btn_actualizar
        )
    
    async def actualizar_cotizaciones(self, e):
        """
        Maneja la actualización de cotizaciones desde la API.
        
        Args:
            e: Evento del botón (puede ser None en la carga inicial)
        """
        # Deshabilitar botón durante la actualización
        if self.btn_actualizar:
            self.btn_actualizar.disabled = True
        
        # Limpiar contenedor y mostrar loader
        self.contenedor_tarjetas.controls.clear()
        self.contenedor_tarjetas.controls.append(self.loader)
        self.page.update()
        
        # Llamada al servicio
        datos, fecha_actualizada = await self.servicio.get_cotizaciones()
        
        # Remover loader y actualizar fecha
        self.contenedor_tarjetas.controls.remove(self.loader)
        self.txt_fecha.value = fecha_actualizada
        
        # Agregar tarjetas con los datos
        if datos:
            for dolar in datos:
                tarjeta = DollarCard(
                    nombre=dolar["nombre"],
                    compra=dolar["compra"],
                    venta=dolar["venta"]
                )
                self.contenedor_tarjetas.controls.append(tarjeta)
        else:
            self.contenedor_tarjetas.controls.append(
                ft.Text("Error de conexión", color="red")
            )
        
        # Rehabilitar botón
        if self.btn_actualizar:
            self.btn_actualizar.disabled = False
        
        self.page.update()
    
    async def iniciar(self):
        """Realiza la carga inicial de datos."""
        await self.actualizar_cotizaciones(None)
