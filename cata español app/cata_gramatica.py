import random
from typing import Dict, List
import streamlit as st

# ============================================================
# CATA — Gramática C1 · DELE Cervantes
# Módulos: Subjuntivo, Perífrasis, Estilo indirecto,
#          Pronombres, Errores anglohablantes, Comprensión lectora
# Ejecutar: streamlit run cata_gramatica.py
# Requisitos: pip install streamlit
# ============================================================

# ─────────────────────────────────────────────
#  DATOS — SUBJUNTIVO VS INDICATIVO
# ─────────────────────────────────────────────

SUBJUNTIVO: List[Dict] = [
    # Oraciones subordinadas sustantivas
    {
        "frase": "Es importante que todos los miembros del equipo ___ (estar) de acuerdo antes de presentar la propuesta.",
        "respuesta": "estén",
        "tipo": "Expresiones impersonales + que",
        "explicacion": "Las expresiones impersonales de valoración (es importante, es necesario, es fundamental...) exigen subjuntivo en la subordinada.",
        "nivel": "C1",
        "trampa": "No confundir con 'es evidente que + indicativo' (afirma un hecho).",
    },
    {
        "frase": "Me sorprende que todavía no ___ (haberse) publicado los resultados del estudio.",
        "respuesta": "se hayan publicado",
        "tipo": "Verbos de emoción + que",
        "explicacion": "Verbos de sentimiento (sorprender, alegrar, molestar, extrañar...) rigen subjuntivo cuando el sujeto de la subordinada es distinto al principal.",
        "nivel": "C1",
        "trampa": "El perfecto de subjuntivo (hayan publicado) expresa una acción anterior al momento presente.",
    },
    {
        "frase": "No creo que la situación ___ (mejorar) sin una intervención decidida de las autoridades.",
        "respuesta": "mejore",
        "tipo": "Verbos de opinión negados",
        "explicacion": "Creer, pensar, opinar, considerar + negación → subjuntivo. Sin negación → indicativo ('Creo que mejorará').",
        "nivel": "C1",
        "trampa": "'Creo que mejorará' (indicativo) vs 'No creo que mejore' (subjuntivo).",
    },
    {
        "frase": "Aunque ___ (llover) mañana, el acto se celebrará al aire libre según lo previsto.",
        "respuesta": "llueva",
        "tipo": "Aunque + subjuntivo (concesión hipotética)",
        "explicacion": "'Aunque' + subjuntivo: la condición es hipotética o no confirmada. 'Aunque' + indicativo: la condición es un hecho conocido ('aunque llueve, salgo').",
        "nivel": "C1",
        "trampa": "Si se sabe que lloverá (hecho), se usa indicativo. Si es hipótesis, subjuntivo.",
    },
    {
        "frase": "Buscan un candidato que ___ (tener) experiencia previa en gestión de equipos internacionales.",
        "respuesta": "tenga",
        "tipo": "Antecedente indefinido o inexistente",
        "explicacion": "Cuando el antecedente es indefinido (buscan alguien que...) o negado (no hay nadie que...), la relativa lleva subjuntivo.",
        "nivel": "C1",
        "trampa": "'Tengo un candidato que tiene experiencia' (indicativo, antecedente conocido) vs 'busco uno que tenga' (subjuntivo, indefinido).",
    },
    {
        "frase": "Te lo digo para que ___ (poder) prepararte con tiempo suficiente.",
        "respuesta": "puedas",
        "tipo": "Conjunciones de finalidad",
        "explicacion": "Para que, a fin de que, con el objetivo de que → siempre subjuntivo, porque expresan una finalidad (algo que aún no ha ocurrido).",
        "nivel": "B2",
        "trampa": "No confundir con 'para + infinitivo' cuando el sujeto es el mismo: 'Te lo digo para poder prepararte'.",
    },
    {
        "frase": "Cuando ___ (terminar) de revisar el informe, envíamelo por correo electrónico.",
        "respuesta": "termines",
        "tipo": "Cuando + subjuntivo (futuro)",
        "explicacion": "'Cuando' + subjuntivo: acción futura o hipotética. 'Cuando' + indicativo: acción habitual o pasada ('cuando termino, siempre me relajo').",
        "nivel": "B2",
        "trampa": "'Cuando llegué' (pasado, indicativo) vs 'cuando llegues' (futuro, subjuntivo).",
    },
    {
        "frase": "Si ___ (haber sabido) lo que iba a pasar, nunca habría firmado ese contrato.",
        "respuesta": "hubiera sabido",
        "tipo": "Condicional irreal de pasado",
        "explicacion": "Estructura: Si + pluscuamperfecto de subjuntivo (hubiera/hubiese + participio) → condicional compuesto (habría + participio). Expresa condición imposible en el pasado.",
        "nivel": "C1",
        "trampa": "Nunca se usa 'si + condicional': *si habría sabido* es incorrecto.",
    },
    {
        "frase": "No hay ningún experto que ___ (poder) predecir con certeza lo que ocurrirá.",
        "respuesta": "pueda",
        "tipo": "Antecedente negado",
        "explicacion": "Con antecedente negado (ningún, nadie, nada...), la oración de relativo siempre lleva subjuntivo.",
        "nivel": "C1",
        "trampa": "Si el antecedente existe y es conocido, se usa indicativo: 'Hay expertos que pueden predecirlo'.",
    },
    {
        "frase": "Ojalá ___ (llegar) a un acuerdo antes de que expire el plazo establecido.",
        "respuesta": "lleguen",
        "tipo": "Ojalá + subjuntivo",
        "explicacion": "'Ojalá' siempre rige subjuntivo. Presente de subjuntivo para deseos realizables; imperfecto para deseos poco probables; pluscuamperfecto para deseos del pasado.",
        "nivel": "B2",
        "trampa": "*Ojalá llegarán* es incorrecto en español normativo.",
    },
    {
        "frase": "Le pidió que ___ (guardar) la información con absoluta discreción.",
        "respuesta": "guardara",
        "tipo": "Verbo de petición en pasado",
        "explicacion": "Verbos de influencia (pedir, rogar, ordenar, recomendar...) en pasado → imperfecto de subjuntivo en la subordinada.",
        "nivel": "C1",
        "trampa": "Si el verbo principal está en presente, se usa presente de subjuntivo: 'Le pide que guarde'.",
    },
    {
        "frase": "Por mucho que ___ (esforzarse), no consiguió superar el obstáculo que tenía delante.",
        "respuesta": "se esforzara",
        "tipo": "Concesivas con por + mucho/más + que",
        "explicacion": "'Por mucho que', 'por más que', 'por poco que' + subjuntivo expresan una concesión de grado. Si el contexto es pasado, imperfecto de subjuntivo.",
        "nivel": "C1",
        "trampa": "Si el contexto es presente o futuro: 'por mucho que se esfuerce, no lo conseguirá'.",
    },
    {
        "frase": "Habla como si ___ (conocer) personalmente a todos los miembros del consejo directivo.",
        "respuesta": "conociera",
        "tipo": "Como si + imperfecto de subjuntivo",
        "explicacion": "'Como si' siempre lleva imperfecto o pluscuamperfecto de subjuntivo porque expresa una comparación irreal o ficticia.",
        "nivel": "C1",
        "trampa": "*Como si conoce* es incorrecto. Siempre subjuntivo después de 'como si'.",
    },
    {
        "frase": "En cuanto ___ (recibir) la notificación oficial, procederemos a tramitar los permisos.",
        "respuesta": "recibamos",
        "tipo": "Conjunciones temporales + futuro",
        "explicacion": "En cuanto, tan pronto como, nada más que, una vez que + subjuntivo cuando la acción es futura.",
        "nivel": "C1",
        "trampa": "'En cuanto llegué' (pasado, indicativo) vs 'en cuanto llegues' (futuro, subjuntivo).",
    },
    {
        "frase": "Me alegra que finalmente ___ (decidirse) a dar ese paso tan importante.",
        "respuesta": "te hayas decidido",
        "tipo": "Perfecto de subjuntivo",
        "explicacion": "Cuando la emoción es presente pero la acción ya ha ocurrido, se usa el perfecto de subjuntivo (haya/hayas/haya + participio).",
        "nivel": "C1",
        "trampa": "El perfecto de subjuntivo sitúa la acción antes del momento de habla, aunque la emoción sea presente.",
    },
]

# ─────────────────────────────────────────────
#  DATOS — PERÍFRASIS VERBALES
# ─────────────────────────────────────────────

