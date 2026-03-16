
import random
import textwrap
import json
from typing import Dict, List, Optional
import streamlit as st

# ============================================================
# CATA - App de español C2 (verbos + preposición) — v2
# Nuevas funciones: repetición espaciada, ejercicios de nivel
# avanzado, verbos con doble preposición, feedback de IA
# Ejecutar: streamlit run cata_app_espanol_v2.py
# Requisitos: pip install streamlit
# ============================================================

# ─────────────────────────────────────────────
#  BASE DE DATOS  — verbos + preposición
# ─────────────────────────────────────────────

DATA: Dict[str, List[Dict]] = {
    "de": [
        {"verbo": "acordarse", "expresion": "acordarse de",
         "ejemplos": ["Siempre me acuerdo de ti por las mañanas.",
                      "Nunca se acuerda de cerrar la llave del gas."],
         "nivel": "B2"},
        {"verbo": "alegrarse", "expresion": "alegrarse de",
         "ejemplos": ["Me alegro enormemente de que hayas llegado sano.",
                      "Se alegró de que le dieran la beca."],
         "nivel": "B2"},
        {"verbo": "arrepentirse", "expresion": "arrepentirse de",
         "ejemplos": ["Se arrepintió amargamente de no haber dicho nada.",
                      "Nunca me arrepentiré de haber tomado esa decisión."],
         "nivel": "B2"},
        {"verbo": "cansarse", "expresion": "cansarse de",
         "ejemplos": ["Se cansa fácilmente de las conversaciones superficiales.",
                      "Me canso de explicar lo mismo una y otra vez."],
         "nivel": "B2"},
        {"verbo": "darse cuenta", "expresion": "darse cuenta de",
         "ejemplos": ["No se dio cuenta de la gravedad del asunto hasta demasiado tarde.",
                      "Me fui dando cuenta de que algo no encajaba."],
         "nivel": "B2"},
        {"verbo": "enamorarse", "expresion": "enamorarse de",
         "ejemplos": ["Se enamoró perdidamente de alguien a quien apenas conocía.",
                      "Me enamoré de esta ciudad a primera vista."],
         "nivel": "B2"},
        {"verbo": "olvidarse", "expresion": "olvidarse de",
         "ejemplos": ["Se olvidó por completo de la cita con el médico.",
                      "No te olvides de llamarme cuando llegues."],
         "nivel": "B2"},
        {"verbo": "encargarse", "expresion": "encargarse de",
         "ejemplos": ["Se encargó de todos los trámites burocráticos sin quejarse.",
                      "¿Quién se encarga de coordinar el proyecto?"],
         "nivel": "B2"},
        {"verbo": "disfrutar", "expresion": "disfrutar de",
         "ejemplos": ["Disfruta de cada pequeño momento sin pensar en el futuro.",
                      "Nunca ha sabido disfrutar de las cosas sencillas."],
         "nivel": "B2"},
        {"verbo": "tratar", "expresion": "tratar de",
         "ejemplos": ["Trata de no perder la calma aunque te resulte difícil.",
                      "Traté de explicarle la situación sin éxito."],
         "nivel": "B2"},
        {"verbo": "acabar", "expresion": "acabar de",
         "ejemplos": ["Acabo de leer un artículo que me ha dejado sin palabras.",
                      "Acababa de salir cuando sonó el teléfono."],
         "nivel": "B2"},
        {"verbo": "ocuparse", "expresion": "ocuparse de",
         "ejemplos": ["Se ocupa de los asuntos más delicados con una discreción admirable.",
                      "¿Alguien puede ocuparse de esta reclamación?"],
         "nivel": "B2"},
        {"verbo": "aburrirse", "expresion": "aburrirse de",
         "ejemplos": ["Se aburre rápidamente de las personas que no le plantean retos intelectuales.",
                      "Me aburrí de esperar y decidí marcharme."],
         "nivel": "B2"},
        {"verbo": "presumir", "expresion": "presumir de",
         "ejemplos": ["Presume de cultura pero rara vez lee un libro.",
                      "No hay que presumir de lo que no se tiene."],
         "nivel": "B2"},
        {"verbo": "tratarse", "expresion": "tratarse de",
         "ejemplos": ["Se trata de una cuestión de principios, no de intereses.",
                      "¿De qué se trata exactamente tu propuesta?"],
         "nivel": "B2"},
        # C1-C2 nuevos
        {"verbo": "abstenerse", "expresion": "abstenerse de",
         "ejemplos": ["Se abstuvo de comentar nada hasta conocer todos los detalles.",
                      "Le recomendaron que se abstuviera de hacer declaraciones públicas."],
         "nivel": "C1"},
        {"verbo": "desistir", "expresion": "desistir de",
         "ejemplos": ["Desistió de su empeño tras años de intentos fallidos.",
                      "No pienso desistir de mis objetivos por mucho que cueste."],
         "nivel": "C1"},
        {"verbo": "quejarse", "expresion": "quejarse de",
         "ejemplos": ["Se queja constantemente de la falta de reconocimiento.",
                      "No tiene motivo alguno de quejarse de su situación."],
         "nivel": "C1"},
        {"verbo": "prescindir", "expresion": "prescindir de",
         "ejemplos": ["La empresa decidió prescindir de varios directivos.",
                      "Es muy difícil prescindir de los hábitos arraigados."],
         "nivel": "C2"},
        {"verbo": "desprenderse", "expresion": "desprenderse de",
         "ejemplos": ["Le costó mucho desprenderse de aquella vieja costumbre.",
                      "De sus palabras se desprende una profunda tristeza."],
         "nivel": "C2"},
        {"verbo": "adolecer", "expresion": "adolecer de",
         "ejemplos": ["El informe adolece de una falta total de rigor metodológico.",
                      "Su discurso adolece de cierta superficialidad."],
         "nivel": "C2"},
        {"verbo": "jactarse", "expresion": "jactarse de",
         "ejemplos": ["Se jactaba de conocer a los personajes más influyentes del país.",
                      "No es de buen gusto jactarse de los propios logros."],
         "nivel": "C2"},
        {"verbo": "valerse", "expresion": "valerse de",
         "ejemplos": ["Se valió de sus contactos para conseguir el puesto.",
                      "Para lograrlo, se valió de todos los recursos disponibles."],
         "nivel": "C2"},
    ],
    "a": [
        {"verbo": "acostumbrarse", "expresion": "acostumbrarse a",
         "ejemplos": ["Me estoy acostumbrando a vivir con mucha menos comodidad.",
                      "Tardó años en acostumbrarse al ritmo de la ciudad."],
         "nivel": "B2"},
        {"verbo": "aprender", "expresion": "aprender a",
         "ejemplos": ["Está aprendiendo a gestionar la frustración de forma constructiva.",
                      "Aprendió a leer a los cinco años."],
         "nivel": "B2"},
        {"verbo": "ayudar", "expresion": "ayudar a",
         "ejemplos": ["¿Podrías ayudarme a revisar este texto antes de enviarlo?",
                      "La terapia le ayudó a superar ese período tan duro."],
         "nivel": "B2"},
        {"verbo": "empezar", "expresion": "empezar a",
         "ejemplos": ["Empezó a llover justo cuando salíamos.",
                      "Hoy mismo empiezo a tomar en serio mi salud."],
         "nivel": "B2"},
        {"verbo": "invitar", "expresion": "invitar a",
         "ejemplos": ["La invité a reflexionar sobre sus propias contradicciones.",
                      "Nos invitó a cenar en su nueva casa."],
         "nivel": "B2"},
        {"verbo": "volver", "expresion": "volver a",
         "ejemplos": ["No quiero volver a cometer el mismo error.",
                      "Volvió a llamar tres veces sin que nadie descolgara."],
         "nivel": "B2"},
        {"verbo": "animarse", "expresion": "animarse a",
         "ejemplos": ["Por fin se animó a pedir un aumento de sueldo.",
                      "Me animé a hablar en público y fue mejor de lo esperado."],
         "nivel": "B2"},
        {"verbo": "resistirse", "expresion": "resistirse a",
         "ejemplos": ["Se resiste a admitir que está equivocado.",
                      "Me resulta imposible resistirme a un buen libro."],
         "nivel": "B2"},
        {"verbo": "negarse", "expresion": "negarse a",
         "ejemplos": ["Se negó en redondo a firmar ese contrato.",
                      "Me niego a aceptar que no hay solución."],
         "nivel": "B2"},
        {"verbo": "aspirar", "expresion": "aspirar a",
         "ejemplos": ["Aspira a ocupar un puesto de mayor responsabilidad.",
                      "No aspira a la fama, sino al reconocimiento de sus iguales."],
         "nivel": "B2"},
        {"verbo": "decidirse", "expresion": "decidirse a",
         "ejemplos": ["Por fin se decidió a dar el paso que tanto temía.",
                      "¿Cuándo te vas a decidir a hablar con ella?"],
         "nivel": "B2"},
        {"verbo": "renunciar", "expresion": "renunciar a",
         "ejemplos": ["Renunció a su plaza para seguir un sueño incierto.",
                      "No estoy dispuesto a renunciar a mis convicciones."],
         "nivel": "B2"},
        # C1-C2 nuevos
        {"verbo": "atreverse", "expresion": "atreverse a",
         "ejemplos": ["Pocos se atreven a cuestionar abiertamente sus métodos.",
                      "Por fin se atrevió a decir en voz alta lo que todos pensaban."],
         "nivel": "C1"},
        {"verbo": "contribuir", "expresion": "contribuir a",
         "ejemplos": ["Sus investigaciones han contribuido a redefinir el campo.",
                      "Todos debemos contribuir a construir una sociedad más justa."],
         "nivel": "C1"},
        {"verbo": "comprometerse", "expresion": "comprometerse a",
         "ejemplos": ["Se comprometió formalmente a entregar el informe antes del viernes.",
                      "No me comprometo a nada sin leer antes las condiciones."],
         "nivel": "C1"},
        {"verbo": "oponerse", "expresion": "oponerse a",
         "ejemplos": ["Se opuso firmemente a cualquier tipo de censura.",
                      "¿Por qué te opones a explorar otras opciones?"],
         "nivel": "C1"},
        {"verbo": "propender", "expresion": "propender a",
         "ejemplos": ["Propende a ver el lado negativo de las cosas.",
                      "Este tipo de argumentación propende a la generalización excesiva."],
         "nivel": "C2"},
        {"verbo": "abocarse", "expresion": "abocarse a",
         "ejemplos": ["El proyecto se está abocando a un fracaso estrepitoso.",
                      "Con esas decisiones, se aboca a una crisis inevitable."],
         "nivel": "C2"},
    ],
    "con": [
        {"verbo": "soñar", "expresion": "soñar con",
         "ejemplos": ["Sueña con un mundo en el que la injusticia no exista.",
                      "Anoche soñé contigo y fue extrañísimo."],
         "nivel": "B2"},
        {"verbo": "contar", "expresion": "contar con",
         "ejemplos": ["Puedes contar conmigo para lo que necesites.",
                      "No contaba con que la situación se complicara tanto."],
         "nivel": "B2"},
        {"verbo": "enfadarse", "expresion": "enfadarse con",
         "ejemplos": ["Se enfadó conmigo por una tontería y no habló en tres días.",
                      "Es fácil enfadarse con los demás cuando uno está agotado."],
         "nivel": "B2"},
        {"verbo": "conformarse", "expresion": "conformarse con",
         "ejemplos": ["No se conforma con menos del cien por cien.",
                      "Se conformó con una respuesta vaga cuando merecía más."],
         "nivel": "B2"},
        {"verbo": "encontrarse", "expresion": "encontrarse con",
         "ejemplos": ["Me encontré con una situación que no había previsto en absoluto.",
                      "Se encontró con su ex en el aeropuerto, de todas las casualidades."],
         "nivel": "B2"},
        {"verbo": "toparse", "expresion": "toparse con",
         "ejemplos": ["Se topó con una resistencia que no esperaba.",
                      "Me topé con ese artículo por pura casualidad."],
         "nivel": "B2"},
        # C1-C2
        {"verbo": "comprometerse", "expresion": "comprometerse con",
         "ejemplos": ["Se comprometió de corazón con la causa medioambiental.",
                      "Hay que comprometerse con aquello en lo que se cree."],
         "nivel": "C1",
         "nota": "Comprometerse a + infinitivo (acción concreta) / comprometerse con + sustantivo (causa, persona)"},
        {"verbo": "indignarse", "expresion": "indignarse con",
         "ejemplos": ["Se indigna con cualquier forma de hipocresía.",
                      "Me indigné con su respuesta desdeñosa."],
         "nivel": "C1"},
        {"verbo": "compadecerse", "expresion": "compadecerse con",  # también "de"
         "ejemplos": ["Su versión de los hechos no se compadece con la realidad.",
                      "Esa afirmación no se compadece con los datos disponibles."],
         "nivel": "C2",
         "nota": "En este uso formal, 'compadecerse con' = ser coherente/compatible con"},
        {"verbo": "cebarse", "expresion": "cebarse con",
         "ejemplos": ["La crítica se cebó especialmente con su última novela.",
                      "La enfermedad se cebó con los más vulnerables."],
         "nivel": "C2"},
    ],
    "en": [
        {"verbo": "fijarse", "expresion": "fijarse en",
         "ejemplos": ["Fíjate bien en los matices antes de emitir un juicio.",
                      "Se fijó en un detalle que todos habían pasado por alto."],
         "nivel": "B2"},
        {"verbo": "pensar", "expresion": "pensar en",
         "ejemplos": ["Llevo días pensando en aquella conversación.",
                      "Antes de actuar, piensa en las consecuencias."],
         "nivel": "B2"},
        {"verbo": "tardar", "expresion": "tardar en",
         "ejemplos": ["No tardó en darse cuenta de que algo iba mal.",
                      "¿Cuánto tardarás en terminar?"],
         "nivel": "B2"},
        {"verbo": "insistir", "expresion": "insistir en",
         "ejemplos": ["Insiste en que no pasó nada, aunque las pruebas indican lo contrario.",
                      "No insistas en una idea cuando el contexto ya ha cambiado."],
         "nivel": "B2"},
        {"verbo": "consistir", "expresion": "consistir en",
         "ejemplos": ["El verdadero reto consiste en mantener la coherencia bajo presión.",
                      "¿En qué consiste exactamente tu propuesta?"],
         "nivel": "B2"},
        {"verbo": "convertirse", "expresion": "convertirse en",
         "ejemplos": ["Lo que empezó como un hobby se convirtió en su medio de vida.",
                      "Se convirtió en un referente del pensamiento crítico."],
         "nivel": "B2"},
        {"verbo": "confiar", "expresion": "confiar en",
         "ejemplos": ["Confía en tu criterio aunque los demás no lo compartan.",
                      "Tardé mucho en volver a confiar en alguien."],
         "nivel": "B2"},
        {"verbo": "influir", "expresion": "influir en",
         "ejemplos": ["El entorno influye de forma determinante en el desarrollo personal.",
                      "¿Quién ha influido más en tu manera de pensar?"],
         "nivel": "B2"},
        {"verbo": "participar", "expresion": "participar en",
         "ejemplos": ["Participó en el debate con argumentos sólidos y bien documentados.",
                      "Quiero participar en algo que tenga un impacto real."],
         "nivel": "B2"},
        # C1-C2
        {"verbo": "empeñarse", "expresion": "empeñarse en",
         "ejemplos": ["Se empeña en ver problemas donde no los hay.",
                      "Por más que me empeñé en convencerle, no lo logré."],
         "nivel": "C1"},
        {"verbo": "especializarse", "expresion": "especializarse en",
         "ejemplos": ["Decidió especializarse en derecho internacional.",
                      "La empresa se especializó en soluciones de ciberseguridad."],
         "nivel": "C1"},
        {"verbo": "redundar", "expresion": "redundar en",
         "ejemplos": ["Ese acuerdo redunda en beneficio de todas las partes.",
                      "Una buena formación redunda en mejores resultados."],
         "nivel": "C2"},
        {"verbo": "incidir", "expresion": "incidir en",
         "ejemplos": ["Quiero incidir en la importancia de este punto.",
                      "La política fiscal incide directamente en el bienestar social."],
         "nivel": "C2"},
        {"verbo": "ahondar", "expresion": "ahondar en",
         "ejemplos": ["El ensayo ahonda en las contradicciones del sistema.",
                      "No quiso ahondar en los detalles más dolorosos."],
         "nivel": "C2"},
    ],
    "por": [
        {"verbo": "preocuparse", "expresion": "preocuparse por",
         "ejemplos": ["Se preocupa por los demás antes que por sí mismo.",
                      "Me preocupa por el rumbo que está tomando todo esto."],
         "nivel": "B2"},
        {"verbo": "luchar", "expresion": "luchar por",
         "ejemplos": ["Lleva años luchando por un reconocimiento que se le niega.",
                      "Vale la pena luchar por lo que uno cree justo."],
         "nivel": "B2"},
        {"verbo": "esforzarse", "expresion": "esforzarse por",
         "ejemplos": ["Se esfuerza por entender puntos de vista distintos al suyo.",
                      "Me esforcé por no dejar traslucir mi incomodidad."],
         "nivel": "B2"},
        {"verbo": "interesarse", "expresion": "interesarse por",
         "ejemplos": ["Se interesa genuinamente por el bienestar de su equipo.",
                      "Nunca se había interesado por la política hasta ese momento."],
         "nivel": "B2"},
        {"verbo": "optar", "expresion": "optar por",
         "ejemplos": ["Optó por guardar silencio antes que decir algo de lo que arrepentirse.",
                      "Si tuviera que elegir, optaría por la segunda opción."],
         "nivel": "B2"},
        {"verbo": "disculparse", "expresion": "disculparse por",
         "ejemplos": ["Se disculpó por las molestias ocasionadas con una nota lacónica.",
                      "Nunca se disculpó por lo que dijo aquella noche."],
         "nivel": "B2"},
        {"verbo": "apostar", "expresion": "apostar por",
         "ejemplos": ["La directiva apostó por un perfil joven y sin experiencia previa.",
                      "Siempre he apostado por la honestidad, aunque salga caro."],
         "nivel": "B2"},
        # C1-C2
        {"verbo": "velar", "expresion": "velar por",
         "ejemplos": ["La institución debe velar por el interés general.",
                      "Como responsable, velo por que se cumplan todas las normas."],
         "nivel": "C1"},
        {"verbo": "abogar", "expresion": "abogar por",
         "ejemplos": ["Aboga por una reforma profunda del sistema educativo.",
                      "Su obra aboga por una reconciliación entre ciencia y humanismo."],
         "nivel": "C1"},
        {"verbo": "pujar", "expresion": "pujar por",
         "ejemplos": ["Varios coleccionistas pujaron por esa obra en la subasta.",
                      "Ambas empresas pugnan por hacerse con el contrato."],
         "nivel": "C2"},
        {"verbo": "clamor", "expresion": "clamar por",
         "ejemplos": ["La sociedad civil clamaba por justicia.",
                      "Clamaron por una respuesta que nunca llegó."],
         "nivel": "C2"},
    ],
}

