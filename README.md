# 🏦 Fintech Credit Advisor

Sistema inteligente de evaluación de solicitudes de crédito utilizando GenAI (Gemini) con FastAPI para ofrecer recomendaciones personalizadas basadas en políticas crediticias predefinidas.

## 📋 Descripción del Proyecto

Este proyecto implementa un evaluador de créditos basado en IA que:

- Utiliza el modelo Gemini de Google para analizar solicitudes de crédito
- Evalúa cada solicitud según políticas crediticias documentadas
- Implementa una API REST para integración con sistemas externos
- Proporciona un flujo conversacional guiado para captura de información
- Analiza y compara resultados entre decisiones humanas y de IA

## 🔍 Análisis de Datos y Aprendizaje

El proyecto incluye análisis exploratorio detallado en notebooks que:

- Examina patrones en aprobaciones/rechazos según criterios específicos
- Valida reglas de negocio con datos históricos (ingresos, score crediticio)
- Compara decisiones del agente IA vs decisiones históricas
- Identifica casos especiales donde las políticas son flexibilizadas

## 🧠 Modelo de IA y Técnicas de Prompt

- **Modelo**: Google Gemini (accedido vía Google GenAI SDK)
- **Técnicas de Prompt**:
  - **Prompt Estructurado**: Formato específico con datos del cliente y políticas
  - **In-Context Learning**: Uso de reglas de negocio como contexto en cada solicitud
  - **JSON Schema Enforcement**: Respuestas estructuradas usando esquemas Pydantic
  - **Role-Based Prompt**: Instrucciones específicas para comportarse como experto crediticio

## 🏗️ Estructura del Proyecto

```
seg_bolivar_challenge/
├── data/                         # Datos para análisis y pruebas
│   ├── solicitudes_credito_simuladas.csv  # Dataset de prueba
│   └── resultados_evaluador.csv  # Resultados de evaluación IA
├── docs/                         # Documentación y políticas
│   ├── advisor.txt               # Instrucciones para agente conversacional
│   └── politicas.txt             # Políticas de evaluación crediticia
├── notebooks/                    # Análisis exploratorio
│   ├── exploracion_datos.ipynb   # EDA de solicitudes históricas
│   ├── comparacion_resultados.ipynb  # Comparativa IA vs decisiones históricas
│   └── eda_report.html           # Reporte generado con Sweetviz
├── src/                          # Código fuente
│   ├── agent.py                  # Implementación de agentes IA (advisor/evaluator)
│   ├── schemas.py                # Esquemas Pydantic para validación
│   ├── tools.py                  # Herramientas de consulta de datos
│   ├── main.py                   # Punto de entrada FastAPI
│   └── api/
│       └── routes.py             # Endpoints de la API
├── test_evaluator.py             # Script para validación masiva
└── requirements.txt              # Dependencias del proyecto
```

## 💻 API y Arquitectura

- **Backend**: FastAPI con endpoints para evaluación directa y conversacional
- **Agentes IA**:
  - `agent_advisor`: Guía la conversación para recopilar información
  - `agent_evaluator`: Toma decisiones basadas en políticas crediticias
- **Validación**: Esquemas Pydantic para garantizar estructura correcta de datos
- **Integración**: Diseño modular para conectar con sistemas front-end o externos

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8+
- Cuenta en Google AI Studio (para API key de Gemini)

### Configuración
1. Clonar repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Crear archivo `.env` con las variables:
   ```
   API_KEY=your_google_ai_key
   MODEL_NAME=gemini-1.0-pro
   ```

### Ejecución
```bash
# Iniciar API
uvicorn src.main:app --reload

# Ejecutar evaluación masiva
python test_evaluator.py
```