PERIFRASIS: List[Dict] = [
    {
        "perifrasis": "llevar + gerundio",
        "significado": "Expresa la duración acumulada de una acción que sigue en curso en el momento de referencia.",
        "ejemplos": [
            "Llevo tres horas esperando sin que nadie me atienda.",
            "Cuando llegaste, llevaba trabajando toda la tarde.",
        ],
        "trampa": "El complemento de tiempo responde a '¿cuánto tiempo llevas...?'. No confundir con 'llevar + participio' (= haber conseguido acumular).",
        "ejercicio": "Lleva ___ (trabajar) en esa empresa más de diez años sin que le hayan ofrecido una promoción.",
        "respuesta": "trabajando",
        "nivel": "C1",
    },
    {
        "perifrasis": "seguir + gerundio",
        "significado": "Indica que una acción continúa sin interrupción en el momento de referencia.",
        "ejemplos": [
            "Siguen debatiendo el mismo punto desde hace horas.",
            "Aunque le aconsejaron que parara, siguió trabajando hasta el amanecer.",
        ],
        "trampa": "No confundir con 'continuar + gerundio', que es sinónimo pero de registro más formal.",
        "ejercicio": "A pesar de las advertencias, ___ (cometer) los mismos errores una y otra vez.",
        "respuesta": "sigue cometiendo",
        "nivel": "B2",
    },
    {
        "perifrasis": "dejar de + infinitivo",
        "significado": "Indica la interrupción definitiva o temporal de una acción que se venía realizando.",
        "ejemplos": [
            "Dejó de fumar hace tres años después de varios intentos fallidos.",
            "No dejes de informarme si hay alguna novedad importante.",
        ],
        "trampa": "Con negación ('no dejes de + infinitivo') adquiere un valor de recomendación o mandato: 'no dejes de verla' = asegúrate de verla.",
        "ejercicio": "___ (hablar) con ella desde que tuvieron aquella discusión tan tensa.",
        "respuesta": "Ha dejado de hablar / Dejó de hablar",
        "nivel": "B2",
    },
    {
        "perifrasis": "ponerse a + infinitivo",
        "significado": "Expresa el inicio brusco o inesperado de una acción.",
        "ejemplos": [
            "Sin previo aviso, se puso a llover con una intensidad tremenda.",
            "En cuanto se sentó, se puso a leer sin saludar a nadie.",
        ],
        "trampa": "Indica inicio súbito, no planificado. Contrasta con 'empezar a + infinitivo', que puede ser más neutro y planificado.",
        "ejercicio": "Nada más recibir la noticia, ___ (llorar) sin poder contenerse.",
        "respuesta": "se puso a llorar",
        "nivel": "B2",
    },
    {
        "perifrasis": "volver a + infinitivo",
        "significado": "Indica la repetición de una acción que ya se había realizado antes.",
        "ejemplos": [
            "Volvió a cometer el mismo error que le habían señalado en la revisión anterior.",
            "No quiero volver a pasar por una situación tan incómoda.",
        ],
        "trampa": "Equivale a 'otra vez + verbo'. En negativo, expresa la voluntad de no repetir: 'no quiero volver a verle' = no quiero verle nunca más.",
        "ejercicio": "Tras años de silencio, ___ (publicar) una novela que ha sorprendido a todos.",
        "respuesta": "ha vuelto a publicar",
        "nivel": "B2",
    },
    {
        "perifrasis": "acabar de + infinitivo",
        "significado": "Indica que una acción se ha completado en un momento muy reciente.",
        "ejemplos": [
            "Acabo de hablar con el director y me ha confirmado los cambios.",
            "Cuando llegué, acababan de cerrar la puerta.",
        ],
        "trampa": "Solo se usa en presente (acción recién hecha) e imperfecto (acción recién terminada antes de otra). No se usa en futuro ni con otros tiempos.",
        "ejercicio": "___ (confirmar) que el evento se celebrará tal y como estaba previsto.",
        "respuesta": "Acaban de confirmar",
        "nivel": "B2",
    },
    {
        "perifrasis": "acabar por + infinitivo",
        "significado": "Indica que, tras un proceso o resistencia, se llega finalmente a una conclusión o acción.",
        "ejemplos": [
            "Aunque al principio se resistía, acabó por aceptar las condiciones.",
            "Después de tanto debatirlo, acabamos por no tomar ninguna decisión.",
        ],
        "trampa": "Sinónimo de 'terminar por + infinitivo'. No confundir con 'acabar de + infinitivo' (reciente) ni 'acabar + gerundio' (resultado gradual).",
        "ejercicio": "Tras meses de negociaciones, ___ (firmar) un acuerdo que nadie esperaba.",
        "respuesta": "acabaron por firmar",
        "nivel": "C1",
    },
    {
        "perifrasis": "ir a + infinitivo",
        "significado": "Expresa intención, plan o predicción inmediata sobre el futuro.",
        "ejemplos": [
            "Vamos a revisar todos los puntos antes de tomar una decisión definitiva.",
            "Con esa actitud, va a perder la confianza de todo el equipo.",
        ],
        "trampa": "En imperfecto, expresa una acción que iba a ocurrir pero que puede haberse truncado: 'iba a llamarte pero se me fue de la cabeza'.",
        "ejercicio": "Según las previsiones, ___ (producirse) un cambio significativo en el sector.",
        "respuesta": "va a producirse / se va a producir",
        "nivel": "B2",
    },
    {
        "perifrasis": "tener que + infinitivo",
        "significado": "Expresa obligación o necesidad, ya sea impuesta externamente o deducida por el hablante.",
        "ejemplos": [
            "Tienes que entregar el formulario antes del viernes sin falta.",
            "Tiene que haber algún malentendido; esto no puede ser correcto.",
        ],
        "trampa": "En el segundo uso (deducción), equivale a 'deber de': 'tiene que haber un error' = deduzco que hay un error. 'Deber de' es solo para deducción.",
        "ejercicio": "Con tan pocos recursos, ___ (priorizar) muy bien cada gasto.",
        "respuesta": "tendrán que priorizar / tienen que priorizar",
        "nivel": "B2",
    },
    {
        "perifrasis": "deber + infinitivo",
        "significado": "Expresa obligación moral o deducción lógica (sin 'de': obligación; con 'de': deducción).",
        "ejemplos": [
            "Debes respetar las normas establecidas por la organización.",
            "Debe de ser muy tarde; no hay nadie en las calles.",
        ],
        "trampa": "'Deber + infinitivo' = obligación. 'Deber de + infinitivo' = deducción o probabilidad. En el habla real, esta distinción se está perdiendo, pero el DELE la exige.",
        "ejercicio": "A juzgar por su cara, ___ (estar) agotada después del viaje.",
        "respuesta": "debe de estar",
        "nivel": "C1",
    },
    {
        "perifrasis": "andar + gerundio",
        "significado": "Indica una acción habitual, repetida o persistente, a menudo con cierto matiz negativo o de búsqueda.",
        "ejemplos": [
            "Anda buscando trabajo desde que lo despidieron el año pasado.",
            "No me gusta que anden comentando mis asuntos a mis espaldas.",
        ],
        "trampa": "Similar a 'estar + gerundio' pero con más matiz de dispersión, repetición o actividad continua y difusa. Registro más coloquial.",
        "ejercicio": "Últimamente ___ (quejarse) de todo sin proponer ninguna alternativa.",
        "respuesta": "anda quejándose",
        "nivel": "C1",
    },
    {
        "perifrasis": "quedar en + infinitivo",
        "significado": "Expresa un acuerdo o compromiso adoptado entre dos o más personas.",
        "ejemplos": [
            "Quedamos en llamarnos el lunes para confirmar los detalles finales.",
            "¿No habíais quedado en no comentar nada hasta que fuera oficial?",
        ],
        "trampa": "No confundir con 'quedar + gerundio' (resultado: 'quedó demostrado') ni 'quedar con' (citarse con alguien).",
        "ejercicio": "Según lo acordado, habíamos ___ (vernos) aquí a las seis en punto.",
        "respuesta": "quedado en vernos",
        "nivel": "C1",
    },
]

# ─────────────────────────────────────────────
#  DATOS — ESTILO INDIRECTO
# ─────────────────────────────────────────────

ESTILO_INDIRECTO: List[Dict] = [
    {
        "directo": "«Estoy muy cansada y no puedo seguir trabajando»",
        "verbo_intro": "dijo que",
        "respuesta": "estaba muy cansada y no podía seguir trabajando",
        "cambios": "Presente → imperfecto. Poder (presente) → podía (imperfecto).",
        "nivel": "B2",
        "explicacion": "Cuando el verbo introductor está en pasado, los tiempos del estilo directo retroceden: presente → imperfecto; futuro → condicional; pretérito perfecto → pluscuamperfecto.",
    },
    {
        "directo": "«Lo haré en cuanto pueda»",
        "verbo_intro": "prometió que",
        "respuesta": "lo haría en cuanto pudiera",
        "cambios": "Futuro (haré) → condicional (haría). Pueda (pres. subj.) → pudiera (imp. subj.).",
        "nivel": "C1",
        "explicacion": "El futuro en estilo directo se convierte en condicional en estilo indirecto con verbo introductor en pasado.",
    },
    {
        "directo": "«¿Has terminado el informe que te pedí?»",
        "verbo_intro": "le preguntó si",
        "respuesta": "había terminado el informe que le había pedido",
        "cambios": "Pretérito perfecto (has terminado) → pluscuamperfecto (había terminado).",
        "nivel": "C1",
        "explicacion": "El pretérito perfecto en estilo directo se convierte en pluscuamperfecto en estilo indirecto. Las preguntas totales (sí/no) introducen con 'si'.",
    },
    {
        "directo": "«No comentes nada de esto con nadie»",
        "verbo_intro": "le pidió que",
        "respuesta": "no comentara nada de eso con nadie",
        "cambios": "Imperativo → imperfecto de subjuntivo. 'esto' → 'eso' (deixis).",
        "nivel": "C1",
        "explicacion": "Los imperativos y las peticiones en estilo directo se transforman con verbo + que + imperfecto de subjuntivo en estilo indirecto (verbo en pasado).",
    },
    {
        "directo": "«Mañana tendremos los resultados»",
        "verbo_intro": "anunció que",
        "respuesta": "al día siguiente tendrían los resultados",
        "cambios": "Futuro (tendremos) → condicional (tendrían). 'Mañana' → 'al día siguiente'.",
        "nivel": "C1",
        "explicacion": "Los adverbios de tiempo también cambian: mañana → al día siguiente; hoy → ese día; ayer → el día anterior; aquí → allí.",
    },
    {
        "directo": "«Llevamos tres semanas esperando una respuesta»",
        "verbo_intro": "nos explicó que",
        "respuesta": "llevaban tres semanas esperando una respuesta",
        "cambios": "Llevamos (pres.) → llevaban (imp.). La perífrasis se mantiene.",
        "nivel": "C1",
        "explicacion": "Las perífrasis verbales también cambian sus tiempos: 'llevar + gerundio' en presente → en imperfecto en estilo indirecto.",
    },
    {
        "directo": "«¿Cuándo te dijeron que empezaría el proyecto?»",
        "verbo_intro": "me preguntó",
        "respuesta": "cuándo me habían dicho que empezaría el proyecto",
        "cambios": "Dijeron (indefinido) → habían dicho (pluscuamperfecto). 'Empezaría' no cambia (ya estaba en condicional).",
        "nivel": "C2",
        "explicacion": "El indefinido en estilo directo → pluscuamperfecto en indirecto. Las preguntas parciales (con interrogativo) se introducen sin 'si'.",
    },
    {
        "directo": "«Espero que todo haya salido bien»",
        "verbo_intro": "dijo que",
        "respuesta": "esperaba que todo hubiera salido bien",
        "cambios": "Espero (pres.) → esperaba (imp.). Haya salido (perf. subj.) → hubiera salido (plusc. subj.).",
        "nivel": "C2",
        "explicacion": "El perfecto de subjuntivo en estilo directo se convierte en pluscuamperfecto de subjuntivo en estilo indirecto cuando el verbo introductor está en pasado.",
    },
    {
        "directo": "«Venid a cenar el viernes si podéis»",
        "verbo_intro": "nos invitó a",
        "respuesta": "ir a cenar el viernes si podíamos",
        "cambios": "Imperativo plural → infinitivo (con verbo de invitación). Podéis → podíamos.",
        "nivel": "C1",
        "explicacion": "Con verbos de invitación, ruego o mandato, el imperativo puede transformarse en infinitivo: 'les invitó a ir', 'les mandó salir'.",
    },
    {
        "directo": "«Aquí nunca pasa nada interesante»",
        "verbo_intro": "se quejó de que",
        "respuesta": "allí nunca pasaba nada interesante",
        "cambios": "'Aquí' → 'allí'. Pasa (pres.) → pasaba (imp.).",
        "nivel": "C1",
        "explicacion": "Los demostrativos y adverbios de lugar también cambian: aquí/acá → allí/allá; este/ese → aquel.",
    },
]

