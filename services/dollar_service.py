import httpx
from datetime import datetime
import pytz

class DollarService:
    async def get_cotizaciones(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("https://dolarapi.com/v1/dolares")
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # 1 Definimos los tipos de dolar que queremos
                    orden_deseado = ["oficial", "blue", "cripto", "tarjeta"]
                    resultados = []
                    fecha_str = "Fecha desconocida"
                    fecha_detectada = False

                    for item in data:
                        nombre = item.get("casa", "").lower()
                        
                        if nombre in orden_deseado:
                            # Agregamos a la lista
                            resultados.append({
                                "nombre": nombre.capitalize(),
                                "compra": item.get("compra"),
                                "venta": item.get("venta")
                            })

                            # 2 Capturamos la fecha del primer item válido
                            if not fecha_detectada and item.get("fechaActualizacion"):
                                try:
                                    # La API devuelve UTC
                                    fecha_raw = item.get("fechaActualizacion")
                                    fecha_utc = datetime.fromisoformat(fecha_raw.replace("Z", "+00:00"))
                                    
                                    # Convertimos a hora Argentina
                                    zona_arg = pytz.timezone('America/Argentina/Buenos_Aires')
                                    fecha_arg = fecha_utc.astimezone(zona_arg)
                                    
                                    # Formateamos para la UI
                                    fecha_str = fecha_arg.strftime("Actualizado: %d/%m/%Y %H:%M")
                                    fecha_detectada = True
                                except Exception as e:
                                    print(f"Error parseando fecha: {e}")

                    # 3 Ordenamos la lista según el orden_deseado
                    resultados.sort(key=lambda x: orden_deseado.index(x["nombre"].lower()))

                    # Devolvemos la lista limpia y la fecha
                    return resultados, fecha_str
                
                else:
                    return [], "Error de API"
                    
        except Exception as e:
            print(f"Error en servicio: {e}")
            return [], "Error de conexión"