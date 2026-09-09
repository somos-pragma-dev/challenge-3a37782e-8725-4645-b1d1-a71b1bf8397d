# Diseño y Desarrollo de una API REST en Banca

El objetivo de este reto es desarrollar una API REST para un sistema de gestión de préstamos bancarios. La API debe manejar la creación, lectura, actualización y eliminación de préstamos. Los préstamos tienen atributos como monto, tasa de interés, duración y estado. La API debe asegurar la integridad de los datos y manejar errores de forma apropiada. Los préstamos se almacenarán en una base de datos relacional.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST con FastAPI y SQLAlchemy |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de la Estructura de Datos

**Objetivo:** Definir los modelos de datos para préstamos y clientes.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los atributos necesarios para los modelos de préstamos y clientes.
- Establecer relaciones entre los modelos.

**Entregable:** Modelos de datos definidos y relaciones establecidas.

<details>
<summary>Pistas de conocimiento</summary>

- Considerar atributos como monto, tasa de interés, duración y estado para los préstamos.
- Incluir atributos como nombre, edad y historial crediticio para los clientes.

</details>

### Fase 2: Implementación de las Rutas de la API

**Objetivo:** Implementar las rutas CRUD para préstamos y clientes.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear rutas para crear, leer, actualizar y eliminar préstamos y clientes.
- Asegurar que las rutas manejen errores de forma apropiada.

**Entregable:** Rutas CRUD implementadas y funcionando.

<details>
<summary>Pistas de conocimiento</summary>

- Utilizar métodos HTTP adecuados para cada operación (POST para crear, GET para leer, PUT para actualizar, DELETE para eliminar).
- Manejar errores como préstamos no encontrados o datos inválidos.

</details>

### Fase 3: Integración con la Base de Datos

**Objetivo:** Integrar la API con una base de datos relacional.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Configurar la conexión a la base de datos.
- Implementar la lógica para persistir y recuperar datos de la base de datos.

**Entregable:** API integrada con la base de datos y funcionando.

<details>
<summary>Pistas de conocimiento</summary>

- Utilizar SQLAlchemy para interactuar con la base de datos.
- Asegurar que los datos se guarden y recuperen correctamente.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué son los modelos de datos y por qué son importantes en este reto?
- **paraQueSirve**: ¿Para qué sirven las rutas CRUD en una API REST?
- **comoSeUsa**: ¿Cómo se usa SQLAlchemy para interactuar con una base de datos en este contexto?
- **erroresComunes**: ¿Cuáles son los errores comunes que puedes encontrar al implementar una API REST y cómo los manejarías?

## Criterios de Evaluacion

- Definición correcta de los modelos de datos para préstamos y clientes.
- Implementación de las rutas CRUD para préstamos y clientes.
- Integración exitosa de la API con la base de datos.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