# ─────────────────────────────────────────────
#  DATOS — PRONOMBRES OD/OI/REFLEXIVOS
# ─────────────────────────────────────────────

PRONOMBRES: List[Dict] = [
    {
        "tipo": "Combinación OI + OD",
        "pregunta": "¿Cuál es la forma correcta?\n\n«Le di el libro a María» → con pronombres: ___",
        "opciones": ["Le lo di", "Se lo di", "Lo le di", "Le di lo"],
        "respuesta": "Se lo di",
        "explicacion": "Cuando OI (le/les) va seguido de OD (lo/la/los/las), el OI se convierte en 'se'. Nunca se dice *le lo, le la, les lo...*",
        "nivel": "B2",
    },
    {
        "tipo": "Posición con infinitivo",
        "pregunta": "¿Cuál es la forma correcta?\n\n«Quiero decir la verdad a ti» → con pronombres: ___",
        "opciones": ["Te quiero decirla", "Quiero decírtela", "Las dos son correctas", "Quiero la decirte"],
        "respuesta": "Las dos son correctas",
        "explicacion": "Con perífrasis verbales y verbos + infinitivo, los pronombres pueden ir delante del verbo conjugado O enclíticos al infinitivo: 'te lo quiero decir' = 'quiero decírtelo'.",
        "nivel": "B2",
    },
    {
        "tipo": "Leísmo",
        "pregunta": "¿Cuál es la opción normativa según la RAE?\n\n«Vi a tu hermano ayer»",
        "opciones": ["Le vi ayer", "Lo vi ayer", "Las dos son aceptadas", "Depende del país"],
        "respuesta": "Las dos son aceptadas",
        "explicacion": "El leísmo de persona masculina singular está aceptado por la RAE como uso correcto. 'Le vi' (persona masculina) es válido. 'Lo vi' también. El leísmo de cosa (*le compré* refiriéndose a un objeto) no está aceptado.",
        "nivel": "C1",
    },
    {
        "tipo": "Posición con gerundio",
        "pregunta": "Elige la opción correcta:\n\n«Está explicando el problema a los estudiantes»",
        "opciones": ["Se los está explicando", "Está explicándoselo", "Las dos son correctas", "Les lo está explicando"],
        "respuesta": "Las dos son correctas",
        "explicacion": "Con estar + gerundio, los pronombres van delante de 'está' O enclíticos al gerundio (con tilde si es necesario): 'se lo está explicando' = 'está explicándoselo'.",
        "nivel": "C1",
    },
    {
        "tipo": "Pronombre reflexivo con cambio de significado",
        "pregunta": "¿Qué diferencia hay?\n\n«Fue al médico» vs «Se fue»",
        "opciones": [
            "Ninguna, son sinónimas",
            "'Fue' = desplazamiento; 'se fue' = marcharse definitivamente o con énfasis en el alejamiento",
            "'Se fue' es incorrecto",
            "'Fue' implica ida y vuelta; 'se fue' solo ida",
        ],
        "respuesta": "'Fue' = desplazamiento; 'se fue' = marcharse definitivamente o con énfasis en el alejamiento",
        "explicacion": "El 'se' aspectual añade matices: 'comió' (comió algo) vs 'se comió' (comió todo, con implicación de completitud). 'Fue' vs 'se fue': el reflexivo enfatiza el alejamiento o la acción completa.",
        "nivel": "C1",
    },
    {
        "tipo": "OD/OI con verbos de comunicación",
        "pregunta": "¿Cuál es la forma correcta con pronombres?\n\n«Expliqué el problema a mis compañeros»",
        "opciones": ["Les expliqué", "Los expliqué", "Se los expliqué", "Se les expliqué"],
        "respuesta": "Se los expliqué",
        "explicacion": "Si sustituimos ambos complementos: OI 'a mis compañeros' → les → se (ante OD). OD 'el problema' → lo. Resultado: 'se lo expliqué'. *Se les expliqué* es incorrecto.",
        "nivel": "C1",
    },
    {
        "tipo": "Duplicación de OI",
        "pregunta": "¿Cuál de estas frases es la correcta en español estándar?",
        "opciones": [
            "A María compré un regalo",
            "A María le compré un regalo",
            "Le compré a María",
            "Compré a María un regalo",
        ],
        "respuesta": "A María le compré un regalo",
        "explicacion": "En español, cuando el OI aparece explícito como sintagma nominal ('a María'), el pronombre OI (le) TAMBIÉN debe aparecer. Esta duplicación es obligatoria en la mayoría de los dialectos.",
        "nivel": "C1",
    },
    {
        "tipo": "Se con verbos intransitivos",
        "pregunta": "¿Qué función tiene 'se' en: «Se murió de repente»?",
        "opciones": [
            "Reflexivo (la acción recae sobre el sujeto)",
            "Se dativo (añade matiz afectivo o de afectación del sujeto)",
            "Pasivo reflejo",
            "Impersonal",
        ],
        "respuesta": "Se dativo (añade matiz afectivo o de afectación del sujeto)",
        "explicacion": "El 'se' aspectual-afectivo añade un matiz de involuntariedad o de mayor implicación del sujeto: 'murió' (dato objetivo) vs 'se murió' (implica afectación, puede sonar más emotivo o lamentable).",
        "nivel": "C2",
    },
    {
        "tipo": "Imperativo con pronombres",
        "pregunta": "¿Cuál es la forma correcta?\n\n«Dile a tu hermana que venga» → con pronombres implícitos: ___",
        "opciones": ["Díla que venga", "Dísela que venga", "Dile que venga", "Se dile que venga"],
        "respuesta": "Dile que venga",
        "explicacion": "Aquí solo hay OI ('a tu hermana' → le). No hay OD que sustituir (la subordinada 'que venga' no se pronominaliza). El pronombre va enclítico al imperativo: 'dile'.",
        "nivel": "C1",
    },
    {
        "tipo": "Se impersonal vs pasiva refleja",
        "pregunta": "¿Cuál es la diferencia?\n\n«Se busca secretaria» vs «Se buscan secretarias»",
        "opciones": [
            "Ninguna, son intercambiables",
            "La primera es impersonal (el verbo no concuerda); la segunda es pasiva refleja (el verbo concuerda con el sujeto)",
            "La primera es pasiva refleja; la segunda es impersonal",
            "Ambas son pasivas reflejas",
        ],
        "respuesta": "La primera es impersonal (el verbo no concuerda); la segunda es pasiva refleja (el verbo concuerda con el sujeto)",
        "explicacion": "'Se busca secretaria': impersonal, verbo en singular aunque 'secretaria' sea el OD. 'Se buscan secretarias': pasiva refleja, el verbo concuerda con el sujeto paciente 'secretarias'.",
        "nivel": "C2",
    },
]

# ─────────────────────────────────────────────
#  DATOS — ERRORES DE ANGLOHABLANTES
# ─────────────────────────────────────────────

