# 🏦 Fintech Credit Advisor

Sistema inteligente de evaluación de créditos desarrollado con FastAPI y Streamlit, que utiliza modelos GenAI para proporcionar asesoramiento crediticio personalizado.

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema completo de evaluación de crédito que incluye:

- **Backend API**: Servicio FastAPI con agentes inteligentes para evaluación crediticia
- **Frontend Web**: Interfaz de chat moderna desarrollada con Streamlit
- **Procesamiento de Datos**: Análisis automático de solicitudes de crédito
- **Sistema de Conversación**: Chat interactivo para recopilar información del usuario

## 🏗️ Estructura del Proyecto

```
seg_bolivar_challenge/
├── data/                           # Datos de solicitudes de crédito
│   └── solicitudes_credito_simuladas.csv
├── docs/                           # Documentación y políticas
│   ├── advisor.txt
│   └── politicas.txt
├── notebooks/                      # Análisis exploratorio de datos
│   ├── eda_report.html
│   └── exploracion_datos.ipynb
├── src/                           # Código fuente principal
│   ├── agent.py                   # Agentes de IA para evaluación
│   ├── app.py                     # Aplicación frontend Streamlit
│   ├── config.py                  # Configuración de la aplicación
│   ├── schemas.py                 # Esquemas de validación de datos
│   ├── tools.py                   # Herramientas de consulta de datos
│   ├── utils.py                   # Utilidades del frontend
│   └── api/
│       └── routes.py              # Rutas de la API FastAPI
├── requirements.txt               # Dependencias del proyecto
├── start.sh                       # Script de inicio para Linux/Mac
├── start.bat                      # Script de inicio para Windows
└── README.md                      # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <repository-url>
   cd seg_bolivar_challenge
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno** (opcional):
   ```bash
   # Crear archivo .env
   echo "API_BASE_URL=http://localhost:8000" > .env
   echo "API_TIMEOUT=30" >> .env
   ```

## 🎯 Ejecución de la Aplicación

### Opción 1: Script Automático (Recomendado)

**En Windows**:
```cmd
start.bat
```

**En Linux/Mac**:
```bash
chmod +x start.sh
./start.sh
```

### Opción 2: Ejecución Manual

**1. Iniciar el Backend (Terminal 1)**:
```bash
uvicorn src.api.routes:router --host localhost --port 8000 --reload
```

**2. Iniciar el Frontend (Terminal 2)**:
```bash
streamlit run src/app.py --server.port 8501
```

### Opción 3: Servicios Individuales

**Solo Backend**:
```bash
./start.sh backend    # Linux/Mac
start.bat backend     # Windows
```

**Solo Frontend**:
```bash
./start.sh frontend   # Linux/Mac
start.bat frontend    # Windows
```

## 🌐 Acceso a la Aplicación

Una vez iniciados los servicios:

- **Frontend (Chat)**: http://localhost:8501
- **Backend API (Documentación)**: http://localhost:8000/docs
- **Backend API (Redoc)**: http://localhost:8000/redoc

## 💬 Uso del Sistema

### Flujo de Conversación

1. **Accede** al frontend en tu navegador
2. **Inicia** una conversación proporcionando tu información:
   - ID de usuario
   - Edad
   - Ingresos mensuales
   - Región de residencia
   - Justificación para el crédito

3. **Interactúa** con el asistente que te guiará paso a paso
4. **Recibe** la evaluación crediticia final con justificación

### Ejemplo de Conversación

```
Usuario: Hola, quiero solicitar un crédito
Asistente: ¡Hola! Te ayudo con tu solicitud. ¿Podrías proporcionarme tu ID de usuario?

Usuario: Mi ID es 12345
Asistente: Perfecto. ¿Cuál es tu edad?

Usuario: Tengo 35 años
Asistente: Gracias. ¿Cuáles son tus ingresos mensuales?
...
```

## 🛠️ Arquitectura Técnica

### Backend (FastAPI)

- **Agentes Inteligentes**: Procesamiento de lenguaje natural para recopilar información
- **Sistema de Evaluación**: Análisis crediticio basado en políticas predefinidas
- **API RESTful**: Endpoints para chat y evaluación directa
- **Validación de Datos**: Esquemas Pydantic para integridad de datos

### Frontend (Streamlit)

- **Interfaz de Chat**: Chat en tiempo real con el asistente
- **Estado de Sesión**: Mantenimiento del historial de conversación
- **Diseño Responsivo**: Interfaz moderna y profesional
- **Manejo de Errores**: Feedback claro para problemas de conectividad

## 🔧 Configuración Avanzada

### Variables de Entorno

| Variable | Descripción | Valor por Defecto |
|----------|-------------|-------------------|
| `API_BASE_URL` | URL base del backend | `http://localhost:8000` |
| `API_TIMEOUT` | Timeout para requests | `30` |
| `MAX_CONVERSATION_LENGTH` | Máximo de mensajes en conversación | `50` |

### Personalización

- **Estilos CSS**: Modifica `src/utils.py` para cambiar la apariencia
- **Configuración**: Ajusta `src/config.py` para modificar comportamientos
- **Agentes**: Personaliza `src/agent.py` para cambiar la lógica de evaluación

## 🧪 Testing

Para ejecutar las pruebas (cuando estén disponibles):

```bash
# Instalar dependencias de desarrollo
pip install pytest

# Ejecutar pruebas
pytest tests/
```

## 📊 Monitoreo y Logs

- Los logs del backend se muestran en la consola donde se ejecuta uvicorn
- Los logs del frontend aparecen en la consola de Streamlit
- Usa el endpoint `/docs` para testing manual de la API

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Agrega nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

Si encuentras problemas:

1. **Revisa los logs** en las consolas de backend y frontend
2. **Verifica la conectividad** entre frontend y backend
3. **Consulta la documentación** de la API en `/docs`
4. **Abre un issue** en el repositorio del proyecto

---

**Desarrollado con ❤️ para Seguros Bolívar**
