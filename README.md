# 🇪🇸 EspañolPro — Preparación DELE C1/C2

Aplicación interactiva para la preparación del examen DELE C1/C2 del Instituto Cervantes.

🔗 **App en producción:** [espanol-pro.streamlit.app](https://espanol-pro.streamlit.app)

## ¿Qué incluye?

- 📗 **Verbos + Preposición** — 162 verbos con 11 preposiciones y repetición espaciada
- 🔗 **Conectores del discurso** — 50 conectores con función, matiz y registro C1/C2
- 🔀 **Subjuntivo vs Indicativo** — 25 contextos reales de nivel C1
- ⚙️ **Perífrasis verbales** — 19 perífrasis con tarjetas y ejercicios de producción
- 🔴 **Ser vs Estar** — 22 contextos con los errores más frecuentes de anglohablantes
- 🔤 **Pronombres** — OD, OI, reflexivos, combinaciones y posición
- 🇬🇧 **Errores de anglohablantes** — 14 errores frecuentes con explicación y corrección
- 📚 **Comprensión lectora** — 10 textos originales en 3 formatos reales del DELE C1
- 📝 **Vocabulario temático** — 180 palabras en 6 temas clave del examen

## Niveles

Todos los ejercicios están etiquetados por nivel **B2 / C1 / C2** y pueden filtrarse desde el sidebar.

## Tecnología

- Python + Streamlit
- Arquitectura modular: `data/`, `modules/`, `core/`, `ui/`
- Desplegado en Streamlit Cloud

## Ejecutar localmente

```bash
git clone https://github.com/1lauraog15-cloud/cata-espanol-app.git
cd cata-espanol-app/cata-espanol-app
pip install -r requirements.txt
streamlit run app.py
```

## Estructura del proyecto

```
cata-espanol-app/
├── app.py                  # Punto de entrada — 38 líneas
├── data/                   # Datos separados por módulo
│   ├── verbos.py
│   ├── conectores.py
│   ├── gramatica.py
│   ├── vocabulario.py
│   └── diagnostico.py
├── modules/                # UI de cada módulo
├── core/                   # Estado, helpers, config, estilos
└── ui/                     # Sidebar y home screen
```