ERRORES_INGLES: List[Dict] = [
    {
        "categoria": "Falsos amigos",
        "error": "*Estoy muy embarazada por lo que has dicho.*",
        "correccion": "Estoy muy avergonzada / me ha dado mucha vergüenza lo que has dicho.",
        "explicacion": "'Embarazada' = pregnant (encinta). 'Embarrassed' en inglés = avergonzado/a en español. Este es uno de los falsos amigos más frecuentes entre anglohablantes.",
        "nivel": "B2",
        "extra": "Otros falsos amigos clave: 'sensible' (sensitivo ≠ sensible), 'actual' (real/actual ≠ actual), 'library' (biblioteca ≠ librería).",
    },
    {
        "categoria": "Calco del inglés",
        "error": "*Estoy excitado por el concierto de esta noche.*",
        "correccion": "Estoy emocionado / ilusionado / muy animado con el concierto de esta noche.",
        "explicacion": "'Excitado' en español tiene connotación sexual en muchos contextos. 'Excited' en inglés = emocionado, entusiasmado. Usar 'emocionado', 'entusiasmado' o 'ilusionado'.",
        "nivel": "B2",
        "extra": "Otros calcos frecuentes: 'realizar' (to realize = darse cuenta, no 'realizar') aunque este uso está cada vez más extendido.",
    },
    {
        "categoria": "Artículo",
        "error": "*La vida es bonita.*",
        "correccion": "La vida es bonita. ✅ (Esta frase es correcta)",
        "explicacion": "En español, los sustantivos en sentido genérico llevan artículo: 'La vida es corta', 'El tiempo es oro'. En inglés no: 'Life is short'. Este es un error opuesto: anglohablantes a veces omiten el artículo donde sí es necesario.",
        "nivel": "B2",
        "extra": "Omisión incorrecta: *'Vida es bonita'* (sin artículo) sería el error típico. En español, el artículo con genéricos es obligatorio.",
    },
    {
        "categoria": "Ser vs Estar",
        "error": "*El cielo es muy azul hoy.*",
        "correccion": "El cielo está muy azul hoy.",
        "explicacion": "'Estar' para estados temporales o resultados perceptibles en un momento concreto. 'Hoy' indica temporalidad → estar. 'El cielo es azul' (en general, como característica) también sería válido pero sin 'hoy'.",
        "nivel": "C1",
        "extra": "Regla C1: algunos adjetivos cambian de significado con ser/estar: 'es aburrido' (su personalidad) vs 'está aburrido' (ahora mismo); 'es malo' vs 'está malo' (enfermo).",
    },
    {
        "categoria": "Ser vs Estar",
        "error": "*La película fue muy aburrida. Estaba dormido al final.*",
        "correccion": "La película fue muy aburrida. Me quedé dormido al final.",
        "explicacion": "'Quedarse + adjetivo/participio' expresa un cambio de estado: quedarse dormido, quedarse callado, quedarse paralizado. 'Estaba dormido' describe el estado resultante, pero 'me quedé dormido' expresa el proceso de quedarse dormido durante la película.",
        "nivel": "C1",
        "extra": "Verbos de cambio de estado esenciales para el C1: volverse, ponerse, quedarse, hacerse, llegar a ser.",
    },
    {
        "categoria": "Por vs Para",
        "error": "*Lo hice por impresionarte.*",
        "correccion": "Lo hice para impresionarte.",
        "explicacion": "'Para + infinitivo' expresa finalidad o propósito consciente. 'Por + infinitivo' expresa causa o motivo: 'lo hice por miedo' (causa, no finalidad). 'Lo hice por impresionarte' sugeriría 'a causa de querer impresionarte', que es gramaticalmente extraño.",
        "nivel": "C1",
        "extra": "Regla general: PARA = destino, finalidad, destinatario. POR = causa, duración, intercambio, agente en pasiva.",
    },
    {
        "categoria": "Por vs Para",
        "error": "*El paquete fue enviado para mensajero.*",
        "correccion": "El paquete fue enviado por mensajero.",
        "explicacion": "En la voz pasiva, el agente (quien realiza la acción) va introducido por 'por', no 'para': 'fue escrito por García Márquez', 'fue enviado por mensajero'.",
        "nivel": "C1",
        "extra": "'Para' indica destino o destinatario: 'el paquete es para ti' (destinatario). 'Por' indica el agente: 'fue enviado por DHL'.",
    },
    {
        "categoria": "Preposiciones verbales",
        "error": "*Depende de si vienes o no.*",
        "correccion": "Depende de si vienes o no. ✅ (Correcta)",
        "explicacion": "Esta frase es correcta. El error frecuente de anglohablantes es omitir la preposición: *'depende si vienes'* (incorrecto). 'Depender de' exige 'de' incluso ante oraciones subordinadas.",
        "nivel": "C1",
        "extra": "Otros verbos que mantienen la preposición ante que/si: acordarse de que, olvidarse de que, asegurarse de que, convencerse de que.",
    },
    {
        "categoria": "Queísmo / Dequeísmo",
        "error": "*Estoy seguro de que vendrá, pero pienso de que llegará tarde.*",
        "correccion": "Estoy seguro de que vendrá, pero pienso que llegará tarde.",
        "explicacion": "'Dequeísmo': añadir 'de' donde no corresponde. 'Pienso de que' es incorrecto; 'pienso que' es lo normativo. 'Queísmo': omitir 'de' donde sí corresponde ('estoy seguro que' es incorrecto: debe ser 'seguro de que').",
        "nivel": "C1",
        "extra": "Truco: sustituye la subordinada por 'eso'. Si puedes decir 'pienso eso' → no lleva 'de'. Si dices 'estoy seguro de eso' → sí lleva 'de'.",
    },
    {
        "categoria": "Haber impersonal",
        "error": "*Habían muchas personas en la reunión.*",
        "correccion": "Había muchas personas en la reunión.",
        "explicacion": "'Haber' en sentido existencial es impersonal: siempre en singular. *'Habían'*, *'hubieron'*, *'habrán'* (en sentido existencial) son incorrectos, aunque están muy extendidos coloquialmente. El DELE exige la forma normativa.",
        "nivel": "C1",
        "extra": "Correcto: 'Hay muchas personas', 'Había mucha gente', 'Habrá varios problemas'. Incorrecto: *'hay personas'* sin artículo también es un error frecuente de anglohablantes.",
    },
    {
        "categoria": "Tiempos verbales: indefinido vs imperfecto",
        "error": "*Cuando era pequeña, fui a la playa todos los veranos.*",
        "correccion": "Cuando era pequeña, iba a la playa todos los veranos.",
        "explicacion": "El imperfecto expresa acciones habituales o repetidas en el pasado. El indefinido expresa acciones puntuales y completadas. 'Todos los veranos' indica habitualidad → imperfecto ('iba').",
        "nivel": "B2",
        "extra": "Contraste: 'El verano pasado fui a la playa' (acción puntual, indefinido) vs 'De pequeña iba a la playa' (habitual, imperfecto).",
    },
    {
        "categoria": "Tiempos verbales: pretérito perfecto vs indefinido",
        "error": "*Esta mañana tuve una reunión muy productiva.*",
        "correccion": "Esta mañana he tenido una reunión muy productiva. (España) / Esta mañana tuve... (Latinoamérica)",
        "explicacion": "En España, el pretérito perfecto ('he tenido') se usa cuando el marco temporal incluye el presente: 'esta mañana', 'hoy', 'este año'. El indefinido ('tuve') es estándar en Latinoamérica para cualquier pasado. El DELE acepta ambas normas, pero es importante ser consistente.",
        "nivel": "C1",
        "extra": "Palabras que exigen perfecto en España: hoy, esta semana, este mes, este año, antes, ya, todavía, nunca (con valor actual).",
    },
    {
        "categoria": "Calco estructural del inglés",
        "error": "*Estoy de acuerdo con usted completamente.*",
        "correccion": "Estoy completamente de acuerdo con usted.",
        "explicacion": "En español, los adverbios de grado ('completamente', 'totalmente', 'absolutamente') van generalmente antes del adjetivo o del grupo verbal, no al final. Este orden final es un calco del inglés ('I agree with you completely').",
        "nivel": "C1",
        "extra": "Más natural: 'Estoy totalmente de acuerdo', 'Coincido plenamente con su postura', 'No podría estar más de acuerdo'.",
    },
    {
        "categoria": "Verbos de cambio de estado",
        "error": "*Me hice muy cansada después del trabajo.*",
        "correccion": "Me puse muy cansada / Me quedé agotada después del trabajo.",
        "explicacion": "'Hacerse' expresa cambios profundos, de identidad o condición adquirida (hacerse médico, hacerse famoso, hacerse rico). Para estados físicos o emocionales temporales: 'ponerse' (proceso: ponerse nervioso) o 'quedarse' (resultado: quedarse dormido).",
        "nivel": "C1",
        "extra": "Resumen: PONERSE (cambio rápido, emocional/físico), QUEDARSE (resultado, a menudo involuntario), VOLVERSE (cambio de carácter), HACERSE (cambio de identidad/profesión).",
    },
]

# ─────────────────────────────────────────────
#  DATOS — COMPRENSIÓN LECTORA
# ─────────────────────────────────────────────