# Verbos con doble preposición y cambio de significado
DOUBLE_PREP: List[Dict] = [
    {
        "verbo": "pensar",
        "casos": [
            {"prep": "en", "significado": "tener en mente, reflexionar",
             "ejemplo": "Pienso en ti constantemente."},
            {"prep": "de", "significado": "opinar, tener una valoración",
             "ejemplo": "¿Qué piensas de su última decisión?"},
        ]
    },
    {
        "verbo": "contar",
        "casos": [
            {"prep": "con", "significado": "tener disponible / confiar en alguien",
             "ejemplo": "Cuento contigo para el proyecto."},
            {"prep": "de", "significado": "hablar sobre algo (registro coloquial)",
             "ejemplo": "Cuéntame de tu viaje."},
        ]
    },
    {
        "verbo": "hablar",
        "casos": [
            {"prep": "de", "significado": "tratar un tema",
             "ejemplo": "Hablamos de política hasta las tantas."},
            {"prep": "con", "significado": "comunicarse con alguien",
             "ejemplo": "Ayer hablé con mi jefe y fue bien."},
        ]
    },
    {
        "verbo": "comprometerse",
        "casos": [
            {"prep": "a", "significado": "obligarse a una acción concreta",
             "ejemplo": "Me comprometí a entregar el informe el lunes."},
            {"prep": "con", "significado": "alinearse con una causa o persona",
             "ejemplo": "Se comprometió con la lucha contra el cambio climático."},
        ]
    },
    {
        "verbo": "tratar",
        "casos": [
            {"prep": "de", "significado": "intentar (+ infinitivo) / versar sobre",
             "ejemplo": "Trato de no perder la calma. / El libro trata de la memoria histórica."},
            {"prep": "con", "significado": "tener trato / relacionarse con",
             "ejemplo": "Trato con personas muy diversas en mi trabajo."},
        ]
    },
    {
        "verbo": "quedar",
        "casos": [
            {"prep": "en", "significado": "acordar algo",
             "ejemplo": "Quedamos en vernos el jueves a las siete."},
            {"prep": "con", "significado": "citarse con alguien",
             "ejemplo": "He quedado con Ana para tomar algo."},
        ]
    },
    {
        "verbo": "acabar",
        "casos": [
            {"prep": "de", "significado": "acción recién completada (perífrasis)",
             "ejemplo": "Acabo de leer tu correo."},
            {"prep": "con", "significado": "poner fin a algo/alguien",
             "ejemplo": "Hay que acabar con esta situación de una vez."},
            {"prep": "por", "significado": "terminar haciendo algo tras un proceso",
             "ejemplo": "Acabé por darle la razón aunque no quería."},
        ]
    },
]

