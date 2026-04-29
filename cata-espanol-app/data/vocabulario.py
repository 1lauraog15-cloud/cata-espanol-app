from typing import Dict, List

VOCABULARIO: Dict[str, Dict] = {
    "medio_ambiente": {
        "titulo": "🌍 Medio ambiente",
        "descripcion": "Léxico esencial sobre cambio climático, sostenibilidad y ecología. Frecuente en el DELE C1.",
        "palabras": [
            {"palabra": "la huella ecológica", "categoria": "sustantivo", "definicion": "Impacto ambiental que genera una persona, empresa o actividad", "ejemplo": "La huella ecológica de los países desarrollados supera con creces la capacidad regenerativa del planeta.", "nivel": "C1"},
            {"palabra": "la biodiversidad", "categoria": "sustantivo", "definicion": "Variedad de especies vivas en un ecosistema o en la Tierra", "ejemplo": "La pérdida de biodiversidad es una de las consecuencias más graves de la deforestación masiva.", "nivel": "C1"},
            {"palabra": "el calentamiento global", "categoria": "sustantivo", "definicion": "Aumento progresivo de la temperatura media de la Tierra", "ejemplo": "El calentamiento global está acelerando la fusión de los glaciares polares.", "nivel": "B2"},
            {"palabra": "las emisiones de CO₂", "categoria": "sustantivo", "definicion": "Cantidad de dióxido de carbono liberado a la atmósfera", "ejemplo": "Reducir las emisiones de CO₂ es el principal objetivo del Acuerdo de París.", "nivel": "C1"},
            {"palabra": "la deforestación", "categoria": "sustantivo", "definicion": "Destrucción masiva de bosques y selvas", "ejemplo": "La deforestación del Amazonas amenaza el equilibrio climático de todo el planeta.", "nivel": "B2"},
            {"palabra": "sostenible", "categoria": "adjetivo", "definicion": "Que puede mantenerse sin agotar los recursos naturales", "ejemplo": "Necesitamos un modelo económico sostenible que no comprometa a las generaciones futuras.", "nivel": "B2"},
            {"palabra": "renovable", "categoria": "adjetivo", "definicion": "Que se puede regenerar naturalmente o es inagotable", "ejemplo": "La energía renovable representa ya el 40% de la electricidad consumida en España.", "nivel": "B2"},
            {"palabra": "el reciclaje", "categoria": "sustantivo", "definicion": "Proceso de transformar residuos en nuevos materiales", "ejemplo": "El reciclaje de plásticos sigue siendo insuficiente a nivel global.", "nivel": "B2"},
            {"palabra": "la contaminación", "categoria": "sustantivo", "definicion": "Presencia de sustancias dañinas en el medio ambiente", "ejemplo": "La contaminación del aire en las grandes ciudades causa miles de muertes prematuras al año.", "nivel": "B2"},
            {"palabra": "el efecto invernadero", "categoria": "sustantivo", "definicion": "Retención del calor solar por los gases atmosféricos", "ejemplo": "El efecto invernadero es un fenómeno natural que se ha intensificado por la actividad humana.", "nivel": "B2"},
            {"palabra": "la sequía", "categoria": "sustantivo", "definicion": "Período prolongado de escasez de lluvia", "ejemplo": "Las sequías cada vez más frecuentes amenazan la seguridad alimentaria de millones de personas.", "nivel": "B2"},
            {"palabra": "la deuda ecológica", "categoria": "sustantivo", "definicion": "Deterioro ambiental acumulado que las generaciones futuras deberán asumir", "ejemplo": "El concepto de deuda ecológica pone en cuestión el modelo de crecimiento ilimitado.", "nivel": "C1"},
            {"palabra": "agotar", "categoria": "verbo", "definicion": "Consumir completamente un recurso hasta acabar con él", "ejemplo": "Si seguimos agotando los acuíferos a este ritmo, el agua potable será un bien escaso.", "nivel": "B2"},
            {"palabra": "mitigar", "categoria": "verbo", "definicion": "Reducir o suavizar los efectos negativos de algo", "ejemplo": "Las medidas adoptadas son insuficientes para mitigar el impacto del cambio climático.", "nivel": "C1"},
            {"palabra": "deteriorar", "categoria": "verbo", "definicion": "Empeorar progresivamente la calidad o el estado de algo", "ejemplo": "La actividad industrial ha deteriorado gravemente los ecosistemas costeros.", "nivel": "C1"},
            {"palabra": "el ecosistema", "categoria": "sustantivo", "definicion": "Conjunto de seres vivos y su entorno natural", "ejemplo": "Los ecosistemas marinos están bajo una presión sin precedentes.", "nivel": "B2"},
            {"palabra": "la capa de ozono", "categoria": "sustantivo", "definicion": "Capa de la atmósfera que protege la Tierra de la radiación ultravioleta", "ejemplo": "La recuperación de la capa de ozono es uno de los pocos éxitos de la cooperación medioambiental internacional.", "nivel": "C1"},
            {"palabra": "los residuos", "categoria": "sustantivo", "definicion": "Materiales desechados tras un proceso de producción o consumo", "ejemplo": "La gestión de los residuos electrónicos es uno de los retos medioambientales más urgentes.", "nivel": "B2"},
            {"palabra": "la energía solar", "categoria": "sustantivo", "definicion": "Energía obtenida a partir de la radiación del sol", "ejemplo": "La energía solar ha reducido su coste un 90% en la última década.", "nivel": "B2"},
            {"palabra": "el vertido", "categoria": "sustantivo", "definicion": "Derramamiento de sustancias contaminantes en el medio natural", "ejemplo": "El vertido de petróleo causó un daño irreparable en el ecosistema marino.", "nivel": "C1"},
            {"palabra": "la reforestación", "categoria": "sustantivo", "definicion": "Plantación de árboles en zonas que han sufrido deforestación", "ejemplo": "Los programas de reforestación son esenciales para recuperar los suelos degradados.", "nivel": "C1"},
            {"palabra": "nocivo", "categoria": "adjetivo", "definicion": "Que causa daño o perjuicio a la salud o al medio ambiente", "ejemplo": "Los gases nocivos emitidos por las industrias afectan directamente a la calidad del aire.", "nivel": "C1"},
            {"palabra": "el cambio climático", "categoria": "sustantivo", "definicion": "Alteración del clima a largo plazo causada por la actividad humana", "ejemplo": "El cambio climático ya no es una amenaza futura — es una realidad presente.", "nivel": "B2"},
            {"palabra": "la huella de carbono", "categoria": "sustantivo", "definicion": "Cantidad total de gases de efecto invernadero emitidos por una actividad", "ejemplo": "Calcular la huella de carbono de un producto permite tomar decisiones de consumo más responsables.", "nivel": "C1"},
            {"palabra": "el impacto ambiental", "categoria": "sustantivo", "definicion": "Efecto que una actividad humana produce en el medio ambiente", "ejemplo": "Todo proyecto de construcción debe ir acompañado de un estudio de impacto ambiental.", "nivel": "C1"},
            {"palabra": "la escasez", "categoria": "sustantivo", "definicion": "Insuficiencia de un recurso respecto a la demanda", "ejemplo": "La escasez de agua potable afecta ya a más de dos mil millones de personas.", "nivel": "C1"},
            {"palabra": "comprometerse", "categoria": "verbo", "definicion": "Adquirir un compromiso o responsabilidad con algo", "ejemplo": "Los países firmantes se comprometieron a reducir sus emisiones en un 45% antes de 2030.", "nivel": "C1"},
            {"palabra": "devastar", "categoria": "verbo", "definicion": "Destruir o arruinar completamente un lugar", "ejemplo": "Los incendios forestales devastaron miles de hectáreas en el sur de Europa.", "nivel": "C1"},
            {"palabra": "la concienciación", "categoria": "sustantivo", "definicion": "Proceso de hacer que alguien tome conciencia de algo importante", "ejemplo": "La concienciación ciudadana es imprescindible para lograr cambios reales en los hábitos de consumo.", "nivel": "C1"},
            {"palabra": "el desarrollo sostenible", "categoria": "sustantivo", "definicion": "Desarrollo que satisface las necesidades presentes sin comprometer las futuras", "ejemplo": "El desarrollo sostenible es el eje central de la Agenda 2030 de Naciones Unidas.", "nivel": "C1"},
        ]
    }
}