TEXTOS_LECTURA: List[Dict] = [
    {
        "titulo": "La paradoja de la elección",
        "fuente": "Texto adaptado · Nivel C1",
        "texto": """En las últimas décadas, la proliferación de opciones en todos los ámbitos de la vida cotidiana ha sido presentada como un síntoma inequívoco de progreso y libertad. Sin embargo, el psicólogo Barry Schwartz argumenta, en contra de la intuición dominante, que el exceso de opciones no solo no nos hace más libres, sino que nos paraliza y nos hace, paradójicamente, menos satisfechos.

Schwartz distingue entre dos tipos de personas: los "maximizadores", que dedican un esfuerzo considerable a explorar todas las opciones disponibles antes de tomar una decisión, y los "satisficientes", que optan por la primera alternativa que cumpla sus criterios mínimos. Contrariamente a lo que cabría esperar, los maximizadores, aunque objetivamente toman mejores decisiones, reportan niveles de satisfacción más bajos. La razón es simple: cuantas más opciones se han considerado, mayor es el pesar por las elegidas y mayor la capacidad de imaginar una alternativa mejor.

Este fenómeno, denominado "coste de oportunidad psicológico", se ve agravado por el efecto de comparación: en un mundo con pocas opciones, conformarse con lo disponible es inevitable y, por tanto, satisfactorio. En un mundo con infinitas opciones, la conformidad se percibe como un fracaso personal.

La implicación más inquietante es que la libertad de elección, elevada a dogma en las sociedades occidentales contemporáneas, puede convertirse en una fuente de parálisis y sufrimiento cuando alcanza cierto umbral. Más opciones no equivale necesariamente a más libertad real.""",
        "preguntas": [
            {
                "pregunta": "¿Cuál es la tesis principal del texto?",
                "opciones": [
                    "a) Tener más opciones siempre mejora nuestra calidad de vida.",
                    "b) El exceso de opciones puede reducir la satisfacción personal.",
                    "c) Los maximizadores son más felices que los satisficientes.",
                    "d) La libertad de elección es un mito en las sociedades modernas.",
                ],
                "respuesta": "b) El exceso de opciones puede reducir la satisfacción personal.",
                "explicacion": "El texto argumenta que, paradójicamente, más opciones genera más insatisfacción. Las opciones a) y c) contradicen el argumento. La d) es demasiado radical; el texto matiza que depende del umbral.",
            },
            {
                "pregunta": "Según el texto, ¿qué caracteriza a los 'maximizadores'?",
                "opciones": [
                    "a) Eligen la primera opción que cumpla sus criterios básicos.",
                    "b) Siempre toman las peores decisiones.",
                    "c) Examinan todas las opciones pero reportan menor satisfacción.",
                    "d) Son más felices porque toman mejores decisiones objetivas.",
                ],
                "respuesta": "c) Examinan todas las opciones pero reportan menor satisfacción.",
                "explicacion": "El texto dice explícitamente que los maximizadores 'toman mejores decisiones' pero 'reportan niveles de satisfacción más bajos'. La opción d) solo recoge la primera parte.",
            },
            {
                "pregunta": "¿Qué significa 'coste de oportunidad psicológico' en el contexto del texto?",
                "opciones": [
                    "a) El dinero que cuesta explorar todas las opciones.",
                    "b) El pesar que genera pensar en las alternativas que no elegimos.",
                    "c) El esfuerzo mental de tomar decisiones complejas.",
                    "d) La dificultad de comparar opciones muy similares.",
                ],
                "respuesta": "b) El pesar que genera pensar en las alternativas que no elegimos.",
                "explicacion": "El texto lo explica directamente: 'mayor es el pesar por las elegidas y mayor la capacidad de imaginar una alternativa mejor'. Es el coste emocional de lo no elegido.",
            },
            {
                "pregunta": "¿Qué implica el texto sobre la relación entre libertad y opciones?",
                "opciones": [
                    "a) Más libertad siempre conlleva más opciones.",
                    "b) La libertad solo existe cuando hay pocas opciones.",
                    "c) A partir de cierto punto, más opciones no equivalen a más libertad real.",
                    "d) La libertad de elección es incompatible con la satisfacción personal.",
                ],
                "respuesta": "c) A partir de cierto punto, más opciones no equivalen a más libertad real.",
                "explicacion": "La última oración lo expresa claramente: 'Más opciones no equivale necesariamente a más libertad real'. No se niega la libertad en general, solo se matiza su relación con el número de opciones.",
            },
        ],
    },
    {
        "titulo": "El español y su expansión global",
        "fuente": "Texto adaptado · Nivel C1",
        "texto": """El español es hoy la segunda lengua del mundo por número de hablantes nativos y la cuarta por número total de usuarios, incluyendo quienes la aprenden como lengua extranjera. Sin embargo, más allá de las estadísticas, lo que resulta verdaderamente singular es la velocidad a la que esta expansión se está produciendo, especialmente en los Estados Unidos.

Según las proyecciones del Instituto Cervantes, en 2050 Estados Unidos podría ser el primer país hispanohablante del mundo por delante de México, con más de 130 millones de hispanohablantes. Este crecimiento no obedece únicamente a la inmigración, sino también al auge del español como segunda lengua entre la población angloparlante, estimulado en parte por razones económicas y profesionales.

No obstante, esta expansión no está exenta de tensiones. El debate sobre si el español debe ser lengua cooficial en algunos estados norteamericanos, o si la enseñanza bilingüe debe fomentarse en las escuelas públicas, refleja las fricciones entre la asimilación y la preservación de la identidad cultural. Para muchos hispanos de segunda o tercera generación, el español se convierte en una cuestión identitaria de gran carga simbólica, independientemente de su competencia real en la lengua.

Por otro lado, la diversidad interna del español —con sus variedades léxicas, fonéticas y pragmáticas— plantea el interrogante de qué español se enseña y cuál se considera estándar o prestigioso. La respuesta, inevitablemente, está teñida de consideraciones políticas y económicas que van mucho más allá de la lingüística pura.""",
        "preguntas": [
            {
                "pregunta": "¿Qué dato hace singular la situación del español, según el texto?",
                "opciones": [
                    "a) El número total de hablantes nativos.",
                    "b) La velocidad de su expansión, especialmente en EE.UU.",
                    "c) Su condición de cuarta lengua por número de usuarios.",
                    "d) El número de países donde es lengua oficial.",
                ],
                "respuesta": "b) La velocidad de su expansión, especialmente en EE.UU.",
                "explicacion": "El texto dice: 'lo que resulta verdaderamente singular es la velocidad a la que esta expansión se está produciendo, especialmente en los Estados Unidos'.",
            },
            {
                "pregunta": "Según el texto, ¿por qué crece el español en EE.UU.?",
                "opciones": [
                    "a) Solo por la inmigración latinoamericana.",
                    "b) Por la inmigración y el aprendizaje por razones económicas y profesionales.",
                    "c) Porque el gobierno promueve la cooficialidad del español.",
                    "d) Por el prestigio cultural de los países hispanohablantes.",
                ],
                "respuesta": "b) Por la inmigración y el aprendizaje por razones económicas y profesionales.",
                "explicacion": "El texto afirma que el crecimiento 'no obedece únicamente a la inmigración, sino también al auge del español como segunda lengua... estimulado en parte por razones económicas y profesionales'.",
            },
            {
                "pregunta": "¿Qué quiere decir el texto cuando habla del español como 'cuestión identitaria de gran carga simbólica'?",
                "opciones": [
                    "a) Que hablar español otorga ventajas económicas.",
                    "b) Que el español representa la identidad cultural incluso cuando no se domina bien.",
                    "c) Que la identidad hispana depende del nivel de competencia en español.",
                    "d) Que los hispanohablantes de segunda generación rechazan el español.",
                ],
                "respuesta": "b) Que el español representa la identidad cultural incluso cuando no se domina bien.",
                "explicacion": "El texto dice: 'el español se convierte en una cuestión identitaria de gran carga simbólica, independientemente de su competencia real en la lengua'. La lengua funciona como símbolo aunque no se hable bien.",
            },
            {
                "pregunta": "¿Cuál es el interrogante que plantea la diversidad interna del español?",
                "opciones": [
                    "a) Si el español desplazará al inglés en EE.UU.",
                    "b) Cuántas variedades de español existen en el mundo.",
                    "c) Qué variedad se considera estándar o prestigiosa y quién lo decide.",
                    "d) Si la diversidad lingüística es positiva o negativa.",
                ],
                "respuesta": "c) Qué variedad se considera estándar o prestigiosa y quién lo decide.",
                "explicacion": "'¿Qué español se enseña y cuál se considera estándar o prestigioso?' es la pregunta explícita. La respuesta 'está teñida de consideraciones políticas y económicas', lo que implica que no es una decisión puramente lingüística.",
            },
        ],
    },
    {
        "titulo": "La economía del sueño",
        "fuente": "Texto adaptado · Nivel C1",
        "texto": """Dormir bien no es solo una cuestión de bienestar individual. Es, cada vez más, un factor estratégico para la productividad económica. Varios estudios han cuantificado el impacto del déficit de sueño en términos de pérdida de productividad laboral, y los resultados son llamativos: se estima que en países como Estados Unidos, Japón o Alemania, la privación de sueño cuesta a las economías nacionales entre el 1,5 y el 3% del PIB anual.

Sin embargo, la paradoja es notable: las mismas culturas laborales que generan ese déficit de sueño lo penalizan. Quien duerme en el trabajo es tachado de perezoso, mientras que quien trabaja sin parar recibe aplausos sociales. Esta glorificación del sacrificio y el agotamiento —lo que algunos investigadores llaman "la cultura del hustle"— no solo es contraproducente desde el punto de vista económico, sino que genera externalidades negativas en términos de salud pública.

Frente a este panorama, algunas empresas han comenzado a rediseñar sus entornos de trabajo para facilitar el descanso. Cabinas de siesta en las oficinas, horarios más flexibles o programas de gestión del sueño son algunas de las iniciativas que han surgido en los últimos años. No obstante, los críticos apuntan que estas medidas, sin un cambio cultural profundo, no son más que parches estéticos que no abordan la raíz del problema.

La conclusión que emerge de la investigación científica es incómoda pero inequívoca: somos fundamentalmente peores en casi todo —en creatividad, en toma de decisiones, en empatía, en regulación emocional— cuando dormimos mal. Y una sociedad que duerme mal, toma peores decisiones colectivas.""",
        "preguntas": [
            {
                "pregunta": "¿Cuál es la paradoja que describe el texto?",
                "opciones": [
                    "a) Dormir bien mejora la productividad pero perjudica la economía.",
                    "b) Las culturas que generan déficit de sueño penalizan a quienes duermen.",
                    "c) Las empresas invierten en sueño pero los trabajadores lo rechazan.",
                    "d) El sueño es valorado en teoría pero ignorado en la práctica científica.",
                ],
                "respuesta": "b) Las culturas que generan déficit de sueño penalizan a quienes duermen.",
                "explicacion": "La paradoja está en el segundo párrafo: las mismas culturas que producen el déficit de sueño castigan socialmente a quien duerme en el trabajo.",
            },
            {
                "pregunta": "¿Qué crítica se hace a las medidas empresariales mencionadas?",
                "opciones": [
                    "a) Que son demasiado caras para las empresas.",
                    "b) Que no funcionan porque los empleados no las usan.",
                    "c) Que son superficiales si no hay un cambio cultural de fondo.",
                    "d) Que generan desigualdad entre los trabajadores.",
                ],
                "respuesta": "c) Que son superficiales si no hay un cambio cultural de fondo.",
                "explicacion": "El texto dice que 'sin un cambio cultural profundo, no son más que parches estéticos que no abordan la raíz del problema'.",
            },
            {
                "pregunta": "¿Qué significa 'la cultura del hustle' en el contexto del texto?",
                "opciones": [
                    "a) Una tendencia a valorar el ocio y el descanso.",
                    "b) La glorificación del trabajo extremo y el agotamiento.",
                    "c) Un movimiento para regular las horas laborales.",
                    "d) La cultura empresarial que premia el sueño.",
                ],
                "respuesta": "b) La glorificación del trabajo extremo y el agotamiento.",
                "explicacion": "El texto define directamente: 'la glorificación del sacrificio y el agotamiento —lo que algunos investigadores llaman «la cultura del hustle»'.",
            },
            {
                "pregunta": "¿Cuál es la conclusión principal que ofrece el texto?",
                "opciones": [
                    "a) Las empresas deben instalar cabinas de siesta.",
                    "b) El déficit de sueño afecta negativamente al individuo y a la sociedad en su conjunto.",
                    "c) La economía moderna ha resuelto el problema del déficit de sueño.",
                    "d) Dormir bien es solo una cuestión de salud personal.",
                ],
                "respuesta": "b) El déficit de sueño afecta negativamente al individuo y a la sociedad en su conjunto.",
                "explicacion": "La conclusión final lo resume: somos peores en todo cuando dormimos mal, y 'una sociedad que duerme mal, toma peores decisiones colectivas'. El impacto es tanto individual como colectivo.",
            },
        ],
    },
]

# ─────────────────────────────────────────────
#  CONFIG
# ─────────────────────────────────────────────

NIVEL_COLORS = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}

