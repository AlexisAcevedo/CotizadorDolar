import flet as ft

class DollarCard(ft.Card):
    def __init__(self, nombre, compra, venta):
        super().__init__()
        
        # Formateamos los valores (si compra es 1000, queda $1000)
        lbl_compra = f"${compra}"
        lbl_venta = f"${venta}"

        # Diseño interno de la tarjeta
        self.content = ft.Container(
            content=ft.Column(
                [
                    # Título
                    ft.Text(value=nombre, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_200),
                    
                    ft.Divider(color=ft.Colors.GREY_600),
                    
                    # Fila con Compra y Venta
                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("Compra", size=14, color=ft.Colors.WHITE),
                                ft.Text(lbl_compra, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                            ]),
                            
                            ft.Icon(ft.Icons.ARROW_RIGHT_ALT),    
                            ft.Column([
                                ft.Text("Venta", size=14, color=ft.Colors.WHITE),
                                ft.Text(lbl_venta, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)
                            ]),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
            ),
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.GREY_800,
        )