# Ejercicios de hueco — frase con ___
GAP_EXERCISES: List[Dict] = [
    {"frase": "Llevaba años soñando ___ un lugar así y por fin lo ha encontrado.",
     "respuesta": "con", "verbo": "soñar con",
     "explicacion": "Soñar con + sustantivo/infinitivo expresa deseo o lo que aparece en sueños."},
    {"frase": "El nuevo plan adolece ___ una falta total de concreción.",
     "respuesta": "de", "verbo": "adolecer de",
     "explicacion": "Adolecer de significa carecer de algo o tener un defecto."},
    {"frase": "Se abstuvo ___ opinar hasta conocer todos los datos.",
     "respuesta": "de", "verbo": "abstenerse de",
     "explicacion": "Abstenerse de + infinitivo: contenerse de hacer algo."},
    {"frase": "La medida redunda ___ beneficio de los consumidores.",
     "respuesta": "en", "verbo": "redundar en",
     "explicacion": "Redundar en: tener como consecuencia, repercutir en."},
    {"frase": "Se valió ___ todos sus contactos para conseguir el contrato.",
     "respuesta": "de", "verbo": "valerse de",
     "explicacion": "Valerse de: aprovecharse de algo o alguien como medio."},
    {"frase": "La crítica se cebó especialmente ___ su segunda novela.",
     "respuesta": "con", "verbo": "cebarse con",
     "explicacion": "Cebarse con: ensañarse con alguien/algo de forma desproporcionada."},
    {"frase": "El documento ahonda ___ las causas estructurales de la crisis.",
     "respuesta": "en", "verbo": "ahondar en",
     "explicacion": "Ahondar en: profundizar, explorar con mayor detalle."},
    {"frase": "Por fin se atrevió ___ decir en público lo que todos pensaban.",
     "respuesta": "a", "verbo": "atreverse a",
     "explicacion": "Atreverse a + infinitivo: tener el valor de hacer algo."},
    {"frase": "Aboga ___ una reforma profunda del sistema de pensiones.",
     "respuesta": "por", "verbo": "abogar por",
     "explicacion": "Abogar por: defender una causa o idea públicamente."},
    {"frase": "Nunca había incidido tanto ___ la importancia del contexto.",
     "respuesta": "en", "verbo": "incidir en",
     "explicacion": "Incidir en: hacer hincapié en algo / influir en algo."},
    {"frase": "Se jactaba ___ conocer a los personajes más poderosos del país.",
     "respuesta": "de", "verbo": "jactarse de",
     "explicacion": "Jactarse de: presumir con arrogancia de algo."},
    {"frase": "La empresa decidió prescindir ___ varios altos cargos.",
     "respuesta": "de", "verbo": "prescindir de",
     "explicacion": "Prescindir de: renunciar a algo/alguien, considerarlo innecesario."},
    {"frase": "Me comprometí ___ revisar el informe antes del lunes.",
     "respuesta": "a", "verbo": "comprometerse a",
     "explicacion": "Comprometerse a + infinitivo: obligarse a realizar una acción concreta."},
    {"frase": "Se comprometió ___ la causa desde el primer día.",
     "respuesta": "con", "verbo": "comprometerse con",
     "explicacion": "Comprometerse con + sustantivo: alinearse, identificarse con algo."},
    {"frase": "Velar ___ el interés público es la función primordial del Estado.",
     "respuesta": "por", "verbo": "velar por",
     "explicacion": "Velar por: cuidar, proteger, garantizar algo."},
]