st.set_page_config(
    page_title="Cata Gramática C1",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Lato', sans-serif; }
    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1280px; }

    .hero {
        background: linear-gradient(135deg, #064e3b 0%, #065f46 60%, #059669 100%);
        border-radius: 20px; padding: 1.6rem 2rem; margin-bottom: 1.2rem; color: white;
    }
    .hero h1 { font-family: 'Playfair Display', serif; font-size: 1.9rem; margin: 0 0 0.3rem 0; color: white; }
    .hero p { margin: 0; color: #a7f3d0; font-size: 0.95rem; }

    .card-box, .quiz-box {
        background: white; border: 1px solid #e5e7eb; border-radius: 18px;
        padding: 1.3rem; box-shadow: 0 4px 16px rgba(0,0,0,0.05); margin-bottom: 0.8rem;
    }
    .card-title {
        color: #064e3b; font-size: 1.5rem; font-weight: 700; margin-bottom: 0.5rem;
        font-family: 'Playfair Display', serif;
    }
    .tag {
        display: inline-block; border-radius: 999px; padding: 0.25rem 0.7rem;
        font-size: 0.8rem; font-weight: 700; margin-bottom: 0.6rem;
        background: #d1fae5; color: #064e3b;
    }
    .nivel-badge {
        display: inline-block; border-radius: 999px; padding: 0.2rem 0.6rem;
        font-size: 0.78rem; font-weight: 700; color: white; margin-left: 0.4rem;
    }
    .example-block {
        background: #ecfdf5; border-left: 3px solid #059669;
        border-radius: 0 10px 10px 0; padding: 0.55rem 0.9rem;
        margin: 0.35rem 0; font-style: italic; color: #065f46; font-size: 0.93rem;
    }
    .trampa-box {
        background: #fef3c7; border: 1px solid #fcd34d; border-radius: 10px;
        padding: 0.55rem 0.9rem; font-size: 0.88rem; color: #78350f; margin-top: 0.6rem;
    }
    .error-box {
        background: #fef2f2; border-left: 3px solid #ef4444;
        border-radius: 0 10px 10px 0; padding: 0.6rem 0.9rem;
        margin: 0.4rem 0; font-size: 0.93rem; color: #7f1d1d;
    }
    .correcto-box {
        background: #ecfdf5; border-left: 3px solid #059669;
        border-radius: 0 10px 10px 0; padding: 0.6rem 0.9rem;
        margin: 0.4rem 0; font-size: 0.93rem; color: #065f46;
    }
    .texto-lectura {
        background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 14px;
        padding: 1.4rem; font-size: 0.97rem; color: #1f2937;
        line-height: 1.8; margin-bottom: 1rem;
    }
    .section-title {
        font-size: 1.1rem; font-weight: 700; color: #064e3b; margin-bottom: 0.2rem;
        font-family: 'Playfair Display', serif;
    }
    .section-sub { color: #6b7280; margin-bottom: 0.8rem; font-size: 0.9rem; }
    .metric-card {
        background: white; border: 1px solid #e5e7eb; border-radius: 16px;
        padding: 0.85rem 1rem; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .metric-value { font-size: 1.6rem; font-weight: 700; color: #064e3b; }
    .metric-label { font-size: 0.82rem; color: #6b7280; margin-top: 0.15rem; }
    .feedback-ok {
        background: #ecfdf5; border: 1px solid #6ee7b7; color: #065f46;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem; white-space: pre-wrap;
    }
    .feedback-bad {
        background: #fef2f2; border: 1px solid #fca5a5; color: #7f1d1d;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem; white-space: pre-wrap;
    }
    .feedback-neutral {
        background: #f8fafc; border: 1px solid #e2e8f0; color: #334155;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem; white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ESTADO
# ─────────────────────────────────────────────

def init_state():
    defaults = {
        # Subjuntivo
        "subj_idx": None, "subj_ans": None, "subj_fb": None,
        "subj_score": 0, "subj_total": 0,
        # Perífrasis — tarjetas
        "peri_card_idx": 0, "peri_quiz_idx": None, "peri_quiz_fb": None,
        "peri_score": 0, "peri_total": 0,
        # Estilo indirecto
        "ei_idx": None, "ei_fb": None, "ei_score": 0, "ei_total": 0,
        # Pronombres
        "pron_idx": None, "pron_fb": None, "pron_score": 0, "pron_total": 0,
        # Errores inglés
        "err_idx": 0, "err_revealed": False,
        # Lectura
        "lect_idx": 0, "lect_answers": {}, "lect_checked": False,
        "lect_score": 0, "lect_total": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def normalize(t: str) -> str:
    return " ".join(t.lower().strip().split())

def show_fb(kind: str, msg: str):
    css = {"ok": "feedback-ok", "bad": "feedback-bad",
           "neutral": "feedback-neutral"}.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  RENDER
# ─────────────────────────────────────────────

init_state()

st.markdown("""
<div class="hero">
    <h1>📝 Gramática C1 · DELE Cervantes</h1>
    <p>Subjuntivo · Perífrasis · Estilo indirecto · Pronombres · Errores de anglohablantes · Comprensión lectora</p>
</div>
""", unsafe_allow_html=True)

# Métricas
m1, m2, m3, m4 = st.columns(4)
for col, val, label in [
    (m1, f"{st.session_state.subj_score}/{st.session_state.subj_total}", "subjuntivo"),
    (m2, f"{st.session_state.peri_score}/{st.session_state.peri_total}", "perífrasis"),
    (m3, f"{st.session_state.ei_score}/{st.session_state.ei_total}", "estilo indirecto"),
    (m4, f"{st.session_state.pron_score}/{st.session_state.pron_total}", "pronombres"),
]:
    col.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div>'
                 f'<div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔀 Subjuntivo",
    "⚙️ Perífrasis",
    "💬 Estilo indirecto",
    "🔤 Pronombres",
    "🇬🇧 Errores anglohablantes",
    "📚 Comprensión lectora",
])

# ══════════════════════════════
#  TAB 1 — SUBJUNTIVO
# ══════════════════════════════
with tab1:
    st.markdown('<div class="section-title">Subjuntivo vs Indicativo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Rellena el hueco con la forma correcta del verbo. Nivel C1 · DELE Cervantes.</div>', unsafe_allow_html=True)

    if st.session_state.subj_idx is None:
        st.session_state.subj_idx = random.randrange(len(SUBJUNTIVO))

    ej = SUBJUNTIVO[st.session_state.subj_idx]
    nc = NIVEL_COLORS.get(ej.get("nivel", "C1"), "#8b5cf6")

    frase_html = ej["frase"].replace("___", '<span style="background:#d1fae5;color:#065f46;'
                                     'padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
    st.markdown(f'<div class="quiz-box">'
                f'<span class="tag">{ej["tipo"]}</span>'
                f'<span class="nivel-badge" style="background:{nc};">{ej.get("nivel","C1")}</span>'
                f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{frase_html}</p>'
                f'</div>', unsafe_allow_html=True)

    user_ans = st.text_input("Tu respuesta (forma verbal):",
                              placeholder="Ej: haya terminado / fuera / tenga...",
                              key=f"subj_input_{st.session_state.subj_idx}")

    s1, s2, s3 = st.columns(3)
    with s1:
        if st.button("Comprobar ✓", key="subj_check", use_container_width=True):
            st.session_state.subj_total += 1
            if normalize(user_ans) == normalize(ej["respuesta"]):
                st.session_state.subj_score += 1
                st.session_state.subj_fb = ("ok",
                    f"✅ Correcto: **{ej['respuesta']}**\n\n"
                    f"📖 {ej['explicacion']}"
                    + (f"\n\n⚠️ Truco: {ej['trampa']}" if ej.get('trampa') else ""))
            else:
                st.session_state.subj_fb = ("bad",
                    f"❌ Respuesta correcta: **{ej['respuesta']}**\n\n"
                    f"📖 {ej['explicacion']}"
                    + (f"\n\n⚠️ Truco: {ej['trampa']}" if ej.get('trampa') else ""))
            st.rerun()
    with s2:
        if st.button("Ver solución 👁", key="subj_sol", use_container_width=True):
            st.session_state.subj_fb = ("neutral",
                f"**{ej['respuesta']}** ({ej['tipo']})\n\n"
                f"📖 {ej['explicacion']}"
                + (f"\n\n⚠️ Truco: {ej['trampa']}" if ej.get('trampa') else ""))
            st.rerun()
    with s3:
        if st.button("Nueva →", key="subj_next", use_container_width=True):
            st.session_state.subj_idx = random.randrange(len(SUBJUNTIVO))
            st.session_state.subj_fb = None
            st.rerun()

    if st.session_state.subj_fb:
        show_fb(*st.session_state.subj_fb)

    if st.session_state.subj_total:
        pct = int(st.session_state.subj_score / st.session_state.subj_total * 100)
        st.progress(st.session_state.subj_score / st.session_state.subj_total)
        st.caption(f"Precisión: {st.session_state.subj_score}/{st.session_state.subj_total} ({pct} %)")
        if st.button("Reiniciar", key="subj_reset"):
            st.session_state.subj_score = 0
            st.session_state.subj_total = 0
            st.session_state.subj_fb = None
            st.rerun()

    st.markdown("---")
    st.markdown("**Tipos de subjuntivo en este módulo:**")
    tipos = list(dict.fromkeys(e["tipo"] for e in SUBJUNTIVO))
    cols = st.columns(3)
    for i, tipo in enumerate(tipos):
        cols[i % 3].markdown(f"• {tipo}")


# ══════════════════════════════
#  TAB 2 — PERÍFRASIS
# ══════════════════════════════
with tab2:
    st.markdown('<div class="section-title">Perífrasis verbales</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Estudia las perífrasis más importantes para el C1 y practica con ejercicios de producción.</div>', unsafe_allow_html=True)

    ptab1, ptab2 = st.tabs(["📖 Tarjetas", "✏️ Ejercicios"])

    with ptab1:
        idx = st.session_state.peri_card_idx % len(PERIFRASIS)
        p = PERIFRASIS[idx]
        nc_p = NIVEL_COLORS.get(p.get("nivel", "C1"), "#8b5cf6")

        st.markdown(f"""
        <div class="card-box">
            <span class="tag">{p['perifrasis']}</span>
            <span class="nivel-badge" style="background:{nc_p};">{p.get('nivel','C1')}</span>
            <div class="card-title">{p['perifrasis']}</div>
            <div style="color:#374151;margin-bottom:0.6rem;">{p['significado']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Ejemplos:**")
        for ej in p["ejemplos"]:
            st.markdown(f'<div class="example-block">{ej}</div>', unsafe_allow_html=True)

        if p.get("trampa"):
            st.markdown(f'<div class="trampa-box">⚠️ <strong>Atención:</strong> {p["trampa"]}</div>',
                        unsafe_allow_html=True)

        pc1, pc2, pc3 = st.columns(3)
        with pc1:
            if st.button("← Anterior", key="peri_prev", use_container_width=True):
                st.session_state.peri_card_idx = (idx - 1) % len(PERIFRASIS)
                st.rerun()
        with pc2:
            if st.button("Siguiente →", key="peri_next", use_container_width=True):
                st.session_state.peri_card_idx = (idx + 1) % len(PERIFRASIS)
                st.rerun()
        with pc3:
            if st.button("Aleatoria 🎲", key="peri_rand", use_container_width=True):
                st.session_state.peri_card_idx = random.randrange(len(PERIFRASIS))
                st.rerun()
        st.caption(f"Perífrasis {idx + 1} de {len(PERIFRASIS)}")

    with ptab2:
        if st.session_state.peri_quiz_idx is None:
            st.session_state.peri_quiz_idx = random.randrange(len(PERIFRASIS))

        pq = PERIFRASIS[st.session_state.peri_quiz_idx]
        nc_pq = NIVEL_COLORS.get(pq.get("nivel", "C1"), "#8b5cf6")

        frase_pq = pq["ejercicio"].replace("___",
            '<span style="background:#d1fae5;color:#065f46;padding:2px 10px;'
            'border-radius:6px;font-weight:700;">___</span>')
        st.markdown(f'<div class="quiz-box">'
                    f'<span class="tag">{pq["perifrasis"]}</span>'
                    f'<span class="nivel-badge" style="background:{nc_pq};">{pq.get("nivel","C1")}</span>'
                    f'<p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{frase_pq}</p>'
                    f'</div>', unsafe_allow_html=True)

        pq_ans = st.text_input("Completa con la perífrasis correcta:",
                                placeholder="Ej: lleva trabajando / dejó de fumar...",
                                key=f"peri_input_{st.session_state.peri_quiz_idx}")

        pq1, pq2, pq3 = st.columns(3)
        with pq1:
            if st.button("Comprobar ✓", key="peri_check", use_container_width=True):
                st.session_state.peri_total += 1
                # Accept if the key verb form is present
                correct_tokens = set(normalize(pq["respuesta"]).split())
                user_tokens = set(normalize(pq_ans).split())
                if len(correct_tokens & user_tokens) >= len(correct_tokens) - 1:
                    st.session_state.peri_score += 1
                    st.session_state.peri_quiz_fb = ("ok",
                        f"✅ Correcto. Forma esperada: **{pq['respuesta']}**\n\n"
                        f"📖 {pq['significado']}"
                        + (f"\n\n⚠️ {pq['trampa']}" if pq.get('trampa') else ""))
                else:
                    st.session_state.peri_quiz_fb = ("bad",
                        f"❌ Forma correcta: **{pq['respuesta']}**\n\n"
                        f"📖 {pq['significado']}"
                        + (f"\n\n⚠️ {pq['trampa']}" if pq.get('trampa') else ""))
                st.rerun()
        with pq2:
            if st.button("Ver solución 👁", key="peri_sol", use_container_width=True):
                st.session_state.peri_quiz_fb = ("neutral",
                    f"**{pq['respuesta']}**\n\n📖 {pq['significado']}")
                st.rerun()
        with pq3:
            if st.button("Nueva →", key="peri_next_q", use_container_width=True):
                st.session_state.peri_quiz_idx = random.randrange(len(PERIFRASIS))
                st.session_state.peri_quiz_fb = None
                st.rerun()

        if st.session_state.peri_quiz_fb:
            show_fb(*st.session_state.peri_quiz_fb)

        if st.session_state.peri_total:
            pct = int(st.session_state.peri_score / st.session_state.peri_total * 100)
            st.progress(st.session_state.peri_score / st.session_state.peri_total)
            st.caption(f"Precisión: {st.session_state.peri_score}/{st.session_state.peri_total} ({pct} %)")


# ══════════════════════════════
#  TAB 3 — ESTILO INDIRECTO
# ══════════════════════════════
with tab3:
    st.markdown('<div class="section-title">Estilo indirecto</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Transforma las frases al estilo indirecto. Fundamental en el DELE C1.</div>', unsafe_allow_html=True)

    if st.session_state.ei_idx is None:
        st.session_state.ei_idx = random.randrange(len(ESTILO_INDIRECTO))

    ei = ESTILO_INDIRECTO[st.session_state.ei_idx]
    nc_ei = NIVEL_COLORS.get(ei.get("nivel", "C1"), "#8b5cf6")

    st.markdown(f"""
    <div class="quiz-box">
        <span class="nivel-badge" style="background:{nc_ei};margin-bottom:0.6rem;display:inline-block;">{ei.get("nivel","C1")}</span>
        <p style="font-size:1rem;color:#374151;margin-top:0.4rem;">
            <strong>Estilo directo:</strong> {ei['directo']}
        </p>
        <p style="font-size:1rem;color:#374151;">
            <strong>Transforma con:</strong> <em>{ei['verbo_intro']}...</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    ei_ans = st.text_area("Tu transformación:",
                           height=80,
                           placeholder=f"... {ei['verbo_intro']} ...",
                           key=f"ei_input_{st.session_state.ei_idx}")

    ei1, ei2, ei3 = st.columns(3)
    with ei1:
        if st.button("Comprobar ✓", key="ei_check", use_container_width=True):
            st.session_state.ei_total += 1
            correct_tokens = set(normalize(ei["respuesta"]).split())
            user_tokens = set(normalize(ei_ans).split())
            overlap = len(correct_tokens & user_tokens) / len(correct_tokens) if correct_tokens else 0
            if overlap >= 0.75:
                st.session_state.ei_score += 1
                st.session_state.ei_fb = ("ok",
                    f"✅ Correcto.\n\n"
                    f"Forma de referencia: *{ei['verbo_intro']} {ei['respuesta']}*\n\n"
                    f"📖 Cambios: {ei['cambios']}\n\n{ei['explicacion']}")
            else:
                st.session_state.ei_fb = ("bad",
                    f"❌ Forma correcta:\n\n*{ei['verbo_intro']} {ei['respuesta']}*\n\n"
                    f"📖 Cambios: {ei['cambios']}\n\n{ei['explicacion']}")
            st.rerun()
    with ei2:
        if st.button("Ver solución 👁", key="ei_sol", use_container_width=True):
            st.session_state.ei_fb = ("neutral",
                f"*{ei['verbo_intro']} {ei['respuesta']}*\n\n"
                f"📖 Cambios: {ei['cambios']}\n\n{ei['explicacion']}")
            st.rerun()
    with ei3:
        if st.button("Nueva →", key="ei_next", use_container_width=True):
            st.session_state.ei_idx = random.randrange(len(ESTILO_INDIRECTO))
            st.session_state.ei_fb = None
            st.rerun()

    if st.session_state.ei_fb:
        show_fb(*st.session_state.ei_fb)

    if st.session_state.ei_total:
        pct = int(st.session_state.ei_score / st.session_state.ei_total * 100)
        st.progress(st.session_state.ei_score / st.session_state.ei_total)
        st.caption(f"Precisión: {st.session_state.ei_score}/{st.session_state.ei_total} ({pct} %)")

    st.markdown("---")
    st.markdown("**Tabla de correspondencias temporales:**")
    tabla_html = """
    <table style="width:100%;border-collapse:collapse;font-size:0.88rem;background:white;border-radius:12px;overflow:hidden;border:1px solid #e5e7eb;">
    <thead><tr style="background:#d1fae5;">
        <th style="padding:0.5rem 0.8rem;text-align:left;color:#064e3b;">Estilo directo</th>
        <th style="padding:0.5rem 0.8rem;text-align:left;color:#064e3b;">Estilo indirecto (verbo pasado)</th>
    </tr></thead>
    <tbody>
    <tr style="border-top:1px solid #e5e7eb;"><td style="padding:0.45rem 0.8rem;">Presente (habla)</td><td style="padding:0.45rem 0.8rem;">Imperfecto (hablaba)</td></tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;"><td style="padding:0.45rem 0.8rem;">Pretérito perfecto (ha hablado)</td><td style="padding:0.45rem 0.8rem;">Pluscuamperfecto (había hablado)</td></tr>
    <tr style="border-top:1px solid #e5e7eb;"><td style="padding:0.45rem 0.8rem;">Futuro (hablará)</td><td style="padding:0.45rem 0.8rem;">Condicional (hablaría)</td></tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;"><td style="padding:0.45rem 0.8rem;">Imperativo (habla)</td><td style="padding:0.45rem 0.8rem;">Imperfecto subjuntivo (hablara)</td></tr>
    <tr style="border-top:1px solid #e5e7eb;"><td style="padding:0.45rem 0.8rem;">Pres. subjuntivo (hable)</td><td style="padding:0.45rem 0.8rem;">Imp. subjuntivo (hablara)</td></tr>
    <tr style="border-top:1px solid #e5e7eb;background:#f9fafb;"><td style="padding:0.45rem 0.8rem;">Perf. subjuntivo (haya hablado)</td><td style="padding:0.45rem 0.8rem;">Plusc. subjuntivo (hubiera hablado)</td></tr>
    </tbody>
    </table>
    <div style="font-size:0.82rem;color:#6b7280;margin-top:0.5rem;">
    Cambios de adverbio: mañana → al día siguiente · hoy → ese día · aquí → allí · este → ese/aquel
    </div>
    """
    st.markdown(tabla_html, unsafe_allow_html=True)


# ══════════════════════════════
#  TAB 4 — PRONOMBRES
# ══════════════════════════════
with tab4:
    st.markdown('<div class="section-title">Pronombres OD / OI / Reflexivos</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Combinaciones, posición y usos avanzados. Los errores de pronombres son muy frecuentes en el DELE C1.</div>', unsafe_allow_html=True)

    if st.session_state.pron_idx is None:
        st.session_state.pron_idx = random.randrange(len(PRONOMBRES))

    pr = PRONOMBRES[st.session_state.pron_idx]
    nc_pr = NIVEL_COLORS.get(pr.get("nivel", "C1"), "#8b5cf6")

    st.markdown(f"""
    <div class="quiz-box">
        <span class="tag">{pr['tipo']}</span>
        <span class="nivel-badge" style="background:{nc_pr};">{pr.get('nivel','C1')}</span>
        <p style="font-size:1.05rem;color:#1e1b4b;margin-top:0.6rem;">{pr['pregunta']}</p>
    </div>
    """, unsafe_allow_html=True)

    pr_sel = st.radio("Elige la opción correcta:", pr["opciones"],
                      key=f"pron_radio_{st.session_state.pron_idx}")

    pr1, pr2, pr3 = st.columns(3)
    with pr1:
        if st.button("Comprobar ✓", key="pron_check", use_container_width=True):
            st.session_state.pron_total += 1
            if pr_sel == pr["respuesta"]:
                st.session_state.pron_score += 1
                st.session_state.pron_fb = ("ok",
                    f"✅ Correcto: **{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            else:
                st.session_state.pron_fb = ("bad",
                    f"❌ Correcta: **{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            st.rerun()
    with pr2:
        if st.button("Ver solución 👁", key="pron_sol", use_container_width=True):
            st.session_state.pron_fb = ("neutral",
                f"**{pr['respuesta']}**\n\n📖 {pr['explicacion']}")
            st.rerun()
    with pr3:
        if st.button("Nueva →", key="pron_next", use_container_width=True):
            st.session_state.pron_idx = random.randrange(len(PRONOMBRES))
            st.session_state.pron_fb = None
            st.rerun()

    if st.session_state.pron_fb:
        show_fb(*st.session_state.pron_fb)

    if st.session_state.pron_total:
        pct = int(st.session_state.pron_score / st.session_state.pron_total * 100)
        st.progress(st.session_state.pron_score / st.session_state.pron_total)
        st.caption(f"Precisión: {st.session_state.pron_score}/{st.session_state.pron_total} ({pct} %)")
        if st.button("Reiniciar", key="pron_reset"):
            st.session_state.pron_score = 0
            st.session_state.pron_total = 0
            st.session_state.pron_fb = None
            st.rerun()

    st.markdown("---")
    st.markdown("**Tabla de combinaciones OI + OD:**")
    comb_html = """
    <table style="width:100%;border-collapse:collapse;font-size:0.88rem;background:white;border-radius:12px;overflow:hidden;border:1px solid #e5e7eb;">
    <thead><tr style="background:#d1fae5;">
        <th style="padding:0.5rem;color:#064e3b;">OI</th>
        <th style="padding:0.5rem;color:#064e3b;">+ lo</th>
        <th style="padding:0.5rem;color:#064e3b;">+ la</th>
        <th style="padding:0.5rem;color:#064e3b;">+ los</th>
        <th style="padding:0.5rem;color:#064e3b;">+ las</th>
    </tr></thead>
    <tbody>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;">
        <td style="padding:0.45rem;font-weight:700;background:#f9fafb;">me</td>
        <td style="padding:0.45rem;">me lo</td><td style="padding:0.45rem;">me la</td>
        <td style="padding:0.45rem;">me los</td><td style="padding:0.45rem;">me las</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;">
        <td style="padding:0.45rem;font-weight:700;background:#f9fafb;">te</td>
        <td style="padding:0.45rem;">te lo</td><td style="padding:0.45rem;">te la</td>
        <td style="padding:0.45rem;">te los</td><td style="padding:0.45rem;">te las</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;background:#fef9c3;">
        <td style="padding:0.45rem;font-weight:700;">le → se</td>
        <td style="padding:0.45rem;font-weight:700;">se lo</td><td style="padding:0.45rem;font-weight:700;">se la</td>
        <td style="padding:0.45rem;font-weight:700;">se los</td><td style="padding:0.45rem;font-weight:700;">se las</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;">
        <td style="padding:0.45rem;font-weight:700;background:#f9fafb;">nos</td>
        <td style="padding:0.45rem;">nos lo</td><td style="padding:0.45rem;">nos la</td>
        <td style="padding:0.45rem;">nos los</td><td style="padding:0.45rem;">nos las</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;">
        <td style="padding:0.45rem;font-weight:700;background:#f9fafb;">os</td>
        <td style="padding:0.45rem;">os lo</td><td style="padding:0.45rem;">os la</td>
        <td style="padding:0.45rem;">os los</td><td style="padding:0.45rem;">os las</td>
    </tr>
    <tr style="border-top:1px solid #e5e7eb;text-align:center;background:#fef9c3;">
        <td style="padding:0.45rem;font-weight:700;">les → se</td>
        <td style="padding:0.45rem;font-weight:700;">se lo</td><td style="padding:0.45rem;font-weight:700;">se la</td>
        <td style="padding:0.45rem;font-weight:700;">se los</td><td style="padding:0.45rem;font-weight:700;">se las</td>
    </tr>
    </tbody>
    </table>
    <div style="font-size:0.82rem;color:#6b7280;margin-top:0.4rem;">⚠️ le/les + lo/la/los/las → siempre SE (no *le lo, *les la...)</div>
    """
    st.markdown(comb_html, unsafe_allow_html=True)


# ══════════════════════════════
#  TAB 5 — ERRORES ANGLOHABLANTES
# ══════════════════════════════
with tab5:
    st.markdown('<div class="section-title">Errores frecuentes de anglohablantes</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Detecta el error, entiende por qué ocurre y aprende la forma correcta. Especialmente relevante para el DELE C1.</div>', unsafe_allow_html=True)

    err = ERRORES_INGLES[st.session_state.err_idx]
    nc_err = NIVEL_COLORS.get(err.get("nivel", "C1"), "#8b5cf6")

    st.markdown(
        f'<span class="tag">{err["categoria"]}</span>'
        f'<span class="nivel-badge" style="background:{nc_err};">{err.get("nivel","C1")}</span>',
        unsafe_allow_html=True,
    )

    # Show the error
    st.markdown(f'<div class="error-box">❌ <strong>Error frecuente:</strong> {err["error"]}</div>',
                unsafe_allow_html=True)

    if not st.session_state.err_revealed:
        if st.button("👁 Ver corrección y explicación", use_container_width=False, key="err_reveal"):
            st.session_state.err_revealed = True
            st.rerun()
    else:
        st.markdown(f'<div class="correcto-box">✅ <strong>Corrección:</strong> {err["correccion"]}</div>',
                    unsafe_allow_html=True)
        st.markdown(f'<div class="quiz-box"><strong>📖 Explicación:</strong><br>{err["explicacion"]}</div>',
                    unsafe_allow_html=True)
        if err.get("extra"):
            st.markdown(f'<div class="trampa-box">💡 <strong>Saber más:</strong> {err["extra"]}</div>',
                        unsafe_allow_html=True)

    st.markdown("")
    e1, e2, e3 = st.columns(3)
    with e1:
        if st.button("← Anterior", key="err_prev", use_container_width=True):
            st.session_state.err_idx = (st.session_state.err_idx - 1) % len(ERRORES_INGLES)
            st.session_state.err_revealed = False
            st.rerun()
    with e2:
        st.markdown(f'<p style="text-align:center;color:#6b7280;padding-top:0.5rem;">'
                    f'{st.session_state.err_idx + 1} / {len(ERRORES_INGLES)}</p>',
                    unsafe_allow_html=True)
    with e3:
        if st.button("Siguiente →", key="err_next", use_container_width=True):
            st.session_state.err_idx = (st.session_state.err_idx + 1) % len(ERRORES_INGLES)
            st.session_state.err_revealed = False
            st.rerun()

    st.markdown("---")
    st.markdown("**Categorías cubiertas:**")
    cats = list(dict.fromkeys(e["categoria"] for e in ERRORES_INGLES))
    cols = st.columns(3)
    for i, cat in enumerate(cats):
        cols[i % 3].markdown(f"• {cat}")


# ══════════════════════════════
#  TAB 6 — COMPRENSIÓN LECTORA
# ══════════════════════════════
with tab6:
    st.markdown('<div class="section-title">Comprensión lectora · Estilo DELE C1</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Lee el texto y responde las preguntas de opción múltiple. Las opciones están diseñadas para que debas leer con precisión.</div>', unsafe_allow_html=True)

    texto = TEXTOS_LECTURA[st.session_state.lect_idx]

    # Text selector
    tl1, tl2, tl3 = st.columns([1, 2, 1])
    with tl1:
        if st.button("← Texto anterior", key="lect_prev", use_container_width=True):
            st.session_state.lect_idx = (st.session_state.lect_idx - 1) % len(TEXTOS_LECTURA)
            st.session_state.lect_answers = {}
            st.session_state.lect_checked = False
            st.rerun()
    with tl2:
        st.markdown(f'<p style="text-align:center;font-weight:700;color:#064e3b;padding-top:0.4rem;">'
                    f'{texto["titulo"]} ({st.session_state.lect_idx + 1}/{len(TEXTOS_LECTURA)})</p>',
                    unsafe_allow_html=True)
    with tl3:
        if st.button("Texto siguiente →", key="lect_next", use_container_width=True):
            st.session_state.lect_idx = (st.session_state.lect_idx + 1) % len(TEXTOS_LECTURA)
            st.session_state.lect_answers = {}
            st.session_state.lect_checked = False
            st.rerun()

    # Text
    st.markdown(f'<div class="texto-lectura">{texto["texto"].replace(chr(10), "<br>")}</div>',
                unsafe_allow_html=True)
    st.caption(texto["fuente"])

    # Questions
    st.markdown("**Preguntas:**")
    for i, q in enumerate(texto["preguntas"]):
        st.markdown(f"**{i+1}.** {q['pregunta']}")
        sel = st.radio(
            label=f"Pregunta {i+1}",
            options=q["opciones"],
            label_visibility="collapsed",
            key=f"lect_{st.session_state.lect_idx}_q{i}",
        )
        st.session_state.lect_answers[i] = sel

        if st.session_state.lect_checked:
            if sel == q["respuesta"]:
                st.markdown(f'<div class="feedback-ok">✅ Correcto. {q["explicacion"]}</div>',
                            unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="feedback-bad">❌ Respuesta correcta: **{q["respuesta"]}**\n\n{q["explicacion"]}</div>',
                            unsafe_allow_html=True)
        st.markdown("")

    lb1, lb2, lb3 = st.columns(3)
    with lb1:
        if st.button("Comprobar todo ✓", key="lect_check", use_container_width=True):
            correct = sum(
                1 for i, q in enumerate(texto["preguntas"])
                if st.session_state.lect_answers.get(i) == q["respuesta"]
            )
            st.session_state.lect_score = correct
            st.session_state.lect_total = len(texto["preguntas"])
            st.session_state.lect_checked = True
            st.rerun()
    with lb2:
        if st.button("Reiniciar respuestas 🔄", key="lect_reset", use_container_width=True):
            st.session_state.lect_answers = {}
            st.session_state.lect_checked = False
            st.rerun()
    with lb3:
        pass

    if st.session_state.lect_checked:
        total = st.session_state.lect_total
        score = st.session_state.lect_score
        pct = int(score / total * 100) if total else 0
        color = "#065f46" if pct >= 75 else "#92400e" if pct >= 50 else "#991b1b"
        st.markdown(
            f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
            f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
            f'<span style="font-size:1.3rem;font-weight:700;color:{color};">{score}/{total}</span>'
            f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctas ({pct} %)</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
