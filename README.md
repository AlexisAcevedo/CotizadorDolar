# 💵 Monitor Dólar Argentina

Una aplicación de escritorio moderna y elegante para monitorear las cotizaciones del dólar en Argentina en tiempo real.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flet](https://img.shields.io/badge/Flet-0.80.1-purple.svg)

## 📋 Descripción

**Monitor Dólar Argentina** es una aplicación de escritorio desarrollada con [Flet](https://flet.dev/) que permite visualizar las cotizaciones actualizadas de diferentes tipos de dólar en Argentina. La aplicación consume datos de la API pública [DolarAPI](https://dolarapi.com/) y presenta la información de manera clara y atractiva.

### Tipos de Dólar Monitoreados

- 💼 **Dólar Oficial**
- 💵 **Dólar Blue**
- 🪙 **Dólar Cripto**
- 💳 **Dólar Tarjeta**

## ✨ Características

- ✅ **Cotizaciones en tiempo real** mediante API REST
- 🎨 **Interfaz moderna** con tema oscuro
- 📊 **Visualización clara** de precios de compra y venta
- ⚡ **Carga asíncrona** con indicador de progreso
- 📱 **Diseño responsivo** y fácil de usar
- 🔄 **Actualización automática** al iniciar la aplicación

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/AlexisAcevedo/CotizadorDolar.git
cd CotizadorDolar
```

2. **Crear un entorno virtual** (recomendado)

```bash
python -m venv venv
```

3. **Activar el entorno virtual**

- En Windows:
```bash
venv\Scripts\activate
```

- En Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instalar las dependencias**

```bash
pip install flet httpx
```

## 🎮 Uso

Para ejecutar la aplicación, simplemente ejecuta:

```bash
python main.py
```

La aplicación se abrirá en una ventana de escritorio mostrando las cotizaciones actuales del dólar.

## 🏗️ Estructura del Proyecto

```
CotizadorDolar/
│
├── main.py              # Punto de entrada de la aplicación
├── dollar_service.py    # Servicio para consumir la API de cotizaciones
├── dollar_card.py       # Componente visual para mostrar cada cotización
├── venv/                # Entorno virtual (no incluido en el repositorio)
└── README.md            # Este archivo
```

### Descripción de Archivos

- **`main.py`**: Archivo principal que configura la interfaz de usuario y orquesta la aplicación.
- **`dollar_service.py`**: Clase que maneja las peticiones HTTP asíncronas a la API de DolarAPI.
- **`dollar_card.py`**: Componente reutilizable que crea tarjetas visuales para cada tipo de dólar.

## 🛠️ Tecnologías Utilizadas

- **[Python](https://www.python.org/)**: Lenguaje de programación principal
- **[Flet](https://flet.dev/)**: Framework para crear aplicaciones multiplataforma con Python
- **[httpx](https://www.python-httpx.org/)**: Cliente HTTP asíncrono para Python
- **[DolarAPI](https://dolarapi.com/)**: API pública para obtener cotizaciones del dólar en Argentina

## 📡 API Utilizada

Este proyecto utiliza la API gratuita de [DolarAPI](https://dolarapi.com/):

```
GET https://dolarapi.com/v1/dolares
```

La API devuelve un array de objetos JSON con la siguiente estructura:

```json
[
  {
    "nombre": "Oficial",
    "compra": 1050.00,
    "venta": 1090.00
  },
  ...
]
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto:

1. Haz un fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commitea tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Ideas para Mejoras Futuras

- [ ] Agregar actualización automática periódica
- [ ] Implementar gráficos históricos de cotizaciones
- [ ] Agregar notificaciones cuando el dólar alcance cierto valor
- [ ] Permitir al usuario seleccionar qué tipos de dólar mostrar
- [ ] Agregar conversión de montos entre pesos y dólares
- [ ] Modo claro/oscuro configurable
- [ ] Exportar datos a CSV o Excel


## 👤 Autor

**Alexis**

- GitHub: [@tu-usuario](https://github.com/AlexisAcevedo)

## 🙏 Agradecimientos

- Gracias a [DolarAPI](https://dolarapi.com/) por proporcionar la API gratuita
- Gracias al equipo de [Flet](https://flet.dev/) por el excelente framework

---

⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub!