# Ejercicios de detección de error
ERROR_EXERCISES: List[Dict] = [
    {"frase_incorrecta": "Me arrepiento *con* no haber asistido a aquella conferencia.",
     "prep_incorrecta": "con", "prep_correcta": "de",
     "verbo": "arrepentirse de",
     "frase_correcta": "Me arrepiento de no haber asistido a aquella conferencia.",
     "explicacion": "Arrepentirse rige la preposición 'de', no 'con'."},
    {"frase_incorrecta": "El proyecto adolece *con* una falta de planificación evidente.",
     "prep_incorrecta": "con", "prep_correcta": "de",
     "verbo": "adolecer de",
     "frase_correcta": "El proyecto adolece de una falta de planificación evidente.",
     "explicacion": "Adolecer siempre va con 'de': adolecer de un defecto o carencia."},
    {"frase_incorrecta": "Se abstuvo *en* hacer declaraciones hasta conocer los hechos.",
     "prep_incorrecta": "en", "prep_correcta": "de",
     "verbo": "abstenerse de",
     "frase_correcta": "Se abstuvo de hacer declaraciones hasta conocer los hechos.",
     "explicacion": "Abstenerse lleva 'de', no 'en'."},
    {"frase_incorrecta": "Aboga *sobre* una mayor transparencia en la gestión pública.",
     "prep_incorrecta": "sobre", "prep_correcta": "por",
     "verbo": "abogar por",
     "frase_correcta": "Aboga por una mayor transparencia en la gestión pública.",
     "explicacion": "Abogar lleva 'por', no 'sobre'."},
    {"frase_incorrecta": "La medida redunda *para* beneficio de los ciudadanos más vulnerables.",
     "prep_incorrecta": "para", "prep_correcta": "en",
     "verbo": "redundar en",
     "frase_correcta": "La medida redunda en beneficio de los ciudadanos más vulnerables.",
     "explicacion": "Redundar lleva 'en': redundar en beneficio / en perjuicio de."},
    {"frase_incorrecta": "No pienso desistir *con* mis objetivos por muchos obstáculos que encuentre.",
     "prep_incorrecta": "con", "prep_correcta": "de",
     "verbo": "desistir de",
     "frase_correcta": "No pienso desistir de mis objetivos por muchos obstáculos que encuentre.",
     "explicacion": "Desistir lleva 'de': desistir de un empeño, una idea, un plan."},
    {"frase_incorrecta": "Se cebó *sobre* los más débiles sin ningún tipo de escrúpulos.",
     "prep_incorrecta": "sobre", "prep_correcta": "con",
     "verbo": "cebarse con",
     "frase_correcta": "Se cebó con los más débiles sin ningún tipo de escrúpulos.",
     "explicacion": "Cebarse lleva 'con': cebarse con alguien significa ensañarse con él."},
    {"frase_incorrecta": "Insto *sobre* todos los presentes a reflexionar sobre sus responsabilidades.",
     "prep_incorrecta": "sobre", "prep_correcta": "a",
     "verbo": "instar a",
     "frase_correcta": "Insto a todos los presentes a reflexionar sobre sus responsabilidades.",
     "explicacion": "Instar lleva 'a': instar a alguien a hacer algo."},
]

