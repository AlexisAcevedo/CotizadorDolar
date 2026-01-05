import httpx

class DollarService:
    async def get_cotizaciones(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("https://dolarapi.com/v1/dolares")
                
                if response.status_code == 200:
                    return response.json() # Devuelve la lista completa de dólares
                else:
                    return [] # Si falla, devolvemos lista vacía
        except Exception as e:
            print(f"Error: {e}")
            return []