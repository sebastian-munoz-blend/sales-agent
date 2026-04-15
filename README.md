# Sales Agent with Agentic AI

Agente inteligente para análisis de ventas que permite realizar consultas en lenguaje natural, traducirlas a SQL y generar resultados en múltiples formatos (tabla, gráfico o archivo).

---

## Descripción

Este proyecto implementa un **agente de análisis de ventas** utilizando principios de *Agentic AI*.
El agente interpreta preguntas del usuario, genera consultas SQL automáticamente y ejecuta acciones adicionales como visualización de datos o exportación de resultados.

El sistema está diseñado con una arquitectura modular que separa:

* Interpretación de intención
* Generación de SQL
* Ejecución de consultas
* Visualización
* Exportación de resultados

---

## Funcionalidades

* 🔍 Consultas en lenguaje natural
* 🧾 Traducción automática a SQL
* 📊 Visualización de resultados (gráficos)
* 📁 Exportación a CSV o Excel
* 🔁 Interacción iterativa con el usuario
* 🛡️ Validación de consultas SQL (guardrails)

---

## Arquitectura

El flujo del agente es el siguiente:

1. El usuario realiza una pregunta en lenguaje natural
2. El agente detecta la intención (tabla, gráfico, archivo, etc.)
3. Se genera una consulta SQL basada en el esquema
4. Se valida la consulta (seguridad)
5. Se ejecuta contra la base de datos
6. Se procesan los resultados
7. Se responde en el formato solicitado

---

## Estructura del proyecto

```bash
sales-agent/
│
├── agents/            # Lógica del agente
├── services/          # Funciones auxiliares (SQL, gráficos, exportación)
├── data/              # Datos de entrada (CSV)
├── db/                # Base de datos SQLite
├── main.py            # Punto de entrada
├── requirements.txt   # Dependencias
└── README.md
```

---

## Base de datos

Tabla: `ventas`

Columnas:

* `id`
* `vendedor`
* `sede`
* `producto`
* `cantidad`
* `precio`
* `fecha`

---

## Instalación

```bash
git clone https://github.com/sebastian-munoz-blend/sales-agent.git
cd sales-agent

pip install -r requirements.txt
```

---

## Ejecución

```bash
python main.py
```

El agente iniciará en consola y podrás hacer preguntas como:

```text
Top 5 productos más vendidos en Medellín
```

```text
Vendedor con más ventas en Bogotá
```

```text
Guarda las ventas por vendedor en un archivo CSV
```

---

## Ejemplos de uso

### 🔹 Consulta

> Top 5 productos más vendidos en Medellín

### 🔹 SQL generado

```sql
SELECT producto, SUM(cantidad) AS total_vendido
FROM ventas
WHERE sede = 'Medellín'
GROUP BY producto
ORDER BY total_vendido DESC
LIMIT 5;
```

### 🔹 Resultado

* Tabla con resultados
* Gráfico de barras

---

### 🔹 Consulta

> Guarda las ventas por vendedor en un archivo CSV

### 🔹 Resultado

* Archivo generado: `resultado_ventas.csv`

---

## Tecnologías utilizadas

* Python
* SQLite
* Pandas
* Matplotlib
* LangChain / LangGraph (conceptualmente)
* Modelos de lenguaje (LLM)

---

## Seguridad

El sistema incluye validaciones para evitar ejecución de consultas peligrosas:

* Bloqueo de operaciones como `DELETE`, `DROP`, `UPDATE`
* Restricción al uso de la tabla `ventas`
* Validación previa a la ejecución

---

## Consideraciones de diseño

* Arquitectura modular para facilitar escalabilidad
* Separación clara entre lógica del agente y servicios
* Uso de LLM para interpretar intención (no reglas fijas)
* Preparado para integración con conectores MCP

---

## Posibles mejoras

* Integración real con MCP (Multi-Connector Protocol)
* API REST o interfaz web (Streamlit)
* Soporte para múltiples bases de datos
* Dashboard interactivo
* Despliegue en la nube (AWS / HuggingFace)

---

## Autor

**Sebastián Muñoz**
Proyecto desarrollado como ejercicio práctico de Agentic AI

---