PREPS = ["de", "a", "con", "en", "por"]
CATEGORY_LABELS = {
    "de": "Verbos + DE",
    "a": "Verbos + A",
    "con": "Verbos + CON",
    "en": "Verbos + EN",
    "por": "Verbos + POR",
}

NIVEL_COLORS = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Cata Español C2",
    page_icon="🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400;700&display=swap');

    html, body, [class*="css"] { font-family: 'Lato', sans-serif; }

    .block-container { padding-top: 1.2rem; padding-bottom: 2rem; max-width: 1300px; }

    .hero {
        background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);
        border-radius: 20px;
        padding: 1.8rem 2rem;
        margin-bottom: 1.2rem;
        color: white;
    }
    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        margin: 0 0 0.3rem 0;
        color: white;
    }
    .hero p { margin: 0; color: #c7d2fe; font-size: 0.95rem; }

    .metric-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 0.85rem 1rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .metric-value { font-size: 1.6rem; font-weight: 700; color: #1e1b4b; }
    .metric-label { font-size: 0.82rem; color: #6b7280; margin-top: 0.15rem; }

    .card-box {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.3rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    }
    .card-chip {
        display: inline-block;
        background: #ede9fe;
        color: #4c1d95;
        border-radius: 999px;
        padding: 0.3rem 0.75rem;
        font-size: 0.82rem;
        font-weight: 700;
        margin-bottom: 0.75rem;
    }
    .nivel-badge {
        display: inline-block;
        border-radius: 999px;
        padding: 0.2rem 0.6rem;
        font-size: 0.78rem;
        font-weight: 700;
        color: white;
        margin-left: 0.5rem;
    }
    .card-title {
        color: #312e81;
        font-size: 1.7rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
        font-family: 'Playfair Display', serif;
    }
    .card-line { color: #374151; margin-bottom: 0.4rem; font-size: 0.97rem; }
    .example-block {
        background: #f5f3ff;
        border-left: 3px solid #7c3aed;
        border-radius: 0 10px 10px 0;
        padding: 0.55rem 0.9rem;
        margin: 0.35rem 0;
        font-style: italic;
        color: #3730a3;
        font-size: 0.93rem;
    }
    .nota-box {
        background: #fef3c7;
        border: 1px solid #fcd34d;
        border-radius: 10px;
        padding: 0.55rem 0.9rem;
        font-size: 0.88rem;
        color: #78350f;
        margin-top: 0.6rem;
    }

    .quiz-box {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1.3rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1e1b4b;
        margin-bottom: 0.2rem;
        font-family: 'Playfair Display', serif;
    }
    .section-sub { color: #6b7280; margin-bottom: 0.8rem; font-size: 0.9rem; }

    .feedback-ok {
        background: #ecfdf5; border: 1px solid #6ee7b7; color: #065f46;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem;
        white-space: pre-wrap; font-size: 0.93rem;
    }
    .feedback-bad {
        background: #fef2f2; border: 1px solid #fca5a5; color: #7f1d1d;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem;
        white-space: pre-wrap; font-size: 0.93rem;
    }
    .feedback-neutral {
        background: #f8fafc; border: 1px solid #e2e8f0; color: #334155;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem;
        white-space: pre-wrap; font-size: 0.93rem;
    }
    .feedback-ai {
        background: #f0f4ff; border: 1px solid #818cf8; color: #1e1b4b;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem;
        white-space: pre-wrap; font-size: 0.93rem;
    }

    .double-prep-card {
        background: #fefce8;
        border: 1px solid #fde68a;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .dp-verb { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #78350f; font-weight: 700; }
    .dp-row { margin: 0.45rem 0; }
    .dp-prep { display: inline-block; background: #fef3c7; color: #78350f; border-radius: 6px; padding: 0.15rem 0.45rem; font-weight: 700; font-size: 0.88rem; }
    .dp-sig { color: #374151; font-size: 0.9rem; }
    .dp-ex { color: #78350f; font-style: italic; font-size: 0.87rem; margin-top: 0.1rem; }

    .weak-tag { background: #fee2e2; color: #991b1b; border-radius: 6px; padding: 0.15rem 0.5rem; font-size: 0.78rem; font-weight: 700; }

    .tab-header { font-family: 'Playfair Display', serif; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  STATE
# ─────────────────────────────────────────────

def init_state():
    all_items: List[Dict] = []
    for prep, items in DATA.items():
        for item in items:
            enriched = dict(item)
            enriched["prep"] = prep
            all_items.append(enriched)

    defaults = {
        "all_items": all_items,
        "filtered_items": list(all_items),
        "current_card_index": 0,
        "quiz_score": 0,
        "quiz_total": 0,
        "quiz_streak": 0,
        "feedback": ("neutral", "Elige categorías y empieza a practicar ✨"),
        "quiz_data": None,
        "study_mode": "Elegir preposición",
        "weak_items": {},           # verbo_expresion -> fail_count
        "gap_index": None,
        "gap_feedback": None,
        "error_index": None,
        "error_feedback": None,
        "ai_feedback": None,
        "double_prep_index": 0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def active_items(selected_preps: List[str]) -> List[Dict]:
    base = [i for i in st.session_state.all_items if i["prep"] in selected_preps]
    # mezcla ponderada: los débiles aparecen el doble
    weighted = []
    for item in base:
        key = item["expresion"]
        fails = st.session_state.weak_items.get(key, 0)
        weighted.append(item)
        if fails >= 2:
            weighted.append(item)  # doble probabilidad si ≥2 fallos
    return base, weighted  # base para navegación, weighted para quiz


def set_feedback(kind: str, message: str):
    st.session_state.feedback = (kind, message)


def show_feedback():
    kind, message = st.session_state.feedback
    css = {"ok": "feedback-ok", "bad": "feedback-bad",
           "neutral": "feedback-neutral", "ai": "feedback-ai"}.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{message}</div>', unsafe_allow_html=True)


def register_fail(item: Dict):
    key = item["expresion"]
    st.session_state.weak_items[key] = st.session_state.weak_items.get(key, 0) + 1


def register_ok(item: Dict):
    key = item["expresion"]
    if key in st.session_state.weak_items and st.session_state.weak_items[key] > 0:
        st.session_state.weak_items[key] -= 1


# ─────────────────────────────────────────────
#  QUIZ GENERATOR
# ─────────────────────────────────────────────

def new_quiz_question(items: List[Dict], weighted: List[Dict], mode: str):
    if not items:
        st.session_state.quiz_data = None
        return

    chosen_mode = mode if mode != "Mixto" else random.choice([
        "Elegir preposición", "Completar expresión", "Ejemplo correcto"])

    item = random.choice(weighted if weighted else items)

    if chosen_mode == "Elegir preposición":
        options = PREPS[:]
        random.shuffle(options)
        st.session_state.quiz_data = {
            "type": chosen_mode, "item": item,
            "question": f"¿Qué preposición completa correctamente esta estructura?\n\n**{item['verbo']} + ___**",
            "answer": item["prep"], "options": options,
        }
        return

    if chosen_mode == "Completar expresión":
        ejemplo = random.choice(item["ejemplos"])
        st.session_state.quiz_data = {
            "type": chosen_mode, "item": item,
            "question": f"Escribe la expresión completa (verbo + preposición).\n\n**Contexto:** {ejemplo}",
            "answer": item["expresion"], "options": None,
        }
        return

    # Ejemplo correcto
    wrong_pool = []
    for other in items:
        if other["expresion"] != item["expresion"]:
            wrong_pool.extend(other["ejemplos"])
    wrong_options = random.sample(wrong_pool, k=min(3, len(wrong_pool))) if wrong_pool else []
    correct_option = random.choice(item["ejemplos"])
    options = wrong_options + [correct_option]
    random.shuffle(options)
    st.session_state.quiz_data = {
        "type": chosen_mode, "item": item,
        "question": f"Selecciona el ejemplo que corresponde a:\n\n**{item['expresion']}**",
        "answer": correct_option, "options": options,
    }


def check_answer(user_answer: str):
    quiz = st.session_state.quiz_data
    if not quiz:
        set_feedback("neutral", "No hay pregunta activa.")
        return
    if not user_answer.strip():
        set_feedback("bad", "Escribe o selecciona una respuesta antes de comprobar.")
        return

    correct = normalize(user_answer) == normalize(quiz["answer"])
    st.session_state.quiz_total += 1

    if correct:
        st.session_state.quiz_score += 1
        st.session_state.quiz_streak += 1
        register_ok(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        set_feedback("ok", f"✅ Correcto.\n\nEjemplo: {ejemplo}{nota}")
    else:
        st.session_state.quiz_streak = 0
        register_fail(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        set_feedback("bad",
                     f"❌ Respuesta correcta: **{quiz['answer']}**\n\nEjemplo: {ejemplo}{nota}")


# ─────────────────────────────────────────────
#  LLAMADA A CLAUDE (AI FEEDBACK)
# ─────────────────────────────────────────────

async def get_ai_feedback_async(verbo_expr: str, frase_usuario: str) -> str:
    """Obtiene feedback de Claude para un ejercicio de escritura libre."""
    import aiohttp
    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 350,
        "messages": [
            {"role": "user", "content": (
                f"Eres un profesor de español de nivel C2 experto en gramática. "
                f"El alumno debe escribir una frase usando la expresión '{verbo_expr}'. "
                f"Frase del alumno: «{frase_usuario}»\n\n"
                f"Evalúa brevemente (máximo 4 líneas):\n"
                f"1. ¿Usa correctamente la preposición y la estructura?\n"
                f"2. ¿Es natural y fluida para un hablante nativo?\n"
                f"3. Una sugerencia de mejora si la hay.\n"
                f"Responde SIEMPRE en español, de forma directa y constructiva."
            )}
        ]
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.anthropic.com/v1/messages",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=aiohttp.ClientTimeout(total=20)
            ) as resp:
                data = await resp.json()
                return data["content"][0]["text"]
    except Exception as e:
        return f"No se pudo conectar con la IA: {e}"


def call_claude_feedback(verbo_expr: str, frase_usuario: str) -> str:
    import asyncio
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                future = pool.submit(asyncio.run, get_ai_feedback_async(verbo_expr, frase_usuario))
                return future.result(timeout=25)
        else:
            return loop.run_until_complete(get_ai_feedback_async(verbo_expr, frase_usuario))
    except Exception as e:
        return f"Error al obtener feedback: {e}"


# ─────────────────────────────────────────────
#  MAIN RENDER
# ─────────────────────────────────────────────

init_state()

st.markdown("""
<div class="hero">
    <h1>🇪🇸 Cata Español — Nivel C2</h1>
    <p>Verbos + preposición · Ejercicios de hueco · Detección de errores · Doble preposición · Feedback de IA</p>
</div>
""", unsafe_allow_html=True)

# ── SIDEBAR ──
with st.sidebar:
    st.markdown("### ⚙️ Panel de estudio")
    selected_preps: List[str] = []
    for prep in PREPS:
        n = len(DATA[prep])
        if st.checkbox(f"{CATEGORY_LABELS[prep]} ({n})", value=True, key=f"prep_{prep}"):
            selected_preps.append(prep)

    base_items, weighted_items = active_items(selected_preps)
    st.session_state.filtered_items = base_items

    st.markdown("---")
    nivel_filter = st.multiselect("🎓 Nivel", ["B2", "C1", "C2"], default=["B2", "C1", "C2"])
    base_items = [i for i in base_items if i.get("nivel", "B2") in nivel_filter]
    weighted_items = [i for i in weighted_items if i.get("nivel", "B2") in nivel_filter]

    st.markdown("---")
    mode = st.selectbox(
        "🎯 Tipo de quiz",
        ["Elegir preposición", "Completar expresión", "Ejemplo correcto", "Mixto"],
        index=0,
    )
    st.session_state.study_mode = mode

    st.markdown("---")
    # Verbos débiles
    n_weak = len([v for v, c in st.session_state.weak_items.items() if c >= 2])
    if n_weak:
        st.markdown(f'<span class="weak-tag">⚠️ {n_weak} verbo(s) con ≥2 fallos → aparecen más en el quiz</span>', unsafe_allow_html=True)
        if st.button("Reiniciar repetición espaciada"):
            st.session_state.weak_items = {}
            st.rerun()
    else:
        st.caption("Sin verbos marcados como débiles aún.")

    st.markdown("---")
    st.info("Recorre primero las tarjetas, luego practica con el quiz y los ejercicios avanzados.")

items = base_items

if not items:
    st.warning("Activa al menos una categoría / nivel para empezar.")
    st.stop()

if st.session_state.current_card_index >= len(items):
    st.session_state.current_card_index = 0

# Métricas
progress_ratio = st.session_state.quiz_score / st.session_state.quiz_total if st.session_state.quiz_total else 0.0
m1, m2, m3, m4, m5 = st.columns(5)
for col, val, label in [
    (m1, len(items), "verbos activos"),
    (m2, st.session_state.quiz_score, "aciertos"),
    (m3, st.session_state.quiz_total, "intentos"),
    (m4, st.session_state.quiz_streak, "racha"),
    (m5, f"{int(progress_ratio*100)}%", "precisión"),
]:
    col.markdown(f'<div class="metric-card"><div class="metric-value">{val}</div><div class="metric-label">{label}</div></div>', unsafe_allow_html=True)

st.progress(progress_ratio)
st.markdown("<br>", unsafe_allow_html=True)

# ── TABS ──
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📚 Tarjetas",
    "🧠 Quiz",
    "✍️ Rellena el hueco",
    "🔍 Detecta el error",
    "🔀 Doble preposición",
])

# ────────────────────────────────
#  TAB 1 — TARJETAS
# ────────────────────────────────
with tab1:
    st.markdown('<div class="section-title">Explorador de tarjetas</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Estudia la estructura, preposición y ejemplos de cada verbo.</div>', unsafe_allow_html=True)

    current_item = items[st.session_state.current_card_index]
    nivel = current_item.get("nivel", "B2")
    nivel_color = NIVEL_COLORS.get(nivel, "#6b7280")

    st.markdown(f"""
    <div class="card-box">
        <div>
            <span class="card-chip">{CATEGORY_LABELS[current_item['prep']]}</span>
            <span class="nivel-badge" style="background:{nivel_color};">{nivel}</span>
        </div>
        <div class="card-title">{current_item['expresion']}</div>
        <div class="card-line"><strong>Verbo base:</strong> {current_item['verbo']}</div>
        <div class="card-line"><strong>Preposición:</strong> {current_item['prep']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**Ejemplos:**")
    for ej in current_item["ejemplos"]:
        st.markdown(f'<div class="example-block">{ej}</div>', unsafe_allow_html=True)

    if "nota" in current_item:
        st.markdown(f'<div class="nota-box">💡 <strong>Nota:</strong> {current_item["nota"]}</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("← Anterior", use_container_width=True):
            st.session_state.current_card_index = (st.session_state.current_card_index - 1) % len(items)
            st.rerun()
    with c2:
        if st.button("Siguiente →", use_container_width=True):
            st.session_state.current_card_index = (st.session_state.current_card_index + 1) % len(items)
            st.rerun()
    with c3:
        if st.button("Aleatoria 🎲", use_container_width=True):
            st.session_state.current_card_index = random.randrange(len(items))
            st.rerun()
    with c4:
        if st.button("Mezclar 🔀", use_container_width=True):
            shuffled = items[:]
            random.shuffle(shuffled)
            st.session_state.filtered_items = shuffled
            st.session_state.current_card_index = 0
            st.rerun()

    st.caption(f"Tarjeta {st.session_state.current_card_index + 1} de {len(items)}")

# ────────────────────────────────
#  TAB 2 — QUIZ
# ────────────────────────────────
with tab2:
    col_quiz, col_free = st.columns([1.1, 0.9], gap="large")

    with col_quiz:
        st.markdown('<div class="section-title">Quiz dinámico</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Los verbos con más fallos aparecen con mayor frecuencia.</div>', unsafe_allow_html=True)

        if st.session_state.quiz_data is None:
            new_quiz_question(items, weighted_items, st.session_state.study_mode)

        quiz = st.session_state.quiz_data
        if quiz and quiz["item"] in items:
            st.markdown('<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(quiz["question"])

            user_answer = ""
            if quiz["type"] in ["Elegir preposición", "Ejemplo correcto"]:
                display_opts = []
                for opt in quiz["options"]:
                    display_opts.append("\n".join(textwrap.wrap(opt, width=54))
                                       if quiz["type"] == "Ejemplo correcto" else opt)
                sel = st.radio("Selecciona", display_opts, key=f"r_{quiz['question'][:30]}")
                if quiz["type"] == "Ejemplo correcto":
                    user_answer = dict(zip(display_opts, quiz["options"])).get(sel, sel)
                else:
                    user_answer = sel
            else:
                user_answer = st.text_input("Tu respuesta", placeholder="Ej: acordarse de",
                                            key=f"i_{quiz['question'][:30]}")

            q1, q2, q3 = st.columns(3)
            with q1:
                if st.button("Comprobar ✓", use_container_width=True):
                    check_answer(user_answer)
                    st.rerun()
            with q2:
                if st.button("Ver solución 👁", use_container_width=True):
                    set_feedback("neutral", f"Solución: {quiz['answer']}\n\nEjemplo: {random.choice(quiz['item']['ejemplos'])}")
                    st.rerun()
            with q3:
                if st.button("Nueva →", use_container_width=True):
                    new_quiz_question(items, weighted_items, st.session_state.study_mode)
                    set_feedback("neutral", "Nueva pregunta cargada.")
                    st.rerun()

            if st.button("Reiniciar marcador", use_container_width=True):
                st.session_state.quiz_score = 0
                st.session_state.quiz_total = 0
                st.session_state.quiz_streak = 0
                set_feedback("neutral", "Marcador reiniciado.")
                st.rerun()

            show_feedback()
            st.markdown('</div>', unsafe_allow_html=True)

    with col_free:
        st.markdown('<div class="section-title">✍️ Escritura libre + IA</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Escribe tu propia frase y recibe feedback de Claude.</div>', unsafe_allow_html=True)

        rand_item = random.choice(items)
        if "free_write_item" not in st.session_state:
            st.session_state.free_write_item = rand_item

        fw_item = st.session_state.free_write_item
        nivel_color_fw = NIVEL_COLORS.get(fw_item.get("nivel", "B2"), "#6b7280")

        st.markdown(f"""
        <div class="quiz-box">
            <div>
                <span class="card-chip" style="background:#ede9fe;color:#4c1d95;">{fw_item['expresion']}</span>
                <span class="nivel-badge" style="background:{nivel_color_fw};">{fw_item.get('nivel','B2')}</span>
            </div>
            <p style="color:#374151;font-size:0.92rem;margin-top:0.5rem;">
                Escribe una frase original usando <strong>{fw_item['expresion']}</strong>.
                Procura que sea natural y de nivel C2.
            </p>
        </div>
        """, unsafe_allow_html=True)

        user_frase = st.text_area("Tu frase:", height=80, key="free_frase",
                                  placeholder=f"Ej: {random.choice(fw_item['ejemplos'])}")

        fw1, fw2 = st.columns(2)
        with fw1:
            if st.button("Pedir feedback a IA 🤖", use_container_width=True):
                if user_frase.strip():
                    with st.spinner("Claude está evaluando tu frase…"):
                        fb = call_claude_feedback(fw_item["expresion"], user_frase.strip())
                    st.session_state.ai_feedback = fb
                else:
                    st.session_state.ai_feedback = "⚠️ Escribe una frase primero."
                st.rerun()
        with fw2:
            if st.button("Cambiar verbo 🔄", use_container_width=True):
                st.session_state.free_write_item = random.choice(items)
                st.session_state.ai_feedback = None
                st.rerun()

        if st.session_state.ai_feedback:
            st.markdown(f'<div class="feedback-ai">🤖 <strong>Feedback de IA:</strong>\n\n{st.session_state.ai_feedback}</div>',
                        unsafe_allow_html=True)

# ────────────────────────────────
#  TAB 3 — RELLENA EL HUECO
# ────────────────────────────────
with tab3:
    st.markdown('<div class="section-title">Rellena el hueco</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Escribe la preposición que falta en cada frase de nivel C1–C2.</div>', unsafe_allow_html=True)

    if st.session_state.gap_index is None:
        st.session_state.gap_index = random.randrange(len(GAP_EXERCISES))

    gap = GAP_EXERCISES[st.session_state.gap_index]
    frase_display = gap["frase"].replace("___", "**___**")

    st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_display}</p></div>', unsafe_allow_html=True)
    st.caption(f"Verbo de referencia: *{gap['verbo']}*")

    gap_ans = st.text_input("Preposición:", placeholder="de / a / con / en / por",
                            key=f"gap_{st.session_state.gap_index}")

    g1, g2, g3 = st.columns(3)
    with g1:
        if st.button("Comprobar ✓", key="gap_check", use_container_width=True):
            if normalize(gap_ans) == normalize(gap["respuesta"]):
                st.session_state.gap_feedback = ("ok", f"✅ Correcto: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
            else:
                st.session_state.gap_feedback = ("bad", f"❌ Respuesta correcta: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
            st.rerun()
    with g2:
        if st.button("Solución 👁", key="gap_sol", use_container_width=True):
            st.session_state.gap_feedback = ("neutral", f"Preposición: **{gap['respuesta']}**\n\n💡 {gap['explicacion']}")
            st.rerun()
    with g3:
        if st.button("Nueva frase →", key="gap_next", use_container_width=True):
            st.session_state.gap_index = random.randrange(len(GAP_EXERCISES))
            st.session_state.gap_feedback = None
            st.rerun()

    if st.session_state.gap_feedback:
        kind, msg = st.session_state.gap_feedback
        css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

# ────────────────────────────────
#  TAB 4 — DETECTA EL ERROR
# ────────────────────────────────
with tab4:
    st.markdown('<div class="section-title">Detecta el error</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Cada frase tiene una preposición incorrecta (marcada con *). Escribe la correcta.</div>', unsafe_allow_html=True)

    if st.session_state.error_index is None:
        st.session_state.error_index = random.randrange(len(ERROR_EXERCISES))

    err = ERROR_EXERCISES[st.session_state.error_index]
    frase_display_err = err["frase_incorrecta"].replace(
        f"*{err['prep_incorrecta']}*",
        f'<span style="background:#fee2e2;color:#991b1b;padding:0 4px;border-radius:4px;font-weight:700;">*{err["prep_incorrecta"]}*</span>'
    )

    st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_display_err}</p></div>', unsafe_allow_html=True)
    st.caption(f"Verbo involucrado: *{err['verbo']}*")

    err_ans = st.text_input("Preposición correcta:", placeholder="de / a / con / en / por",
                            key=f"err_{st.session_state.error_index}")

    e1, e2, e3 = st.columns(3)
    with e1:
        if st.button("Comprobar ✓", key="err_check", use_container_width=True):
            if normalize(err_ans) == normalize(err["prep_correcta"]):
                st.session_state.error_feedback = ("ok",
                    f"✅ Correcto: **{err['prep_correcta']}**\n\n"
                    f"Frase corregida: {err['frase_correcta']}\n\n"
                    f"💡 {err['explicacion']}")
            else:
                st.session_state.error_feedback = ("bad",
                    f"❌ La preposición correcta es: **{err['prep_correcta']}**\n\n"
                    f"Frase corregida: {err['frase_correcta']}\n\n"
                    f"💡 {err['explicacion']}")
            st.rerun()
    with e2:
        if st.button("Solución 👁", key="err_sol", use_container_width=True):
            st.session_state.error_feedback = ("neutral",
                f"Correcta: **{err['prep_correcta']}**\n\n"
                f"{err['frase_correcta']}\n\n💡 {err['explicacion']}")
            st.rerun()
    with e3:
        if st.button("Nueva frase →", key="err_next", use_container_width=True):
            st.session_state.error_index = random.randrange(len(ERROR_EXERCISES))
            st.session_state.error_feedback = None
            st.rerun()

    if st.session_state.error_feedback:
        kind, msg = st.session_state.error_feedback
        css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
        st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

# ────────────────────────────────
#  TAB 5 — DOBLE PREPOSICIÓN
# ────────────────────────────────
with tab5:
    st.markdown('<div class="section-title">Verbos con doble preposición</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Verbos que cambian de significado según la preposición. Fundamental para el C2.</div>', unsafe_allow_html=True)

    for dp in DOUBLE_PREP:
        casos_html = ""
        for caso in dp["casos"]:
            casos_html += f"""
            <div class="dp-row">
                <span class="dp-prep">+ {caso['prep']}</span>
                <span class="dp-sig"> → {caso['significado']}</span>
                <div class="dp-ex">&ldquo;{caso['ejemplo']}&rdquo;</div>
            </div>"""
        st.markdown(f"""
        <div class="double-prep-card">
            <div class="dp-verb">{dp['verbo']}</div>
            {casos_html}
        </div>
        """, unsafe_allow_html=True)
