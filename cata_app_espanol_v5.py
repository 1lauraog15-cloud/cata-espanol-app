import random
import textwrap
import json
from typing import Dict, List, Optional
import streamlit as st

# ============================================================
# CATA — App de español C2 · v5
# Módulo 1: Verbos + preposición (162 verbos, 11 preposiciones)
# Módulo 2: Conectores del discurso (50 conectores)
# Ejecutar: streamlit run cata_app_espanol_v5.py
# Requisitos: pip install streamlit aiohttp
# ============================================================

DATA: Dict[str, List[Dict]] = {

    # ══════════════════════════════════════════
    #  + DE
    # ══════════════════════════════════════════
    "de": [
        {"verbo": "acordarse", "expresion": "acordarse de",
         "ejemplos": [
             "Siempre me acuerdo de ti cuando paso por ese barrio.",
             "¿Te has acordado de apagar el horno antes de salir?",
             "Me alegra que te hayas acordado de llamarla; llevaba días esperando.",
             "Ojalá se hubiera acordado de traer los documentos.",
         ], "nivel": "B2"},

        {"verbo": "alegrarse", "expresion": "alegrarse de",
         "ejemplos": [
             "Me alegro muchísimo de que hayas encontrado trabajo.",
             "Se alegró de que le concedieran la beca sin apenas trámites.",
             "Nos hemos alegrado de verte tan recuperada.",
             "Es una noticia de la que todos deberíamos alegrarnos.",
         ], "nivel": "B2"},

        {"verbo": "arrepentirse", "expresion": "arrepentirse de",
         "ejemplos": [
             "Se arrepintió amargamente de no haber dicho nada en su momento.",
             "Me arrepiento de que la conversación acabara así.",
             "Nunca me he arrepentido de haber tomado esa decisión tan arriesgada.",
             "Si no actúas ahora, te arrepentirás de haberlo dejado pasar.",
         ], "nivel": "B2"},

        {"verbo": "cansarse", "expresion": "cansarse de",
         "ejemplos": [
             "Se cansa fácilmente de las personas que no le plantean retos intelectuales.",
             "Me he cansado de repetir lo mismo sin que nadie escuche.",
             "Cuando te canses de esperar, avísame y buscamos otra solución.",
             "Llevaba meses cansándose de una rutina que ya no tenía sentido.",
         ], "nivel": "B2"},

        {"verbo": "darse cuenta", "expresion": "darse cuenta de",
         "ejemplos": [
             "No se dio cuenta de la gravedad del asunto hasta que fue demasiado tarde.",
             "Me fui dando cuenta de que algo no encajaba en su versión.",
             "¿Te has dado cuenta de que lleva tres días sin contestar?",
             "Ojalá se hubiera dado cuenta de ello antes de tomar esa decisión.",
         ], "nivel": "B2"},

        {"verbo": "enamorarse", "expresion": "enamorarse de",
         "ejemplos": [
             "Se enamoró perdidamente de alguien a quien apenas conocía.",
             "Me he enamorado de esta ciudad desde el primer día.",
             "Es difícil no enamorarse de un lugar que te trata con tanta generosidad.",
             "Se habían enamorado de la misma idea sin saberlo.",
         ], "nivel": "B2"},

        {"verbo": "olvidarse", "expresion": "olvidarse de",
         "ejemplos": [
             "Se olvidó por completo de la cita con el médico.",
             "No te olvides de que mañana es el plazo límite.",
             "Me he olvidado de adjuntar el archivo; lo reenvío ahora.",
             "Sería imperdonable que nos olvidáramos de quienes más lo necesitan.",
         ], "nivel": "B2"},

        {"verbo": "encargarse", "expresion": "encargarse de",
         "ejemplos": [
             "Se encargó de todos los trámites burocráticos sin quejarse.",
             "¿Quién se ha encargado de coordinar el proyecto esta semana?",
             "Quiero que alguien se encargue de revisar cada línea antes de publicar.",
             "Se había encargado de que todo estuviera listo mucho antes de lo previsto.",
         ], "nivel": "B2"},

        {"verbo": "disfrutar", "expresion": "disfrutar de",
         "ejemplos": [
             "Disfruta de cada pequeño momento sin pensar constantemente en el futuro.",
             "Nunca ha sabido disfrutar de las cosas sencillas que tiene delante.",
             "Espero que hayas disfrutado de las vacaciones tanto como mereces.",
             "Para que disfruten de la experiencia, conviene que lleguen descansados.",
         ], "nivel": "B2"},

        {"verbo": "tratar", "expresion": "tratar de",
         "ejemplos": [
             "Trata de no perder la calma aunque la situación sea muy difícil.",
             "He tratado de explicarle la situación varias veces sin éxito.",
             "Traté de que comprendiera mi posición, pero no quiso escuchar.",
             "Por más que trate de concentrarse, el ruido le impide avanzar.",
         ], "nivel": "B2",
         "nota": "Tratar de + infinitivo = intentar. Tratar con + sustantivo = relacionarse con alguien."},

        {"verbo": "acabar", "expresion": "acabar de",
         "ejemplos": [
             "Acabo de leer un artículo que me ha dejado sin palabras.",
             "Acababa de salir cuando sonó el teléfono con la noticia.",
             "Cuando acabes de revisar el informe, mándamelo al correo.",
             "Acaban de confirmar que el proyecto ha sido aprobado.",
         ], "nivel": "B2",
         "nota": "Acabar de + infinitivo = acción recién completada. Acabar con = poner fin a algo."},

        {"verbo": "ocuparse", "expresion": "ocuparse de",
         "ejemplos": [
             "Se ocupa de los asuntos más delicados con una discreción admirable.",
             "¿Alguien se ha ocupado ya de esta reclamación?",
             "Necesito que alguien se ocupe de coordinar los turnos esta semana.",
             "Se había ocupado de todo sin pedir nada a cambio.",
         ], "nivel": "B2"},

        {"verbo": "aburrirse", "expresion": "aburrirse de",
         "ejemplos": [
             "Se aburre rápidamente de cualquier cosa que no le suponga un reto real.",
             "Me he aburrido de hacer siempre lo mismo en el mismo sitio.",
             "Cuando te aburras de esperar, dímelo y buscamos otra alternativa.",
             "Llevaba meses aburriéndose de una rutina que no le aportaba nada.",
         ], "nivel": "B2"},

        {"verbo": "presumir", "expresion": "presumir de",
         "ejemplos": [
             "Presume de cultura pero rara vez abre un libro.",
             "Ha presumido de conocer a todo el mundo sin que nadie lo corrobore.",
             "No hay nada más incómodo que quien presume de lo que no tiene.",
             "Presumía de que nunca se equivocaba, hasta que lo hizo públicamente.",
         ], "nivel": "B2"},

        {"verbo": "tratarse", "expresion": "tratarse de",
         "ejemplos": [
             "Se trata de una cuestión de principios, no de intereses económicos.",
             "¿De qué se trata exactamente la propuesta que has preparado?",
             "Cuando se trate de decisiones importantes, consulta siempre con el equipo.",
             "Ha quedado claro de qué se trata: de un malentendido sin más.",
         ], "nivel": "B2"},

        {"verbo": "abstenerse", "expresion": "abstenerse de",
         "ejemplos": [
             "Se abstuvo de comentar nada hasta conocer todos los detalles.",
             "Le recomendaron que se abstuviera de hacer declaraciones públicas.",
             "En situaciones así, es mejor que te abstengas de emitir un juicio precipitado.",
             "Se ha abstenido de votar porque considera que no tiene información suficiente.",
         ], "nivel": "C1"},

        {"verbo": "desistir", "expresion": "desistir de",
         "ejemplos": [
             "Desistió de su empeño tras años de intentos fallidos y costosos.",
             "No pienso desistir de mis objetivos por mucho que cueste.",
             "Ojalá no hubiera desistido de aquel proyecto tan prometedor.",
             "Le aconsejaron que desistiera de la demanda antes de que fuera demasiado tarde.",
         ], "nivel": "C1"},

        {"verbo": "quejarse", "expresion": "quejarse de",
         "ejemplos": [
             "Se queja constantemente de la falta de reconocimiento en el trabajo.",
             "No tiene motivo alguno de quejarse de su situación actual.",
             "Me sorprende que se haya quejado de algo tan nimio.",
             "Si te quejas de las condiciones, hazlo a través de los cauces oficiales.",
         ], "nivel": "C1"},

        {"verbo": "prescindir", "expresion": "prescindir de",
         "ejemplos": [
             "La empresa ha decidido prescindir de varios directivos de alto nivel.",
             "Es muy difícil prescindir de los hábitos que llevan años arraigados.",
             "Han prescindido de un proveedor que llevaba con ellos más de una década.",
             "Para que el texto funcione, tendrás que prescindir de todo lo accesorio.",
         ], "nivel": "C2"},

        {"verbo": "desprenderse", "expresion": "desprenderse de",
         "ejemplos": [
             "Le costó mucho desprenderse de aquella vieja costumbre tan perjudicial.",
             "De sus palabras se desprende una profunda tristeza que no disimula.",
             "No ha podido desprenderse de la sensación de que algo salió mal.",
             "Para avanzar, a veces hay que desprenderse de lo que más queremos.",
         ], "nivel": "C2"},

        {"verbo": "adolecer", "expresion": "adolecer de",
         "ejemplos": [
             "El informe adolece de una falta total de rigor metodológico.",
             "Su discurso adolece de cierta superficialidad que resulta muy evidente.",
             "El proyecto ha adolecido de los mismos defectos desde el principio.",
             "Toda propuesta que adolezca de transparencia está condenada al fracaso.",
         ], "nivel": "C2"},

        {"verbo": "jactarse", "expresion": "jactarse de",
         "ejemplos": [
             "Se jactaba de conocer a los personajes más influyentes del país.",
             "No es de buen gusto jactarse de los propios logros ante los demás.",
             "Se ha jactado de que nunca comete errores, lo cual es una exageración.",
             "Quien se jacte de saberlo todo, suele ser quien menos sabe.",
         ], "nivel": "C2"},

        {"verbo": "valerse", "expresion": "valerse de",
         "ejemplos": [
             "Se valió de sus contactos para conseguir el puesto que quería.",
             "Para lograrlo, se valió de todos los recursos que tenía disponibles.",
             "Se ha valido de argucias legales para evitar cualquier responsabilidad.",
             "No está bien valerse de la confianza de alguien para obtener ventajas.",
         ], "nivel": "C2"},

        {"verbo": "depender", "expresion": "depender de",
         "ejemplos": [
             "El resultado depende de muchos factores que aún no controlamos.",
             "Ha dependido siempre de la opinión ajena para tomar decisiones.",
             "Todo dependerá de que los socios lleguen a un acuerdo antes del viernes.",
             "Para que el plan funcione, no puede depender de una sola persona.",
         ], "nivel": "B2"},

        {"verbo": "carecer", "expresion": "carecer de",
         "ejemplos": [
             "La propuesta carece de sustento empírico y no puede aprobarse así.",
             "Un argumento que carezca de evidencias no tiene ningún valor.",
             "Ha carecido siempre de la empatía necesaria para liderar un equipo.",
             "Carecer de recursos no es excusa para carecer de ideas.",
         ], "nivel": "C1"},

        {"verbo": "burlarse", "expresion": "burlarse de",
         "ejemplos": [
             "Se burló de sus colegas sin darse cuenta del daño que causaba.",
             "No está bien burlarse de quien hace un esfuerzo honesto.",
             "Se han burlado de la normativa durante años sin consecuencias.",
             "Quien se burle de los errores ajenos, suele cometer los mismos.",
         ], "nivel": "B2"},

        {"verbo": "fiarse", "expresion": "fiarse de",
         "ejemplos": [
             "No me fío de las estadísticas que no puedo contrastar.",
             "¿Te has fiado de alguien que luego te ha fallado?",
             "Es difícil fiarse de una persona que ha mentido en repetidas ocasiones.",
             "Me alegra que te hayas fiado de mi criterio para tomar esta decisión.",
         ], "nivel": "B2"},

        {"verbo": "enterarse", "expresion": "enterarse de",
         "ejemplos": [
             "Se enteró de la noticia por un mensaje que nadie esperaba.",
             "¿Cómo te has enterado de que iban a hacer cambios en el equipo?",
             "Cuando se enteren de lo ocurrido, la reacción será imprevisible.",
             "Me habría gustado que me hubieran enterado de ello antes.",
         ], "nivel": "B2"},

        {"verbo": "librarse", "expresion": "librarse de",
         "ejemplos": [
             "Se libró de una sanción grave gracias a un error procedimental.",
             "No ha podido librarse de la sensación de culpa pese al tiempo transcurrido.",
             "Para que te libres de esa carga, necesitas hablar con alguien de confianza.",
             "Se han librado de responsabilidades que les correspondían claramente.",
         ], "nivel": "B2"},

        {"verbo": "servirse", "expresion": "servirse de",
         "ejemplos": [
             "Se sirvió de la ambigüedad del texto para interpretarlo a su favor.",
             "Ha sabido servirse de las herramientas disponibles con mucha eficacia.",
             "Para redactar el informe, se sirvió de datos que nadie había consultado antes.",
             "Es lícito servirse de la ley siempre que no se haga de mala fe.",
         ], "nivel": "C1"},

        {"verbo": "nutrirse", "expresion": "nutrirse de",
         "ejemplos": [
             "Su obra se nutre de referencias culturales muy diversas.",
             "El movimiento se ha nutrido de las aportaciones de cientos de voluntarios.",
             "Para que una argumentación sea sólida, debe nutrirse de evidencias contrastadas.",
             "Se nutría de lecturas que pocos en su entorno conocían.",
         ], "nivel": "C2"},

        {"verbo": "partir", "expresion": "partir de",
         "ejemplos": [
             "El análisis parte de premisas que no están suficientemente justificadas.",
             "Ha partido de cero y ha construido algo que nadie esperaba.",
             "Para que el razonamiento sea válido, debe partir de datos fiables.",
             "Partimos de la base de que todos los implicados actuaron de buena fe.",
         ], "nivel": "C1",
         "nota": "Partir de = tomar como punto de partida. No confundir con partir hacia = marcharse."},
    ],

    # ══════════════════════════════════════════
    #  + A
    # ══════════════════════════════════════════
    "a": [
        {"verbo": "acostumbrarse", "expresion": "acostumbrarse a",
         "ejemplos": [
             "Me estoy acostumbrando a vivir con mucha menos comodidad.",
             "Tardó años en acostumbrarse al ritmo vertiginoso de la ciudad.",
             "Cuando te hayas acostumbrado a la rutina, todo se hará más fácil.",
             "Nunca se ha acostumbrado a que le den órdenes sin una explicación.",
         ], "nivel": "B2"},

        {"verbo": "aprender", "expresion": "aprender a",
         "ejemplos": [
             "Está aprendiendo a gestionar la frustración de forma constructiva.",
             "Ha aprendido a leer entre líneas mejor que nadie en el equipo.",
             "Ojalá aprendamos a escuchar antes de juzgar.",
             "Aprendió a vivir con la incertidumbre sin que esta la paralizara.",
         ], "nivel": "B2"},

        {"verbo": "ayudar", "expresion": "ayudar a",
         "ejemplos": [
             "¿Podrías ayudarme a revisar este texto antes de enviarlo?",
             "La terapia le ayudó a superar un período realmente duro.",
             "Necesito que alguien me ayude a organizar las ideas antes de la reunión.",
             "Ha ayudado a cientos de personas a encontrar su camino.",
         ], "nivel": "B2"},

        {"verbo": "empezar", "expresion": "empezar a",
         "ejemplos": [
             "Empezó a llover justo cuando salíamos del edificio.",
             "He empezado a entender por qué esto no funcionaba.",
             "Cuando empieces a ver los resultados, la motivación llegará sola.",
             "Han empezado a tomar medidas que nadie esperaba tan pronto.",
         ], "nivel": "B2"},

        {"verbo": "invitar", "expresion": "invitar a",
         "ejemplos": [
             "La invité a reflexionar sobre sus propias contradicciones.",
             "Nos invitaron a participar en un debate que resultó muy enriquecedor.",
             "El texto invita a que el lector cuestione sus propias certezas.",
             "Ha invitado a todos sus contactos a unirse a la iniciativa.",
         ], "nivel": "B2"},

        {"verbo": "volver", "expresion": "volver a",
         "ejemplos": [
             "No quiero volver a cometer el mismo error dos veces.",
             "Ha vuelto a llamar tres veces sin que nadie descolgara.",
             "Cuando vuelvas a encontrarte en esa situación, recuerda lo aprendido.",
             "Nunca pensé que volvería a sentirme tan segura.",
         ], "nivel": "B2"},

        {"verbo": "animarse", "expresion": "animarse a",
         "ejemplos": [
             "Por fin se animó a pedir un aumento que llevaba meses mereciendo.",
             "Me animé a hablar en público y fue mucho mejor de lo esperado.",
             "¿Por qué no te animas a presentar tu proyecto al concurso?",
             "Se han animado a dar el paso que tanto tiempo habían pospuesto.",
         ], "nivel": "B2"},

        {"verbo": "resistirse", "expresion": "resistirse a",
         "ejemplos": [
             "Se resiste a admitir que está equivocado aunque las pruebas sean claras.",
             "Me resulta imposible resistirme a un buen libro bien escrito.",
             "Para que la reforma funcione, no puede resistirse a los cambios necesarios.",
             "Se ha resistido a aceptar la realidad durante demasiado tiempo.",
         ], "nivel": "B2"},

        {"verbo": "negarse", "expresion": "negarse a",
         "ejemplos": [
             "Se negó en redondo a firmar un contrato que consideraba injusto.",
             "Me niego a aceptar que no hay ninguna solución a este problema.",
             "Se han negado a colaborar sin dar una explicación razonada.",
             "Ojalá nunca tuvieras que negarte a algo por cuestión de principios.",
         ], "nivel": "B2"},

        {"verbo": "aspirar", "expresion": "aspirar a",
         "ejemplos": [
             "Aspira a ocupar un puesto de mayor responsabilidad en la organización.",
             "No aspira a la fama, sino al reconocimiento genuino de sus iguales.",
             "Para aspirar a ese cargo, necesitarás experiencia que aún no tienes.",
             "Ha aspirado siempre a algo más que lo que su entorno le ofrecía.",
         ], "nivel": "B2"},

        {"verbo": "decidirse", "expresion": "decidirse a",
         "ejemplos": [
             "Por fin se decidió a dar el paso que tanto tiempo había pospuesto.",
             "¿Cuándo te vas a decidir a hablar con ella de una vez?",
             "Me alegra que te hayas decidido a tomar las riendas de la situación.",
             "Cuando se decida a actuar, ya podría ser demasiado tarde.",
         ], "nivel": "B2"},

        {"verbo": "renunciar", "expresion": "renunciar a",
         "ejemplos": [
             "Renunció a su plaza fija para seguir un sueño incierto.",
             "No estoy dispuesto a renunciar a mis convicciones por comodidad.",
             "Ha renunciado a muchas cosas para poder estar presente en momentos clave.",
             "Ojalá nunca tengas que renunciar a lo que realmente importa.",
         ], "nivel": "B2"},

        {"verbo": "atreverse", "expresion": "atreverse a",
         "ejemplos": [
             "Pocos se atreven a cuestionar abiertamente sus métodos.",
             "Por fin se atrevió a decir en voz alta lo que todos pensaban.",
             "Me alegra que te hayas atrevido a plantear esa pregunta.",
             "¿Te atreverías a defender esa postura delante de todo el consejo?",
         ], "nivel": "C1"},

        {"verbo": "contribuir", "expresion": "contribuir a",
         "ejemplos": [
             "Sus investigaciones han contribuido a redefinir el campo de estudio.",
             "Todos debemos contribuir a construir una sociedad más justa.",
             "Ha contribuido a que el debate se enriqueciera con perspectivas nuevas.",
             "Para que contribuyas a mejorar el sistema, primero debes entenderlo.",
         ], "nivel": "C1"},

        {"verbo": "comprometerse", "expresion": "comprometerse a",
         "ejemplos": [
             "Se comprometió formalmente a entregar el informe antes del viernes.",
             "No me comprometo a nada sin leer antes todas las condiciones.",
             "Se han comprometido a que los cambios estarán listos antes del plazo.",
             "Para que te tomen en serio, debes comprometerte a cumplir lo que dices.",
         ], "nivel": "C1",
         "nota": "Comprometerse a + infinitivo (acción concreta). Comprometerse con + sustantivo (causa o persona)."},

        {"verbo": "oponerse", "expresion": "oponerse a",
         "ejemplos": [
             "Se opuso firmemente a cualquier tipo de censura o restricción.",
             "¿Por qué te opones a explorar alternativas que podrían funcionar?",
             "Se han opuesto a la propuesta sin haber leído el documento completo.",
             "Aunque se opongan a la medida, tendrán que acatarla.",
         ], "nivel": "C1"},

        {"verbo": "propender", "expresion": "propender a",
         "ejemplos": [
             "Propende a ver el lado negativo de las cosas incluso cuando van bien.",
             "Este tipo de argumentación propende a la generalización excesiva.",
             "Ha propendido siempre a soluciones individuales antes que colectivas.",
             "Un sistema que propenda a la inequidad acabará generando conflicto.",
         ], "nivel": "C2"},

        {"verbo": "abocarse", "expresion": "abocarse a",
         "ejemplos": [
             "El proyecto se está abocando a un fracaso que nadie quiere reconocer.",
             "Con esas decisiones, se aboca a una crisis que podría haberse evitado.",
             "Si no corrigen el rumbo, se habrán abocado a un callejón sin salida.",
             "Para que no se aboque al desastre, alguien tiene que tomar las riendas.",
         ], "nivel": "C2"},

        {"verbo": "acceder", "expresion": "acceder a",
         "ejemplos": [
             "Accedió a firmar el acuerdo solo tras largas negociaciones.",
             "No ha accedido a ninguna de las condiciones que se le plantearon.",
             "Para que accedan a reunirse contigo, necesitarás un intermediario.",
             "Se ha accedido a la información que antes estaba restringida.",
         ], "nivel": "C1"},

        {"verbo": "dedicarse", "expresion": "dedicarse a",
         "ejemplos": [
             "Se dedica a la investigación con una pasión que pocos entienden.",
             "Ha dedicado toda su vida profesional a causas que no dan beneficio inmediato.",
             "¿A qué te has dedicado estos años en los que no hemos tenido contacto?",
             "Para que pueda dedicarse a lo que importa, necesita delegar.",
         ], "nivel": "B2"},

        {"verbo": "exponerse", "expresion": "exponerse a",
         "ejemplos": [
             "Al publicar eso, se expone a críticas que quizás no está preparado para recibir.",
             "Se ha expuesto a riesgos innecesarios por no haber pedido consejo.",
             "Para que no te expongas a malentendidos, sé muy preciso en tu redacción.",
             "Quien se exponga a esa información sin contexto puede llegar a conclusiones erróneas.",
         ], "nivel": "C1"},

        {"verbo": "limitarse", "expresion": "limitarse a",
         "ejemplos": [
             "Se limitó a responder lo que le preguntaban, sin añadir nada más.",
             "No te limites a hacer lo mínimo cuando puedes dar mucho más.",
             "Ha limitado a describir los hechos sin emitir ningún juicio de valor.",
             "Para avanzar, no puedes limitarte a lo que ya conoces.",
         ], "nivel": "C1"},

        {"verbo": "resignarse", "expresion": "resignarse a",
         "ejemplos": [
             "Se resignó a vivir con una situación que nunca le pareció justa.",
             "No me resigno a aceptar que esto no tenga solución.",
             "Se han resignado a perder algo que nunca debieron dejar ir.",
             "Para resignarte a algo, primero tienes que haberlo intentado todo.",
         ], "nivel": "C1"},

        {"verbo": "someterse", "expresion": "someterse a",
         "ejemplos": [
             "Se sometió a una revisión exhaustiva sin poner ninguna objeción.",
             "Ha debido someterse a procesos que considera injustos pero inevitables.",
             "Para que el acuerdo sea válido, ambas partes deben someterse a sus términos.",
             "Se somete a una disciplina rigurosa que pocos serían capaces de mantener.",
         ], "nivel": "C1"},

        {"verbo": "tender", "expresion": "tender a",
         "ejemplos": [
             "Tiende a dramatizar situaciones que en realidad son manejables.",
             "Ha tendido siempre a buscar el consenso antes que el conflicto.",
             "Para que un sistema tienda al equilibrio, necesita mecanismos de corrección.",
             "Las personas que han sufrido mucho tienden a desconfiar más de lo normal.",
         ], "nivel": "C1"},
    ],

    # ══════════════════════════════════════════
    #  + CON
    # ══════════════════════════════════════════
    "con": [
        {"verbo": "soñar", "expresion": "soñar con",
         "ejemplos": [
             "Sueña con un mundo en el que la injusticia no exista.",
             "Anoche soñé contigo y me desperté con una sensación extraña.",
             "Ha soñado con ese momento toda su vida y por fin está cerca.",
             "Cuando sueñes con algo con tanta intensidad, ya estás a medio camino.",
         ], "nivel": "B2"},

        {"verbo": "contar", "expresion": "contar con",
         "ejemplos": [
             "Puedes contar conmigo para lo que necesites, sin dudarlo.",
             "No contaba con que la situación se complicara tanto en tan poco tiempo.",
             "¿Has contado con la posibilidad de que no lleguen a tiempo?",
             "Para que el plan funcione, hay que contar con todos los implicados.",
         ], "nivel": "B2",
         "nota": "Contar con = disponer de algo o confiar en alguien. Contar de = narrar (coloquial)."},

        {"verbo": "enfadarse", "expresion": "enfadarse con",
         "ejemplos": [
             "Se enfadó conmigo por una tontería y no habló en tres días.",
             "Es fácil enfadarse con los demás cuando uno está agotado.",
             "Me he enfadado con ella porque no avisó de que no vendría.",
             "No te enfades con quien solo intenta ayudarte.",
         ], "nivel": "B2",
         "nota": "Enfadarse CON alguien (persona). Enfadarse POR algo (motivo o causa)."},

        {"verbo": "conformarse", "expresion": "conformarse con",
         "ejemplos": [
             "No se conforma con menos del cien por cien en todo lo que hace.",
             "Se conformó con una respuesta vaga cuando merecía una explicación completa.",
             "¿De verdad te has conformado con lo que te han ofrecido?",
             "Para que no tengas que conformarte con migajas, negocia desde el principio.",
         ], "nivel": "B2"},

        {"verbo": "encontrarse", "expresion": "encontrarse con",
         "ejemplos": [
             "Me encontré con una situación que no había previsto en absoluto.",
             "Se encontró con su ex en el aeropuerto, de todas las casualidades.",
             "¿Te has encontrado con algún obstáculo que no supieras cómo gestionar?",
             "Cuando se encuentren con la verdad, la reacción será difícil de controlar.",
         ], "nivel": "B2"},

        {"verbo": "toparse", "expresion": "toparse con",
         "ejemplos": [
             "Se topó con una resistencia que no esperaba en absoluto.",
             "Me topé con ese artículo por pura casualidad mientras buscaba otra cosa.",
             "Ha topado con los mismos problemas que todos quienes lo intentaron antes.",
             "Cuando te topes con una barrera, busca el camino alrededor.",
         ], "nivel": "B2"},

        {"verbo": "comprometerse", "expresion": "comprometerse con",
         "ejemplos": [
             "Se comprometió de corazón con la causa medioambiental.",
             "Hay que comprometerse con aquello en lo que uno realmente cree.",
             "Se ha comprometido con un proyecto que le exige mucho más de lo esperado.",
             "Para que te comprometas con algo de verdad, tiene que importarte.",
         ], "nivel": "C1",
         "nota": "Comprometerse CON + sustantivo (causa, persona). Comprometerse A + infinitivo (acción concreta)."},

        {"verbo": "indignarse", "expresion": "indignarse con",
         "ejemplos": [
             "Se indigna con cualquier forma de hipocresía que percibe a su alrededor.",
             "Me indigné con su respuesta desdeñosa y poco profesional.",
             "Se ha indignado con quienes han usado el tema para hacer política.",
             "Es comprensible indignarse con quien actúa de mala fe.",
         ], "nivel": "C1",
         "nota": "Indignarse CON alguien (persona). Indignarse POR algo (motivo o causa)."},

        {"verbo": "cebarse", "expresion": "cebarse con",
         "ejemplos": [
             "La crítica se cebó especialmente con su última novela.",
             "La enfermedad se cebó con los sectores más vulnerables de la población.",
             "Se ha cebado con él de una forma que nadie considera justificada.",
             "Para que no se ceban con nadie, el sistema debe ser equitativo.",
         ], "nivel": "C2"},

        {"verbo": "colaborar", "expresion": "colaborar con",
         "ejemplos": [
             "Ha colaborado con organizaciones de todo el mundo durante años.",
             "Necesitamos que todos colaboren con el proceso de manera constructiva.",
             "¿Con quién has colaborado en el diseño de este proyecto?",
             "Para que los resultados mejoren, los departamentos deben colaborar entre sí.",
         ], "nivel": "B2"},

        {"verbo": "coincidir", "expresion": "coincidir con",
         "ejemplos": [
             "Coincidió con ella en una conferencia que ninguno esperaba asistir.",
             "Mis conclusiones no coinciden con las que ha presentado el informe.",
             "Ha coincidido con varios expertos en que la medida es insuficiente.",
             "Para que las ideas coincidan, primero hay que escucharse mutuamente.",
         ], "nivel": "B2",
         "nota": "Coincidir con = encontrarse o estar de acuerdo con alguien/algo."},

        {"verbo": "cumplir", "expresion": "cumplir con",
         "ejemplos": [
             "Ha cumplido con todos los requisitos sin excepción.",
             "Para que la propuesta prospere, debe cumplir con la normativa vigente.",
             "Se ha comprometido a cumplir con los plazos sin importar las dificultades.",
             "Quien no cumpla con sus obligaciones, deberá responder por ello.",
         ], "nivel": "B2"},

        {"verbo": "lidiar", "expresion": "lidiar con",
         "ejemplos": [
             "Lleva años lidiando con una burocracia que no facilita nada.",
             "Ha lidiado con situaciones mucho más complejas que esta.",
             "Para que puedas lidiar con el problema, primero tienes que entenderlo.",
             "¿Cómo has lidiado con la presión durante todo este tiempo?",
         ], "nivel": "C1"},

        {"verbo": "reconciliarse", "expresion": "reconciliarse con",
         "ejemplos": [
             "Se reconcilió con su hermano después de años de silencio.",
             "Ha tardado mucho en reconciliarse con su propio pasado.",
             "Para reconciliarse con alguien, hace falta voluntad de las dos partes.",
             "Se ha reconciliado con la idea de que no todo puede controlarse.",
         ], "nivel": "C1"},

        {"verbo": "romper", "expresion": "romper con",
         "ejemplos": [
             "Rompió con una tradición que llevaba décadas sin cuestionarse.",
             "Ha roto con todo lo que conocía para empezar desde cero.",
             "Para avanzar, a veces es necesario romper con lo establecido.",
             "Se ha roto con un modelo que ya no responde a las necesidades reales.",
         ], "nivel": "C1"},

        {"verbo": "ilusionarse", "expresion": "ilusionarse con",
         "ejemplos": [
             "Se ilusionó con el proyecto antes de conocer todos los detalles.",
             "No te ilusiones con algo que todavía no está confirmado.",
             "Se ha ilusionado con una posibilidad que me parece remota.",
             "Para que te ilusiones con algo de verdad, tiene que resonar contigo.",
         ], "nivel": "B2"},

        {"verbo": "relacionarse", "expresion": "relacionarse con",
         "ejemplos": [
             "Le cuesta relacionarse con personas que no comparten sus valores.",
             "Se ha relacionado con los ámbitos más diversos a lo largo de su carrera.",
             "Para relacionarte con eficacia, escucha más de lo que hablas.",
             "Ha aprendido a relacionarse con la incertidumbre sin que la paralice.",
         ], "nivel": "B2"},
    ],

    # ══════════════════════════════════════════
    #  + EN
    # ══════════════════════════════════════════
    "en": [
        {"verbo": "fijarse", "expresion": "fijarse en",
         "ejemplos": [
             "Fíjate bien en los matices antes de emitir un juicio precipitado.",
             "Se fijó en un detalle que todos los demás habían pasado por alto.",
             "¿Te has fijado en que nadie ha mencionado el punto más importante?",
             "Para que te fijes en lo esencial, aprende a ignorar lo accesorio.",
         ], "nivel": "B2"},

        {"verbo": "pensar", "expresion": "pensar en",
         "ejemplos": [
             "Llevo días pensando en aquella conversación que no debió acabar así.",
             "Antes de actuar, piensa siempre en las consecuencias para los demás.",
             "Ha pensado en ti cada vez que ha tenido que tomar una decisión difícil.",
             "Para que piensen en ti cuando haya oportunidades, sé memorable.",
         ], "nivel": "B2",
         "nota": "Pensar EN = tener en mente. Pensar DE = opinar sobre algo o alguien."},

        {"verbo": "tardar", "expresion": "tardar en",
         "ejemplos": [
             "No tardó en darse cuenta de que algo iba fundamentalmente mal.",
             "¿Cuánto has tardado en terminar el primer borrador?",
             "Espero que no tarde en llegar una respuesta que aclare todo.",
             "Ha tardado años en recuperarse de algo que nunca debió ocurrir.",
         ], "nivel": "B2"},

        {"verbo": "insistir", "expresion": "insistir en",
         "ejemplos": [
             "Insiste en que no pasó nada, aunque las pruebas indican lo contrario.",
             "No insistas en una idea cuando el contexto ya ha cambiado por completo.",
             "Ha insistido en que se revisen los datos antes de publicar nada.",
             "Para que insistan en tu propuesta, tiene que quedarles claro el valor.",
         ], "nivel": "B2"},

        {"verbo": "consistir", "expresion": "consistir en",
         "ejemplos": [
             "El verdadero reto consiste en mantener la coherencia bajo presión extrema.",
             "¿En qué consiste exactamente la propuesta que has presentado hoy?",
             "La clave ha consistido en escuchar antes de proponer cualquier solución.",
             "Para que un método funcione, debe consistir en pasos replicables.",
         ], "nivel": "B2"},

        {"verbo": "convertirse", "expresion": "convertirse en",
         "ejemplos": [
             "Lo que empezó como un hobby se convirtió en su medio de vida.",
             "Se ha convertido en un referente del pensamiento crítico en su campo.",
             "Para que una idea se convierta en realidad, necesita ejecución.",
             "Nunca pensó que aquella decisión se convertiría en un punto de inflexión.",
         ], "nivel": "B2"},

        {"verbo": "confiar", "expresion": "confiar en",
         "ejemplos": [
             "Confía en tu propio criterio aunque los demás no lo compartan.",
             "Tardé mucho en volver a confiar en alguien después de esa experiencia.",
             "¿Has confiado alguna vez en alguien que no lo merecía?",
             "Para que confíen en ti, primero debes ser coherente con lo que dices.",
         ], "nivel": "B2"},

        {"verbo": "influir", "expresion": "influir en",
         "ejemplos": [
             "El entorno influye de forma determinante en el desarrollo de las personas.",
             "¿Quién ha influido más en tu manera de ver el mundo?",
             "Ha influido en toda una generación de pensadores sin proponérselo.",
             "Para que un libro influya en alguien, tiene que llegar en el momento preciso.",
         ], "nivel": "B2"},

        {"verbo": "participar", "expresion": "participar en",
         "ejemplos": [
             "Participó en el debate con argumentos sólidos y bien documentados.",
             "¿Has participado alguna vez en un proceso de toma de decisiones colectivo?",
             "Se ha negado a participar en algo que considera éticamente cuestionable.",
             "Para que todos participen de forma equitativa, las reglas deben ser claras.",
         ], "nivel": "B2"},

        {"verbo": "empeñarse", "expresion": "empeñarse en",
         "ejemplos": [
             "Se empeña en ver problemas donde no los hay.",
             "Por más que me empeñé en convencerle, no quiso escuchar razones.",
             "Se ha empeñado en un proyecto que todos consideran inviable.",
             "Para que no te empeñes en algo sin futuro, consulta con alguien externo.",
         ], "nivel": "C1"},

        {"verbo": "especializarse", "expresion": "especializarse en",
         "ejemplos": [
             "Decidió especializarse en derecho internacional tras varios años de duda.",
             "Se ha especializado en un área de nicho que pocos dominan.",
             "Para especializarte en algo, primero debes tener una base sólida.",
             "Ha especializado su oferta en un segmento que nadie había atendido.",
         ], "nivel": "C1"},

        {"verbo": "redundar", "expresion": "redundar en",
         "ejemplos": [
             "Ese acuerdo redunda en beneficio de todas las partes implicadas.",
             "Una buena formación siempre redunda en mejores resultados a largo plazo.",
             "Se ha comprobado que la medida ha redundado en perjuicio de los más vulnerables.",
             "Para que redunde en beneficio colectivo, la decisión debe ser transparente.",
         ], "nivel": "C2"},

        {"verbo": "incidir", "expresion": "incidir en",
         "ejemplos": [
             "Quiero incidir en la importancia de este punto antes de pasar al siguiente.",
             "La política fiscal incide directamente en el bienestar social de la población.",
             "Ha incidido en los mismos argumentos sin aportar nada nuevo al debate.",
             "Para que incidas en lo correcto, debes saber qué es lo esencial.",
         ], "nivel": "C2"},

        {"verbo": "ahondar", "expresion": "ahondar en",
         "ejemplos": [
             "El ensayo ahonda en las contradicciones del sistema con una lucidez notable.",
             "No quiso ahondar en los detalles más dolorosos de aquella etapa.",
             "Ha ahondado en cuestiones que otros prefieren ignorar.",
             "Para ahondar en un tema, primero hay que dominarlo en la superficie.",
         ], "nivel": "C2"},

        {"verbo": "centrarse", "expresion": "centrarse en",
         "ejemplos": [
             "Necesita centrarse en lo que realmente importa y dejar de dispersarse.",
             "El debate se ha centrado en aspectos secundarios que no son el fondo del asunto.",
             "Para que te centres en lo esencial, elimina todo lo que distraiga.",
             "Se ha centrado en un problema concreto que nadie había abordado antes.",
         ], "nivel": "B2"},

        {"verbo": "creer", "expresion": "creer en",
         "ejemplos": [
             "Cree en la bondad de las personas incluso cuando le han fallado.",
             "¿Todavía crees en la posibilidad de que esto cambie?",
             "Ha creído siempre en proyectos que otros consideraban utópicos.",
             "Para creer en algo de verdad, tienes que haberlo cuestionado primero.",
         ], "nivel": "B2"},

        {"verbo": "fracasar", "expresion": "fracasar en",
         "ejemplos": [
             "Fracasó en su primer intento pero aprendió más de eso que de sus éxitos.",
             "Ha fracasado en varios proyectos sin que eso le haya quitado el impulso.",
             "Para no fracasar en algo importante, prepárate como si dependiera solo de ti.",
             "Si fracasas en el proceso, al menos habrás aprendido para la próxima vez.",
         ], "nivel": "B2"},

        {"verbo": "implicarse", "expresion": "implicarse en",
         "ejemplos": [
             "Se implicó en el proyecto desde el primer día con una energía envidiable.",
             "No se ha implicado lo suficiente como para reclamar parte del mérito.",
             "Para que el equipo funcione, todos deben implicarse por igual.",
             "Se habría implicado más si le hubieran dado más autonomía.",
         ], "nivel": "C1"},

        {"verbo": "profundizar", "expresion": "profundizar en",
         "ejemplos": [
             "Ha profundizado en aspectos del tema que la bibliografía habitual ignora.",
             "Para profundizar en un campo, necesitas tiempo y disciplina.",
             "Profundizó en las causas estructurales sin perder de vista el caso concreto.",
             "Cuando profundices en esto, verás que la realidad es más compleja.",
         ], "nivel": "C1"},

        {"verbo": "quedar", "expresion": "quedar en",
         "ejemplos": [
             "Quedamos en vernos el jueves a las siete en la entrada.",
             "¿En qué habéis quedado para resolver el conflicto?",
             "Han quedado en que cada uno aportará lo que pueda.",
             "Para que quedes en algo con alguien, asegúrate de que sea concreto.",
         ], "nivel": "B2",
         "nota": "Quedar EN = acordar algo. Quedar CON = citarse con alguien."},

        {"verbo": "reparar", "expresion": "reparar en",
         "ejemplos": [
             "Nadie reparó en el error hasta que ya era demasiado tarde para corregirlo.",
             "¿Has reparado en que nadie ha preguntado lo más obvio?",
             "Si hubieras reparado en ese detalle antes, habríamos evitado el problema.",
             "Para reparar en lo importante, hay que aprender a mirar con atención.",
         ], "nivel": "C1"},

        {"verbo": "vacilar", "expresion": "vacilar en",
         "ejemplos": [
             "No vaciló en defender su postura ante quien fuera.",
             "Ha vacilado en tomar una decisión que lleva semanas sobre la mesa.",
             "Para que no vaciles en el momento clave, practica de antemano.",
             "Se ha vacilado demasiado y ahora la oportunidad se ha perdido.",
         ], "nivel": "C2"},
    ],

    # ══════════════════════════════════════════
    #  + POR
    # ══════════════════════════════════════════
    "por": [
        {"verbo": "preocuparse", "expresion": "preocuparse por",
         "ejemplos": [
             "Se preocupa por los demás antes que por sí mismo, siempre.",
             "Me preocupa por el rumbo que está tomando todo esto.",
             "¿Te has preocupado alguna vez por algo que luego resultó no ser nada?",
             "Para que no te preocupes por todo, aprende a distinguir lo urgente de lo importante.",
         ], "nivel": "B2"},

        {"verbo": "luchar", "expresion": "luchar por",
         "ejemplos": [
             "Lleva años luchando por un reconocimiento que se le niega.",
             "Vale la pena luchar por lo que uno considera justo.",
             "Ha luchado por sus ideales en contextos donde hacerlo tenía un coste real.",
             "Para que luchar por algo tenga sentido, tiene que importarte de verdad.",
         ], "nivel": "B2"},

        {"verbo": "esforzarse", "expresion": "esforzarse por",
         "ejemplos": [
             "Se esfuerza por entender puntos de vista muy distintos al suyo.",
             "Me esforcé por no dejar traslucir mi incomodidad durante la reunión.",
             "Se ha esforzado por mejorar en un área que le costaba mucho.",
             "Para que te esfuerces por algo, primero tiene que importarte el resultado.",
         ], "nivel": "B2"},

        {"verbo": "interesarse", "expresion": "interesarse por",
         "ejemplos": [
             "Se interesa genuinamente por el bienestar de cada persona en su equipo.",
             "Nunca se había interesado por la política hasta que le afectó directamente.",
             "¿Te has interesado alguna vez por algo sin saber bien por qué?",
             "Para que alguien se interese por tu trabajo, primero tiene que conocerlo.",
         ], "nivel": "B2"},

        {"verbo": "optar", "expresion": "optar por",
         "ejemplos": [
             "Optó por guardar silencio antes que decir algo de lo que arrepentirse.",
             "Si tuviera que elegir, optaría sin duda por la segunda opción.",
             "Ha optado por una vía que nadie esperaba pero que tiene mucho sentido.",
             "Para optar por algo con convicción, necesitas conocer bien las alternativas.",
         ], "nivel": "B2"},

        {"verbo": "disculparse", "expresion": "disculparse por",
         "ejemplos": [
             "Se disculpó por las molestias ocasionadas con una nota breve y lacónica.",
             "Nunca se disculpó por lo que dijo aquella noche, y eso lo cambió todo.",
             "Se ha disculpado públicamente por unas declaraciones que generaron controversia.",
             "Para disculparse por algo de verdad, no basta con decirlo: hay que sentirlo.",
         ], "nivel": "B2"},

        {"verbo": "apostar", "expresion": "apostar por",
         "ejemplos": [
             "La directiva apostó por un perfil joven y sin experiencia previa.",
             "Siempre he apostado por la honestidad, aunque salga caro a veces.",
             "Ha apostado por una estrategia arriesgada que muchos consideraban un error.",
             "Para apostar por alguien, tienes que confiar en su potencial.",
         ], "nivel": "B2"},

        {"verbo": "velar", "expresion": "velar por",
         "ejemplos": [
             "La institución debe velar por el interés general, no por el particular.",
             "Como responsable, velo por que se cumplan todas las normas sin excepción.",
             "Se ha velado por que nadie quedara fuera del proceso.",
             "Para que alguien vele por tus intereses, tiene que conocerlos bien.",
         ], "nivel": "C1"},

        {"verbo": "abogar", "expresion": "abogar por",
         "ejemplos": [
             "Aboga por una reforma profunda del sistema educativo.",
             "Su obra aboga por una reconciliación entre ciencia y humanismo.",
             "Ha abogado siempre por los derechos de quienes no tienen voz.",
             "Para abogar por algo con credibilidad, debes haberlo vivido.",
         ], "nivel": "C1"},

        {"verbo": "pujar", "expresion": "pujar por",
         "ejemplos": [
             "Varios coleccionistas pujaron por esa obra en la subasta.",
             "Ambas empresas pugnan por hacerse con el contrato más lucrativo.",
             "Se ha pujado por un activo que muy pocos entendían que valía tanto.",
             "Para pujar por algo en serio, primero debes saber cuánto vale.",
         ], "nivel": "C2"},

        {"verbo": "clamar", "expresion": "clamar por",
         "ejemplos": [
             "La sociedad civil clamaba por justicia sin que nadie la escuchara.",
             "Clamaron por una respuesta que nunca llegó.",
             "Se ha clamado por cambios estructurales durante décadas.",
             "Para que tu voz sea escuchada cuando clamas por algo, necesitas aliados.",
         ], "nivel": "C2"},

        {"verbo": "enfadarse", "expresion": "enfadarse por",
         "ejemplos": [
             "Se enfadó por la falta de respeto, no por lo que dijeron en concreto.",
             "Me he enfadado por algo que en retrospectiva no merecía tanta energía.",
             "¿Por qué te enfadas por cosas que no puedes controlar?",
             "Se ha enfadado por que nadie le avisó del cambio de planes a tiempo.",
         ], "nivel": "B2",
         "nota": "Enfadarse POR algo (motivo o causa). Enfadarse CON alguien (persona responsable)."},

        {"verbo": "indignarse", "expresion": "indignarse por",
         "ejemplos": [
             "Se indignó por el trato recibido durante la reunión.",
             "Me indigno por la impunidad con la que actúan algunos.",
             "Se han indignado por que la decisión se tomó sin consultar a nadie.",
             "Para indignarse por algo con legitimidad, hay que conocerlo bien.",
         ], "nivel": "C1",
         "nota": "Indignarse POR algo (motivo). Indignarse CON alguien (persona)."},

        {"verbo": "decantarse", "expresion": "decantarse por",
         "ejemplos": [
             "Al final se decantó por la opción más conservadora y segura.",
             "Se ha decantado por una metodología que nadie había probado en este contexto.",
             "¿Por cuál de las dos propuestas te has decantado finalmente?",
             "Para decantarse por algo, a veces hay que probar las dos opciones.",
         ], "nivel": "C1"},

        {"verbo": "responsabilizarse", "expresion": "responsabilizarse por",
         "ejemplos": [
             "Se responsabilizó por las consecuencias de una decisión que no fue solo suya.",
             "Nadie quiso responsabilizarse por el error que costó tan caro.",
             "Ha tardado mucho en responsabilizarse por lo que ocurrió.",
             "Para responsabilizarte por algo, primero tienes que entender tu papel.",
         ], "nivel": "C1"},

        {"verbo": "afanarse", "expresion": "afanarse por",
         "ejemplos": [
             "Se afana por conseguir resultados que justifiquen tanto esfuerzo.",
             "Ha afanado toda su energía por un objetivo que muchos no comprenden.",
             "Para que te afanes por algo vale la pena, asegúrate de que es lo correcto.",
             "Se afanó por terminar antes del plazo aunque nadie se lo pidiera.",
         ], "nivel": "C2"},

        {"verbo": "pugnar", "expresion": "pugnar por",
         "ejemplos": [
             "Ambos candidatos pugnan por hacerse con el control del partido.",
             "Ha pugnado por mantener su independencia en un entorno que la limitaba.",
             "Se pugna por recursos que cada vez son más escasos.",
             "Para pugnar por algo con éxito, necesitas más que voluntad.",
         ], "nivel": "C2"},
    ],

    # ══════════════════════════════════════════
    #  + SOBRE
    # ══════════════════════════════════════════
    "sobre": [
        {"verbo": "reflexionar", "expresion": "reflexionar sobre",
         "ejemplos": [
             "Necesito tiempo para reflexionar sobre todo lo que ha pasado.",
             "Ha reflexionado largamente sobre las implicaciones éticas de su decisión.",
             "Para que reflexiones sobre algo de verdad, aparta el ruido y el juicio.",
             "Se ha pedido a todos los implicados que reflexionen sobre su papel.",
         ], "nivel": "B2"},

        {"verbo": "pronunciarse", "expresion": "pronunciarse sobre",
         "ejemplos": [
             "Se pronunció sobre el asunto con una claridad que nadie esperaba.",
             "No se ha pronunciado sobre la dimisión, lo cual dice mucho.",
             "Para que se pronuncien sobre algo oficial, hay que solicitarlo formalmente.",
             "Se han pronunciado sobre el tema personas de todo el espectro político.",
         ], "nivel": "C1"},

        {"verbo": "debatir", "expresion": "debatir sobre",
         "ejemplos": [
             "Debatieron sobre la propuesta durante horas sin llegar a un consenso.",
             "¿Has debatido alguna vez sobre algo que te haya cambiado la perspectiva?",
             "Se ha debatido sobre este asunto en múltiples foros internacionales.",
             "Para debatir sobre algo con rigor, primero hay que documentarse.",
         ], "nivel": "B2"},

        {"verbo": "meditar", "expresion": "meditar sobre",
         "ejemplos": [
             "Meditó sobre la decisión durante días antes de dar una respuesta.",
             "Ha meditado profundamente sobre el sentido de lo que hace.",
             "Para meditar sobre algo sin distorsiones, necesitas distancia emocional.",
             "Se le recomendó que meditara sobre las consecuencias antes de actuar.",
         ], "nivel": "C1"},

        {"verbo": "especular", "expresion": "especular sobre",
         "ejemplos": [
             "No quiero especular sobre las causas sin tener más datos.",
             "Se ha especulado mucho sobre sus intenciones sin base real.",
             "Para especular sobre el futuro de forma útil, parte de datos del presente.",
             "Han especulado sobre el tema sin aportar ninguna evidencia.",
         ], "nivel": "C1"},

        {"verbo": "opinar", "expresion": "opinar sobre",
         "ejemplos": [
             "¿Has opinado alguna vez sobre algo sin conocerlo suficientemente bien?",
             "Se opinó sobre la propuesta antes de que estuviera terminada.",
             "Para opinar sobre algo con autoridad, necesitas haberlo vivido o estudiado.",
             "Ha opinado sobre el asunto con la prudencia que caracteriza su estilo.",
         ], "nivel": "B2"},

        {"verbo": "indagar", "expresion": "indagar sobre",
         "ejemplos": [
             "Indagó sobre el origen de los fondos sin encontrar respuestas claras.",
             "Se ha indagado sobre el asunto pero los resultados no son concluyentes.",
             "Para indagar sobre algo de forma efectiva, necesitas saber qué buscas.",
             "Ha indagado sobre aspectos del tema que nadie había explorado antes.",
         ], "nivel": "C1"},

        {"verbo": "teorizar", "expresion": "teorizar sobre",
         "ejemplos": [
             "Teorizó sobre el problema durante años sin llevarlo nunca a la práctica.",
             "Es más fácil teorizar sobre algo que afrontarlo directamente.",
             "Se ha teorizado mucho sobre este fenómeno sin suficiente base empírica.",
             "Para que teorices sobre algo con credibilidad, debes conocer el terreno.",
         ], "nivel": "C2"},

        {"verbo": "recaer", "expresion": "recaer sobre",
         "ejemplos": [
             "La responsabilidad recae sobre quienes tienen el poder de decidir.",
             "Ha recaído sobre ella una carga que no le correspondía asumir sola.",
             "Para que la decisión no recaiga sobre una sola persona, hay que compartirla.",
             "Se ha recaído sobre los mismos argumentos de siempre sin avanzar.",
         ], "nivel": "C2"},

        {"verbo": "advertir", "expresion": "advertir sobre",
         "ejemplos": [
             "Advirtió sobre los riesgos del proyecto mucho antes de que fallara.",
             "Se ha advertido sobre este peligro en repetidas ocasiones sin que nadie escuchara.",
             "Para advertir sobre algo con eficacia, el mensaje debe ser concreto.",
             "Han advertido sobre las consecuencias con una claridad que nadie puede ignorar.",
         ], "nivel": "C1"},

        {"verbo": "escribir", "expresion": "escribir sobre",
         "ejemplos": [
             "Ha escrito sobre temas que pocos se atreven a abordar en público.",
             "¿Sobre qué escribirías si pudieras elegir libremente?",
             "Se escribe mucho sobre esto pero se entiende poco.",
             "Para escribir sobre algo con profundidad, primero hay que vivirlo.",
         ], "nivel": "B2"},

        {"verbo": "volver", "expresion": "volver sobre",
         "ejemplos": [
             "Volvió sobre el tema cuando creíamos que ya estaba cerrado.",
             "Ha vuelto sobre sus pasos para reconsiderar algo que daba por hecho.",
             "Para volver sobre un asunto sin repetirte, tienes que añadir perspectiva.",
             "Se volvió sobre las mismas conclusiones desde un ángulo completamente distinto.",
         ], "nivel": "C1",
         "nota": "Volver sobre = retomar un tema. No confundir con volver a + infinitivo = hacer algo de nuevo."},
    ],

    # ══════════════════════════════════════════
    #  + CONTRA
    # ══════════════════════════════════════════
    "contra": [
        {"verbo": "luchar", "expresion": "luchar contra",
         "ejemplos": [
             "Ha luchado contra la injusticia en contextos donde hacerlo tenía un coste real.",
             "Luchó contra sus propios miedos hasta que dejaron de paralizarle.",
             "Para luchar contra algo, primero tienes que nombrarlo claramente.",
             "Se ha luchado contra este prejuicio durante décadas con resultados desiguales.",
         ], "nivel": "B2",
         "nota": "Luchar CONTRA algo (oposición). Luchar POR algo (objetivo o causa)."},

        {"verbo": "atentar", "expresion": "atentar contra",
         "ejemplos": [
             "Esa medida atenta contra los derechos más fundamentales.",
             "Ha atentado contra los valores que decía defender.",
             "Para que algo no atente contra la dignidad, debe respetar la autonomía.",
             "Se ha atentado contra la libertad de expresión bajo pretexto de seguridad.",
         ], "nivel": "C1"},

        {"verbo": "rebelarse", "expresion": "rebelarse contra",
         "ejemplos": [
             "Se rebeló contra un sistema que consideraba profundamente injusto.",
             "Ha tardado años en rebelarse contra una dinámica que la perjudicaba.",
             "Para rebelarse contra algo de forma efectiva, hay que proponer una alternativa.",
             "Se han rebelado contra normas que nadie cuestionaba por comodidad.",
         ], "nivel": "C1"},

        {"verbo": "conspirar", "expresion": "conspirar contra",
         "ejemplos": [
             "Todo parecía conspirar contra el éxito del proyecto desde el principio.",
             "Se acusó a varios directivos de haber conspirado contra los intereses de la empresa.",
             "Para que no conspires contra ti mismo, alinea tus acciones con tus objetivos.",
             "Las circunstancias han conspirado contra sus mejores intenciones.",
         ], "nivel": "C2"},

        {"verbo": "ir", "expresion": "ir contra",
         "ejemplos": [
             "Su propuesta va contra todo lo que el equipo ha acordado hasta ahora.",
             "Ha ido contra la corriente toda su vida y no parece arrepentirse.",
             "Para ir contra algo establecido, necesitas argumentos muy sólidos.",
             "Esa decisión va contra los principios que esta organización dice defender.",
         ], "nivel": "B2"},

        {"verbo": "pronunciarse", "expresion": "pronunciarse contra",
         "ejemplos": [
             "Se pronunció contra la medida con argumentos que nadie pudo refutar.",
             "Ha pronunciado contra toda forma de discriminación desde el primer día.",
             "Para pronunciarte contra algo en público, debes estar dispuesto a defenderlo.",
             "Se han pronunciado contra la propuesta más de veinte organismos.",
         ], "nivel": "C1"},

        {"verbo": "manifestarse", "expresion": "manifestarse contra",
         "ejemplos": [
             "Miles de personas se manifestaron contra la reforma.",
             "Se ha manifestado contra la política de recortes en repetidas ocasiones.",
             "Para manifestarte contra algo de forma efectiva, organízate con otros.",
             "Se manifestaron contra una decisión que consideraban ilegítima.",
         ], "nivel": "B2"},

        {"verbo": "discriminar", "expresion": "discriminar contra",
         "ejemplos": [
             "La ley prohíbe discriminar contra cualquier persona por razón de origen.",
             "Se ha discriminado contra este colectivo durante décadas sin consecuencias.",
             "Para que no se discrimine contra nadie, las normas deben ser inequívocas.",
             "Ha denunciado que se ha discriminado contra ella en el proceso de selección.",
         ], "nivel": "C1"},

        {"verbo": "actuar", "expresion": "actuar contra",
         "ejemplos": [
             "Han actuado contra las recomendaciones de todos los expertos.",
             "Se actuó contra los responsables con una rapidez inusual.",
             "Para que actúes contra algo con eficacia, debes conocerlo bien.",
             "Ha actuado contra sus propios intereses por cuestión de principios.",
         ], "nivel": "C1"},

        {"verbo": "inmunizarse", "expresion": "inmunizarse contra",
         "ejemplos": [
             "Con los años se ha inmunizado contra las críticas que antes le dolían.",
             "Para inmunizarte contra la manipulación, desarrolla tu pensamiento crítico.",
             "Se ha inmunizado contra el desánimo gracias a una disciplina inquebrantable.",
             "Nadie puede inmunizarse completamente contra el error.",
         ], "nivel": "C2"},
    ],

    # ══════════════════════════════════════════
    #  + ANTE
    # ══════════════════════════════════════════
    "ante": [
        {"verbo": "rendirse", "expresion": "rendirse ante",
         "ejemplos": [
             "Se rindió ante la evidencia cuando ya no había forma de negarla.",
             "Nunca se ha rendido ante las dificultades, por grandes que fueran.",
             "Para no rendirte ante el primer obstáculo, necesitas una razón poderosa.",
             "Se rindieron ante una realidad que habían intentado ignorar durante meses.",
         ], "nivel": "C1"},

        {"verbo": "doblegarse", "expresion": "doblegarse ante",
         "ejemplos": [
             "Se negó a doblegarse ante la presión que ejercían sobre ella.",
             "Ha cedido cuando esperábamos que no se doblegara ante nadie.",
             "Para no doblegarte ante el poder, necesitas principios muy sólidos.",
             "Se han doblegado ante intereses que decían no compartir.",
         ], "nivel": "C2"},

        {"verbo": "sucumbir", "expresion": "sucumbir ante",
         "ejemplos": [
             "Sucumbió ante la tentación de tomar el camino más fácil.",
             "Ha sucumbido ante una presión que durante meses dijo poder soportar.",
             "Para no sucumbir ante las adversidades, rodéate de personas que te sostengan.",
             "Sucumbieron ante las mismas dinámicas que habían criticado en otros.",
         ], "nivel": "C2"},

        {"verbo": "comparecer", "expresion": "comparecer ante",
         "ejemplos": [
             "Compareció ante el tribunal con una serenidad que impresionó a todos.",
             "Ha sido citado a comparecer ante la comisión parlamentaria.",
             "Para comparecer ante un juez, es imprescindible contar con representación legal.",
             "Se ha negado a comparecer ante la comisión sin una garantía formal.",
         ], "nivel": "C2"},

        {"verbo": "capitular", "expresion": "capitular ante",
         "ejemplos": [
             "Capitularon ante las demandas del sector sin haber negociado lo suficiente.",
             "Se ha negado a capitular ante la presión mediática.",
             "Para no capitular ante algo, debes tener muy clara tu posición de salida.",
             "Capituló ante argumentos que en el fondo siempre supo que eran sólidos.",
         ], "nivel": "C2"},

        {"verbo": "inclinarse", "expresion": "inclinarse ante",
         "ejemplos": [
             "Se inclinó ante la autoridad del argumento, no ante la de la persona.",
             "Ha aprendido a inclinarse ante la evidencia sin que ello le cueste la dignidad.",
             "Para inclinarte ante algo, debes reconocer que tiene más valor que tu resistencia.",
             "Se inclinaron ante la decisión colectiva aunque no la compartían del todo.",
         ], "nivel": "C2"},

        {"verbo": "responder", "expresion": "responder ante",
         "ejemplos": [
             "Debe responder ante la sociedad por las decisiones que tomó en su cargo.",
             "Ha respondido ante el comité con una transparencia inusual.",
             "Para responder ante alguien, primero tienes que aceptar que te debes algo.",
             "Se ha respondido ante los accionistas con datos que muchos ponen en duda.",
         ], "nivel": "C1"},

        {"verbo": "claudicar", "expresion": "claudicar ante",
         "ejemplos": [
             "Claudicó ante la presión cuando todos esperábamos que aguantara.",
             "No ha claudicado ante nada ni nadie en todos estos años.",
             "Para no claudicar ante lo injusto, a veces hay que pagar un precio alto.",
             "Se claudicó ante intereses que siempre habían estado en conflicto con los propios.",
         ], "nivel": "C2"},

        {"verbo": "paralizarse", "expresion": "paralizarse ante",
         "ejemplos": [
             "Se paralizó ante la magnitud de lo que tenía que afrontar.",
             "Ha aprendido a no paralizarse ante la incertidumbre.",
             "Para no paralizarte ante el miedo, actúa aunque sea a pequeña escala.",
             "Se han paralizado ante una decisión que no admite más dilaciones.",
         ], "nivel": "C1"},

        {"verbo": "ceder", "expresion": "ceder ante",
         "ejemplos": [
             "Cedió ante la insistencia sin convencerse de que era lo correcto.",
             "Se ha negado a ceder ante una presión que considera ilegítima.",
             "Para ceder ante algo con dignidad, debes hacerlo por convicción, no por miedo.",
             "Han cedido ante argumentos que hasta hace poco rechazaban.",
         ], "nivel": "C1"},
    ],

    # ══════════════════════════════════════════
    #  + ENTRE
    # ══════════════════════════════════════════
    "entre": [
        {"verbo": "elegir", "expresion": "elegir entre",
         "ejemplos": [
             "Tuvo que elegir entre dos opciones que consideraba igualmente válidas.",
             "¿Has elegido alguna vez entre algo que querías y algo que debías hacer?",
             "Para elegir entre varias alternativas, primero debes conocerlas todas.",
             "Se ha elegido entre candidatos de perfiles muy distintos.",
         ], "nivel": "B2"},

        {"verbo": "distinguir", "expresion": "distinguir entre",
         "ejemplos": [
             "Saber distinguir entre lo urgente y lo importante es una habilidad escasa.",
             "Ha aprendido a distinguir entre crítica constructiva y ataque personal.",
             "Para distinguir entre dos opciones similares, busca los matices.",
             "Se distingue entre dos enfoques que a primera vista parecen idénticos.",
         ], "nivel": "B2"},

        {"verbo": "mediar", "expresion": "mediar entre",
         "ejemplos": [
             "Medió entre las dos partes con una paciencia admirable.",
             "Ha mediado entre departamentos que llevaban meses sin hablarse.",
             "Para mediar entre dos personas en conflicto, necesitas la confianza de ambas.",
             "Se ha mediado entre los intereses de los distintos grupos implicados.",
         ], "nivel": "C1"},

        {"verbo": "oscilar", "expresion": "oscilar entre",
         "ejemplos": [
             "Su estado de ánimo oscila entre la euforia y el abatimiento sin término medio.",
             "Las estimaciones oscilan entre el 15 y el 40 por ciento según la fuente.",
             "Ha oscilado entre dos posiciones sin decidirse claramente por ninguna.",
             "Para que los resultados no oscilen tanto, el proceso debe ser más estable.",
         ], "nivel": "C1"},

        {"verbo": "repartir", "expresion": "repartir entre",
         "ejemplos": [
             "Repartió las responsabilidades entre los miembros del equipo de forma equitativa.",
             "Se ha repartido el trabajo entre todos sin dejar a nadie fuera.",
             "Para repartir entre varios, primero hay que saber qué tiene cada uno.",
             "Han repartido los recursos entre los proyectos con más impacto potencial.",
         ], "nivel": "B2"},

        {"verbo": "debatirse", "expresion": "debatirse entre",
         "ejemplos": [
             "Se debatía entre la lealtad a sus principios y la presión del entorno.",
             "Se ha debatido entre dos opciones sin poder decantarse por ninguna.",
             "Para dejar de debatirte entre dos cosas, a veces basta con actuar.",
             "Lleva semanas debatiéndose entre lo que quiere y lo que considera correcto.",
         ], "nivel": "C1"},

        {"verbo": "intercambiar", "expresion": "intercambiar entre",
         "ejemplos": [
             "Intercambiaron impresiones entre los asistentes al término de la conferencia.",
             "Se han intercambiado documentos entre los equipos sin pasar por los canales habituales.",
             "Para que el conocimiento se intercambie entre los departamentos, hacen falta espacios comunes.",
             "Han intercambiado argumentos entre sí durante horas sin llegar a un acuerdo.",
         ], "nivel": "C1"},
    ],

    # ══════════════════════════════════════════
    #  + HACIA
    # ══════════════════════════════════════════
    "hacia": [
        {"verbo": "tender", "expresion": "tender hacia",
         "ejemplos": [
             "El sistema tiende hacia la concentración de poder si no hay contrapesos.",
             "Ha tendido siempre hacia soluciones que priorizan el largo plazo.",
             "Para que un proceso tienda hacia el equilibrio, necesita mecanismos de corrección.",
             "Se tiende hacia modelos más flexibles que los que conocíamos.",
         ], "nivel": "C1",
         "nota": "Tender hacia = moverse en una dirección. Tender a + infinitivo = tener tendencia a hacer algo."},

        {"verbo": "dirigirse", "expresion": "dirigirse hacia",
         "ejemplos": [
             "Se dirigió hacia la salida sin despedirse de nadie.",
             "La empresa se dirige hacia un modelo de negocio completamente distinto.",
             "Para saber hacia dónde te diriges, primero debes saber de dónde partes.",
             "Se han dirigido hacia mercados que antes ni consideraban.",
         ], "nivel": "B2"},

        {"verbo": "encaminarse", "expresion": "encaminarse hacia",
         "ejemplos": [
             "El proyecto se encamina hacia una fase que nadie anticipaba tan pronto.",
             "Se ha encaminado hacia una carrera que sus allegados no esperaban.",
             "Para encaminarte hacia donde quieres llegar, define el destino con precisión.",
             "Las negociaciones se encaminan hacia un acuerdo que parecía imposible.",
         ], "nivel": "C1"},

        {"verbo": "avanzar", "expresion": "avanzar hacia",
         "ejemplos": [
             "Avanzamos hacia un modelo que aún no entendemos del todo bien.",
             "Se ha avanzado hacia posiciones más matizadas gracias al diálogo.",
             "Para avanzar hacia algo, hay que estar dispuesto a dejar algo atrás.",
             "Ha avanzado hacia sus objetivos con una constancia que pocos mantienen.",
         ], "nivel": "B2"},

        {"verbo": "orientarse", "expresion": "orientarse hacia",
         "ejemplos": [
             "La política educativa se orienta hacia un enfoque más competencial.",
             "Se ha orientado hacia áreas de mayor impacto social.",
             "Para orientarte hacia algo nuevo, primero debes soltar lo que ya conoces.",
             "Han orientado todos sus esfuerzos hacia la sostenibilidad.",
         ], "nivel": "C1"},

        {"verbo": "moverse", "expresion": "moverse hacia",
         "ejemplos": [
             "El sector se mueve hacia modelos de economía circular.",
             "Se ha movido hacia posiciones más moderadas con el paso del tiempo.",
             "Para moverte hacia el cambio, a veces basta con dar el primer pequeño paso.",
             "Han empezado a moverse hacia soluciones que antes rechazaban.",
         ], "nivel": "B2"},
    ],

    # ══════════════════════════════════════════
    #  + TRAS
    # ══════════════════════════════════════════
    "tras": [
        {"verbo": "ir", "expresion": "ir tras",
         "ejemplos": [
             "Ha ido tras ese objetivo con una determinación que asombra a todos.",
             "No vale la pena ir tras algo que no te va a hacer más feliz.",
             "Para ir tras lo que quieres, primero tienes que saber qué es.",
             "Se ha ido tras la solución equivocada durante demasiado tiempo.",
         ], "nivel": "C1"},

        {"verbo": "andar", "expresion": "andar tras",
         "ejemplos": [
             "Lleva meses andando tras una respuesta que nadie parece querer darle.",
             "Ha andado tras esa oportunidad sin éxito durante años.",
             "Para dejar de andar tras algo que no llega, a veces hay que redefinir el objetivo.",
             "Anda tras una verdad que quizás no quiera encontrar.",
         ], "nivel": "C1"},

        {"verbo": "correr", "expresion": "correr tras",
         "ejemplos": [
             "Ha corrido tras el reconocimiento sin darse cuenta de lo que tiene.",
             "No corras tras quien no se detiene a esperarte.",
             "Para dejar de correr tras algo, primero tienes que entender por qué lo persigues.",
             "Se ha corrido tras soluciones rápidas que nunca han resuelto el problema de fondo.",
         ], "nivel": "C1"},

        {"verbo": "esconderse", "expresion": "esconderse tras",
         "ejemplos": [
             "Se esconde tras una apariencia de seguridad que no refleja lo que siente.",
             "Ha usado el humor para esconderse tras él en momentos de vulnerabilidad.",
             "Para dejar de esconderte tras las excusas, primero reconócelas como tales.",
             "Se han escondido tras tecnicismos para no dar una respuesta directa.",
         ], "nivel": "C2"},
    ],
}

# Verbos con doble preposición y cambio de significado
DOUBLE_PREP: List[Dict] = [
    {
        "verbo": "pensar",
        "casos": [
            {"prep": "en", "significado": "tener en mente, reflexionar sobre algo o alguien",
             "ejemplo": "Pienso en ti constantemente."},
            {"prep": "de", "significado": "opinar, tener una valoración sobre algo",
             "ejemplo": "¿Qué piensas de su última decisión?"},
        ]
    },
    {
        "verbo": "contar",
        "casos": [
            {"prep": "con", "significado": "disponer de algo o confiar en alguien",
             "ejemplo": "Cuento contigo para el proyecto."},
            {"prep": "de", "significado": "narrar o hablar sobre algo (registro coloquial)",
             "ejemplo": "Cuéntame de tu viaje."},
        ]
    },
    {
        "verbo": "hablar",
        "casos": [
            {"prep": "de", "significado": "tratar un tema, referirse a algo",
             "ejemplo": "Hablamos de política hasta las tantas."},
            {"prep": "con", "significado": "comunicarse, tener una conversación con alguien",
             "ejemplo": "Ayer hablé con mi jefa y fue muy bien."},
            {"prep": "sobre", "significado": "reflexionar o debatir sobre un tema con más profundidad",
             "ejemplo": "Hablamos largo y tendido sobre las implicaciones del proyecto."},
        ]
    },
    {
        "verbo": "comprometerse",
        "casos": [
            {"prep": "a", "significado": "obligarse a realizar una acción concreta",
             "ejemplo": "Me comprometí a entregar el informe el lunes."},
            {"prep": "con", "significado": "alinearse con una causa, idea o persona",
             "ejemplo": "Se comprometió con la lucha contra el cambio climático."},
        ]
    },
    {
        "verbo": "tratar",
        "casos": [
            {"prep": "de", "significado": "intentar (+ infinitivo) o versar sobre algo",
             "ejemplo": "Trato de no perder la calma. / El libro trata de la memoria histórica."},
            {"prep": "con", "significado": "relacionarse o tener trato con alguien",
             "ejemplo": "Trato con personas muy diversas en mi trabajo."},
        ]
    },
    {
        "verbo": "quedar",
        "casos": [
            {"prep": "en", "significado": "acordar algo con alguien",
             "ejemplo": "Quedamos en vernos el jueves a las siete."},
            {"prep": "con", "significado": "citarse con alguien",
             "ejemplo": "He quedado con Ana para tomar algo."},
        ]
    },
    {
        "verbo": "acabar",
        "casos": [
            {"prep": "de", "significado": "acción recién completada (perífrasis verbal)",
             "ejemplo": "Acabo de leer tu correo."},
            {"prep": "con", "significado": "poner fin a algo o alguien",
             "ejemplo": "Hay que acabar con esta situación de una vez."},
            {"prep": "por", "significado": "terminar haciendo algo tras un proceso largo",
             "ejemplo": "Acabé por darle la razón aunque no quería."},
        ]
    },
    {
        "verbo": "enfadarse",
        "casos": [
            {"prep": "con", "significado": "enfadarse con una persona (receptor de la emoción)",
             "ejemplo": "Se enfadó conmigo por una tontería."},
            {"prep": "por", "significado": "enfadarse a causa de algo (motivo de la emoción)",
             "ejemplo": "Me enfadé por la falta de respeto, no por lo que dijeron."},
        ]
    },
    {
        "verbo": "indignarse",
        "casos": [
            {"prep": "con", "significado": "indignarse con una persona (receptor)",
             "ejemplo": "Me indigné con ella por su actitud tan desdeñosa."},
            {"prep": "por", "significado": "indignarse a causa de algo (motivo)",
             "ejemplo": "Se indignó por la impunidad con la que se actúa."},
        ]
    },
    {
        "verbo": "luchar",
        "casos": [
            {"prep": "por", "significado": "combatir para conseguir o defender algo",
             "ejemplo": "Lucha por sus ideales con una convicción admirable."},
            {"prep": "contra", "significado": "combatir en oposición a algo o alguien",
             "ejemplo": "Ha luchado toda su vida contra la injusticia."},
        ]
    },
    {
        "verbo": "pronunciarse",
        "casos": [
            {"prep": "sobre", "significado": "dar una opinión o posición sobre un asunto",
             "ejemplo": "Se pronunció sobre el tema con una claridad poco habitual."},
            {"prep": "contra", "significado": "declarar oposición a algo",
             "ejemplo": "Se pronunció contra la medida con argumentos irrebatibles."},
        ]
    },
    {
        "verbo": "volver",
        "casos": [
            {"prep": "a", "significado": "repetir una acción (perífrasis)",
             "ejemplo": "Volvió a llamar tres veces sin que nadie contestara."},
            {"prep": "sobre", "significado": "retomar un tema o asunto ya tratado",
             "ejemplo": "Volvió sobre el asunto cuando nadie lo esperaba."},
        ]
    },
]

# Ejercicios de hueco — frase con ___
GAP_EXERCISES: List[Dict] = [
    {"frase": "Llevaba años soñando ___ un lugar así y por fin lo ha encontrado.",
     "respuesta": "con", "verbo": "soñar con",
     "explicacion": "Soñar con + sustantivo o infinitivo: expresa deseo profundo o lo que aparece en sueños."},
    {"frase": "El nuevo plan adolece ___ una falta total de concreción.",
     "respuesta": "de", "verbo": "adolecer de",
     "explicacion": "Adolecer de: carecer de algo o sufrir un defecto determinado."},
    {"frase": "Se abstuvo ___ opinar hasta conocer todos los datos.",
     "respuesta": "de", "verbo": "abstenerse de",
     "explicacion": "Abstenerse de + infinitivo: contenerse de hacer algo."},
    {"frase": "La medida redunda ___ beneficio de los consumidores.",
     "respuesta": "en", "verbo": "redundar en",
     "explicacion": "Redundar en: tener como consecuencia, repercutir en algo."},
    {"frase": "Se valió ___ todos sus contactos para conseguir el contrato.",
     "respuesta": "de", "verbo": "valerse de",
     "explicacion": "Valerse de: aprovecharse de algo o alguien como medio o instrumento."},
    {"frase": "La crítica se cebó especialmente ___ su segunda novela.",
     "respuesta": "con", "verbo": "cebarse con",
     "explicacion": "Cebarse con: ensañarse con alguien o algo de forma desproporcionada."},
    {"frase": "El documento ahonda ___ las causas estructurales de la crisis.",
     "respuesta": "en", "verbo": "ahondar en",
     "explicacion": "Ahondar en: profundizar, explorar con mayor detalle un tema o asunto."},
    {"frase": "Por fin se atrevió ___ decir en público lo que todos pensaban.",
     "respuesta": "a", "verbo": "atreverse a",
     "explicacion": "Atreverse a + infinitivo: tener el valor de hacer algo."},
    {"frase": "Aboga ___ una reforma profunda del sistema de pensiones.",
     "respuesta": "por", "verbo": "abogar por",
     "explicacion": "Abogar por: defender una causa o idea públicamente."},
    {"frase": "Nunca había incidido tanto ___ la importancia del contexto.",
     "respuesta": "en", "verbo": "incidir en",
     "explicacion": "Incidir en: hacer hincapié en algo o influir en ello."},
    {"frase": "Se jactaba ___ conocer a los personajes más poderosos del país.",
     "respuesta": "de", "verbo": "jactarse de",
     "explicacion": "Jactarse de: presumir con arrogancia de algo."},
    {"frase": "La empresa decidió prescindir ___ varios altos cargos.",
     "respuesta": "de", "verbo": "prescindir de",
     "explicacion": "Prescindir de: renunciar a algo o alguien, considerarlo innecesario."},
    {"frase": "Me comprometí ___ entregar el informe antes del plazo.",
     "respuesta": "a", "verbo": "comprometerse a",
     "explicacion": "Comprometerse a + infinitivo: obligarse a realizar una acción concreta."},
    {"frase": "La medida atenta ___ los derechos más fundamentales de los ciudadanos.",
     "respuesta": "contra", "verbo": "atentar contra",
     "explicacion": "Atentar contra: ir en contra de algo de forma grave o dañina."},
    {"frase": "Se pronunció ___ la propuesta con argumentos que nadie pudo rebatir.",
     "respuesta": "contra", "verbo": "pronunciarse contra",
     "explicacion": "Pronunciarse contra: declarar públicamente oposición a algo."},
    {"frase": "Meditó ___ su decisión durante días antes de dar ninguna respuesta.",
     "respuesta": "sobre", "verbo": "meditar sobre",
     "explicacion": "Meditar sobre: reflexionar de forma profunda y pausada sobre algo."},
    {"frase": "Se rebeló ___ un sistema que consideraba profundamente injusto.",
     "respuesta": "contra", "verbo": "rebelarse contra",
     "explicacion": "Rebelarse contra: resistirse o levantarse contra algo o alguien con autoridad."},
    {"frase": "Capitularon ___ las demandas del sector sin haber negociado lo suficiente.",
     "respuesta": "ante", "verbo": "capitular ante",
     "explicacion": "Capitular ante: rendirse o ceder ante una presión o autoridad."},
    {"frase": "El sistema tiende ___ la concentración de poder si no existen contrapesos.",
     "respuesta": "hacia", "verbo": "tender hacia",
     "explicacion": "Tender hacia: moverse o inclinarse en una dirección determinada."},
    {"frase": "Las negociaciones se encaminan ___ un acuerdo que parecía imposible.",
     "respuesta": "hacia", "verbo": "encaminarse hacia",
     "explicacion": "Encaminarse hacia: dirigirse o avanzar en una determinada dirección."},
]

# Ejercicios de detección de error
ERROR_EXERCISES: List[Dict] = [
    {"frase_incorrecta": "Me arrepiento *con* no haber asistido a aquella conferencia tan importante.",
     "prep_incorrecta": "con", "prep_correcta": "de",
     "verbo": "arrepentirse de",
     "frase_correcta": "Me arrepiento de no haber asistido a aquella conferencia tan importante.",
     "explicacion": "Arrepentirse rige siempre 'de', no 'con'."},
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
    {"frase_incorrecta": "Se pronunció *de* la propuesta con argumentos muy sólidos.",
     "prep_incorrecta": "de", "prep_correcta": "sobre / contra",
     "verbo": "pronunciarse sobre / contra",
     "frase_correcta": "Se pronunció sobre la propuesta con argumentos muy sólidos. (O: se pronunció contra la propuesta.)",
     "explicacion": "Pronunciarse lleva 'sobre' para dar opinión o 'contra' para expresar oposición. 'De' no es correcto aquí."},
    {"frase_incorrecta": "Capitularon *de* las demandas del sector sin haber negociado nada.",
     "prep_incorrecta": "de", "prep_correcta": "ante",
     "verbo": "capitular ante",
     "frase_correcta": "Capitularon ante las demandas del sector sin haber negociado nada.",
     "explicacion": "Capitular lleva 'ante': cederse ante una presión o autoridad."},
    {"frase_incorrecta": "Se rebeló *de* un sistema que consideraba profundamente injusto.",
     "prep_incorrecta": "de", "prep_correcta": "contra",
     "verbo": "rebelarse contra",
     "frase_correcta": "Se rebeló contra un sistema que consideraba profundamente injusto.",
     "explicacion": "Rebelarse lleva 'contra', no 'de'."},
    {"frase_incorrecta": "La política educativa se orienta *a* un enfoque más competencial.",
     "prep_incorrecta": "a", "prep_correcta": "hacia",
     "verbo": "orientarse hacia",
     "frase_correcta": "La política educativa se orienta hacia un enfoque más competencial.",
     "explicacion": "Orientarse lleva 'hacia' cuando indica dirección o tendencia, no 'a'."},
]

PREPS = ["de", "a", "con", "en", "por", "sobre", "contra", "ante", "entre", "hacia", "tras"]
CATEGORY_LABELS = {
    "de": "Verbos + DE",
    "a": "Verbos + A",
    "con": "Verbos + CON",
    "en": "Verbos + EN",
    "por": "Verbos + POR",
    "sobre": "Verbos + SOBRE",
    "contra": "Verbos + CONTRA",
    "ante": "Verbos + ANTE",
    "entre": "Verbos + ENTRE",
    "hacia": "Verbos + HACIA",
    "tras": "Verbos + TRAS",
}

NIVEL_COLORS = {"B2": "#3b82f6", "C1": "#8b5cf6", "C2": "#ef4444"}

# Mapa automático: verbo_base → [todas las preps válidas en DATA]
_VERB_TO_PREPS: Dict[str, List[str]] = {}
for _prep, _items in DATA.items():
    for _it in _items:
        _VERB_TO_PREPS.setdefault(_it["verbo"], [])
        if _prep not in _VERB_TO_PREPS[_it["verbo"]]:
            _VERB_TO_PREPS[_it["verbo"]].append(_prep)



# ─────────────────────────────────────────────
#  BASE DE DATOS — CONECTORES
# ─────────────────────────────────────────────

CONECTORES: List[Dict] = [
    # 1. Contraste y concesión
    {"conector": "no obstante",
     "funcion": "Contraste y concesión",
     "matiz": "Introduce un límite o matiz a lo anterior. Más formal que 'sin embargo'. No implica oposición total.",
     "ejemplos": [
         "La propuesta era interesante; no obstante, presentaba graves lagunas metodológicas.",
         "Reconoció sus errores; no obstante, se negó a dimitir.",
     ], "nivel": "C1"},
    {"conector": "por el contrario",
     "funcion": "Contraste y concesión",
     "matiz": "Señala una oposición directa y total entre dos ideas. No matiza: niega completamente lo anterior.",
     "ejemplos": [
         "No se trata de una medida provisional; por el contrario, pretende ser estructural.",
         "Su primera novela fue un fracaso; por el contrario, la segunda batió todos los récords.",
     ], "nivel": "C1"},
    {"conector": "ahora bien",
     "funcion": "Contraste y concesión",
     "matiz": "Acepta algo y a continuación introduce una condición o reserva importante.",
     "ejemplos": [
         "Podemos debatir la propuesta; ahora bien, debe quedar claro quién asume la responsabilidad.",
         "Acepto las condiciones; ahora bien, exijo que consten por escrito.",
     ], "nivel": "C1"},
    {"conector": "si bien es cierto que",
     "funcion": "Contraste y concesión",
     "matiz": "Concede algo antes de introducir una objeción importante. Estructura muy frecuente en textos académicos.",
     "ejemplos": [
         "Si bien es cierto que los resultados mejoraron, el margen sigue siendo insuficiente.",
         "Si bien es cierto que colaboró, su aportación fue más bien discreta.",
     ], "nivel": "C2"},
    {"conector": "aun así",
     "funcion": "Contraste y concesión",
     "matiz": "A pesar de lo dicho, la consecuencia no es la esperada. Indica que el obstáculo no fue suficiente.",
     "ejemplos": [
         "Las condiciones eran adversas; aun así, lograron terminar el proyecto a tiempo.",
         "Le advirtieron del riesgo; aun así, decidió seguir adelante.",
     ], "nivel": "B2"},
    {"conector": "a pesar de que",
     "funcion": "Contraste y concesión",
     "matiz": "Concesión con verbo conjugado. Equivale a 'aunque' con registro más formal.",
     "ejemplos": [
         "A pesar de que los datos no eran concluyentes, se tomó la decisión.",
         "A pesar de que insistió varias veces, nadie le hizo caso.",
     ], "nivel": "B2"},
    {"conector": "por mucho que",
     "funcion": "Contraste y concesión",
     "matiz": "Concesión de grado máximo: aunque el esfuerzo sea el mayor posible, el resultado no cambia.",
     "ejemplos": [
         "Por mucho que lo intente, no consigue concentrarse en un entorno ruidoso.",
         "Por mucho que se esfuercen, el plazo es imposible de cumplir.",
     ], "nivel": "C1"},

    # 2. Causa y origen
    {"conector": "puesto que",
     "funcion": "Causa y origen",
     "matiz": "Causa conocida por ambos interlocutores. Más argumentativo y formal que 'porque'.",
     "ejemplos": [
         "Puesto que ya se han presentado las pruebas, no hay lugar para más dilaciones.",
         "Puesto que nadie se opuso, se aprobó por unanimidad.",
     ], "nivel": "C1"},
    {"conector": "dado que",
     "funcion": "Causa y origen",
     "matiz": "Presenta la causa como un dato previo, establecido y conocido.",
     "ejemplos": [
         "Dado que la situación se ha deteriorado, urge tomar medidas inmediatas.",
         "Dado que no hay consenso, se pospondrá la votación.",
     ], "nivel": "C1"},
    {"conector": "ya que",
     "funcion": "Causa y origen",
     "matiz": "Causal frecuente, ligeramente menos formal que 'puesto que' o 'dado que'.",
     "ejemplos": [
         "Aprovecharé para revisar el documento, ya que de todas formas tenía que abrirlo.",
         "Ya que estamos, deberíamos hablar del presupuesto.",
     ], "nivel": "B2"},
    {"conector": "habida cuenta de que",
     "funcion": "Causa y origen",
     "matiz": "Muy formal. Introduce una causa que se da por sabida y que justifica plenamente lo que sigue.",
     "ejemplos": [
         "Habida cuenta de que los plazos han vencido, no cabe otra alternativa.",
         "Habida cuenta de que el mercado ha cambiado, la estrategia debe revisarse.",
     ], "nivel": "C2"},
    {"conector": "merced a",
     "funcion": "Causa y origen",
     "matiz": "Causa positiva (equivale a 'gracias a'). Registro muy culto o literario. Nunca para causas negativas.",
     "ejemplos": [
         "Merced a su intervención, el conflicto pudo resolverse sin más daños.",
         "Lograron sobrevivir merced a la solidaridad de los vecinos.",
     ], "nivel": "C2"},
    {"conector": "a causa de",
     "funcion": "Causa y origen",
     "matiz": "Causa directa, frecuentemente negativa o neutral. Va seguido de sustantivo.",
     "ejemplos": [
         "El proyecto se canceló a causa de la falta de financiación.",
         "Tuvo que retirarse a causa de una lesión.",
     ], "nivel": "B2"},
    {"conector": "debido a",
     "funcion": "Causa y origen",
     "matiz": "Similar a 'a causa de'. Neutro, puede introducir causas positivas o negativas.",
     "ejemplos": [
         "El retraso se produjo debido a un fallo técnico inesperado.",
         "Debido a su experiencia, fue la candidata más valorada.",
     ], "nivel": "B2"},

    # 3. Consecuencia y resultado
    {"conector": "por consiguiente",
     "funcion": "Consecuencia y resultado",
     "matiz": "Consecuencia lógica y directa. Registro formal. Va seguido de indicativo.",
     "ejemplos": [
         "Los datos son insuficientes; por consiguiente, no se puede emitir un veredicto.",
         "Incumplió el contrato; por consiguiente, deberá hacer frente a las penalizaciones.",
     ], "nivel": "C1"},
    {"conector": "en consecuencia",
     "funcion": "Consecuencia y resultado",
     "matiz": "Equivale a 'por tanto'. Muy habitual en textos argumentativos y académicos.",
     "ejemplos": [
         "El modelo ha demostrado ser ineficiente; en consecuencia, será sustituido.",
         "No se cumplieron los objetivos; en consecuencia, se revisará la estrategia.",
     ], "nivel": "C1"},
    {"conector": "de ahí que",
     "funcion": "Consecuencia y resultado",
     "matiz": "SIEMPRE exige subjuntivo. Presenta la consecuencia como algo que se deriva de forma natural.",
     "ejemplos": [
         "La demanda cayó un 30 %; de ahí que se hayan recortado los turnos de producción.",
         "Nadie confía en él; de ahí que sus propuestas no prosperen.",
     ], "nivel": "C2"},
    {"conector": "por ende",
     "funcion": "Consecuencia y resultado",
     "matiz": "Muy formal o literario. Equivale a 'por tanto'. Poco frecuente en lengua oral.",
     "ejemplos": [
         "Es un argumento circular y, por ende, inválido desde el punto de vista lógico.",
         "Carece de legitimidad y, por ende, de autoridad moral para juzgar.",
     ], "nivel": "C2"},
    {"conector": "así pues",
     "funcion": "Consecuencia y resultado",
     "matiz": "Retoma lo dicho y extrae una conclusión o consecuencia práctica. Más ligero que 'por consiguiente'.",
     "ejemplos": [
         "Así pues, queda claro que el enfoque actual no funciona.",
         "Así pues, procederemos tal y como se acordó en la reunión anterior.",
     ], "nivel": "C1"},

    # 4. Adición y continuidad
    {"conector": "asimismo",
     "funcion": "Adición y continuidad",
     "matiz": "Añade información del mismo tipo o relevancia. Registro formal.",
     "ejemplos": [
         "El informe analiza las causas; asimismo, propone soluciones concretas.",
         "Asimismo, cabe señalar que los plazos han sido sistemáticamente incumplidos.",
     ], "nivel": "C1"},
    {"conector": "es más",
     "funcion": "Adición y continuidad",
     "matiz": "Añade algo que refuerza o supera lo anterior. Introduce una gradación ascendente (positiva o negativa).",
     "ejemplos": [
         "No solo no colaboró; es más, obstaculizó activamente el proceso.",
         "La reforma es necesaria; es más, resulta urgente si se quiere evitar el colapso.",
     ], "nivel": "C1"},
    {"conector": "por añadidura",
     "funcion": "Adición y continuidad",
     "matiz": "Lo añadido es algo extra e inesperado, que se suma a algo ya de por sí significativo.",
     "ejemplos": [
         "El proyecto fracasó y, por añadidura, generó un conflicto interno sin precedentes.",
         "Perdió el empleo y, por añadidura, tuvo que devolver la subvención.",
     ], "nivel": "C2"},
    {"conector": "para colmo",
     "funcion": "Adición y continuidad",
     "matiz": "Añade algo NEGATIVO que empeora aún más una situación ya mala. Nunca para lo positivo.",
     "ejemplos": [
         "Llegó tarde, se equivocó en la presentación y, para colmo, discutió con el cliente.",
         "Ya era un día complicado y, para colmo, empezó a llover a cántaros.",
     ], "nivel": "C1"},
    {"conector": "por si fuera poco",
     "funcion": "Adición y continuidad",
     "matiz": "Similar a 'para colmo'. Añade un elemento negativo que colma la medida de algo ya malo.",
     "ejemplos": [
         "El presupuesto se agotó, el equipo se dispersó y, por si fuera poco, el cliente retiró su confianza.",
         "Llegó sin avisar y, por si fuera poco, esperaba que le preparáramos una sala.",
     ], "nivel": "C1"},

    # 5. Hipótesis y condición
    {"conector": "siempre y cuando",
     "funcion": "Hipótesis y condición",
     "matiz": "Condición positiva y restrictiva: la acción solo es posible si se cumple esa condición.",
     "ejemplos": [
         "Puedo apoyar la propuesta, siempre y cuando se garantice la transparencia del proceso.",
         "Participaremos en el proyecto, siempre y cuando se respeten nuestras condiciones.",
     ], "nivel": "C1"},
    {"conector": "a condición de que",
     "funcion": "Hipótesis y condición",
     "matiz": "Introduce una condición explícita y formal. Más enfático que 'si'.",
     "ejemplos": [
         "Firmaré el acuerdo a condición de que se incluya una cláusula de revisión anual.",
         "Acepta el cargo a condición de que le den plena autonomía.",
     ], "nivel": "C1"},
    {"conector": "a menos que",
     "funcion": "Hipótesis y condición",
     "matiz": "Condición negativa: la acción ocurre salvo que se cumpla esa condición. Lo contrario de 'siempre y cuando'.",
     "ejemplos": [
         "No habrá cambios a menos que la situación se deteriore significativamente.",
         "Seguiremos con el plan inicial, a menos que surja algún imprevisto.",
     ], "nivel": "C1"},
    {"conector": "en caso de que",
     "funcion": "Hipótesis y condición",
     "matiz": "Contempla un escenario posible pero no seguro. Tono más neutro que los anteriores.",
     "ejemplos": [
         "En caso de que no haya acuerdo, se recurrirá al arbitraje.",
         "En caso de que surja alguna duda, no dudes en consultarme.",
     ], "nivel": "B2"},
    {"conector": "suponiendo que",
     "funcion": "Hipótesis y condición",
     "matiz": "Plantea una hipótesis como punto de partida para razonar. A menudo escéptico.",
     "ejemplos": [
         "Suponiendo que los datos sean correctos, las conclusiones son demoledoras.",
         "Suponiendo que acepten la oferta, ¿cuándo podríamos empezar?",
     ], "nivel": "C1"},

    # 6. Estructuración y orden
    {"conector": "en primer lugar",
     "funcion": "Estructuración y orden",
     "matiz": "Abre una enumeración o un argumento estructurado. Siempre exige continuación explícita.",
     "ejemplos": [
         "En primer lugar, es preciso delimitar el alcance del problema.",
         "En primer lugar, agradeceré su presencia; a continuación, pasaré a los detalles.",
     ], "nivel": "B2"},
    {"conector": "acto seguido",
     "funcion": "Estructuración y orden",
     "matiz": "Inmediatamente después, en el tiempo o en el discurso. Más narrativo que 'a continuación'.",
     "ejemplos": [
         "Firmaron el contrato y, acto seguido, brindaron por el acuerdo.",
         "Presentó sus credenciales y, acto seguido, tomó la palabra.",
     ], "nivel": "C1"},
    {"conector": "en lo que respecta a",
     "funcion": "Estructuración y orden",
     "matiz": "Introduce un nuevo subtema dentro del discurso. Equivale a 'en cuanto a' con más formalidad.",
     "ejemplos": [
         "En lo que respecta a la financiación, aún quedan flecos por resolver.",
         "En lo que respecta a los plazos, el calendario es muy ajustado.",
     ], "nivel": "C1"},
    {"conector": "por lo que se refiere a",
     "funcion": "Estructuración y orden",
     "matiz": "Equivale a 'en lo que respecta a'. Muy frecuente en textos académicos y administrativos.",
     "ejemplos": [
         "Por lo que se refiere a los resultados, son más prometedores de lo esperado.",
         "Por lo que se refiere al presupuesto, habrá que buscar fuentes alternativas.",
     ], "nivel": "C1"},

    # 7. Reformulación y aclaración
    {"conector": "es decir",
     "funcion": "Reformulación y aclaración",
     "matiz": "Reformula lo dicho de forma más clara o precisa. El más frecuente y neutro de su categoría.",
     "ejemplos": [
         "El proyecto es inviable; es decir, no puede ejecutarse con los recursos actuales.",
         "La propuesta carece de rigor; es decir, no está respaldada por datos sólidos.",
     ], "nivel": "B2"},
    {"conector": "dicho de otro modo",
     "funcion": "Reformulación y aclaración",
     "matiz": "Reformulación más enfática: la segunda versión es más clara o contundente que la primera.",
     "ejemplos": [
         "El modelo es insostenible; dicho de otro modo, colapsará en menos de dos años.",
         "No hay consenso; dicho de otro modo, partimos de cero.",
     ], "nivel": "C1"},
    {"conector": "mejor dicho",
     "funcion": "Reformulación y aclaración",
     "matiz": "Corrige o matiza lo que se acaba de decir, buscando mayor precisión. No reformula: rectifica.",
     "ejemplos": [
         "Fue un malentendido; mejor dicho, una cadena de malentendidos.",
         "Lo consideramos un riesgo; mejor dicho, una certeza.",
     ], "nivel": "C1"},
    {"conector": "a saber",
     "funcion": "Reformulación y aclaración",
     "matiz": "Introduce una enumeración o especificación explícita de lo anterior. Registro formal.",
     "ejemplos": [
         "Se identificaron tres problemas, a saber: financiación, gestión y comunicación.",
         "La propuesta incluye varios ejes, a saber: formación, innovación y digitalización.",
     ], "nivel": "C2"},

    # 8. Ejemplificación y digresión
    {"conector": "pongamos por caso",
     "funcion": "Ejemplificación y digresión",
     "matiz": "Introduce un ejemplo hipotético para ilustrar un argumento. Más formal que 'por ejemplo'.",
     "ejemplos": [
         "Pongamos por caso que la empresa externaliza ese servicio: ¿qué ocurre con los empleados?",
         "Pongamos por caso que no se alcanza el quórum; el proceso se paralizaría.",
     ], "nivel": "C2"},
    {"conector": "sin ir más lejos",
     "funcion": "Ejemplificación y digresión",
     "matiz": "Introduce un ejemplo cercano y concreto, casi a mano. Implica que no hace falta buscar lejos.",
     "ejemplos": [
         "La situación es preocupante; sin ir más lejos, esta semana han cerrado tres empresas del sector.",
         "Sin ir más lejos, el caso de Finlandia demuestra que es posible.",
     ], "nivel": "C1"},
    {"conector": "dicho sea de paso",
     "funcion": "Ejemplificación y digresión",
     "matiz": "Introduce una digresión o acotación que el hablante considera secundaria pero relevante.",
     "ejemplos": [
         "Su gestión fue mediocre y, dicho sea de paso, bastante cuestionable desde el punto de vista ético.",
         "El informe, dicho sea de paso, fue redactado en menos de 48 horas.",
     ], "nivel": "C2"},
    {"conector": "a propósito",
     "funcion": "Ejemplificación y digresión",
     "matiz": "Introduce una digresión relacionada con el tema. 'A propósito de' = acerca de (registro formal).",
     "ejemplos": [
         "A propósito, ¿has leído el artículo que publicó ayer sobre ese tema?",
         "A propósito de lo que decías, me recuerda a un caso similar que estudié.",
     ], "nivel": "C1"},

    # 9. Conclusión y cierre
    {"conector": "en definitiva",
     "funcion": "Conclusión y cierre",
     "matiz": "Resume y cierra el argumento con una valoración global y rotunda. Registro formal.",
     "ejemplos": [
         "En definitiva, el problema no es técnico sino político.",
         "En definitiva, lo que se pide es responsabilidad y transparencia.",
     ], "nivel": "B2"},
    {"conector": "en resumidas cuentas",
     "funcion": "Conclusión y cierre",
     "matiz": "Introduce un resumen simplificado. Registro más coloquial que 'en definitiva' o 'en suma'.",
     "ejemplos": [
         "En resumidas cuentas, el proyecto no era viable desde el principio.",
         "En resumidas cuentas, nadie quería asumir la responsabilidad.",
     ], "nivel": "C1"},
    {"conector": "al fin y al cabo",
     "funcion": "Conclusión y cierre",
     "matiz": "Relativiza o concede algo después de considerarlo todo. A menudo introduce una conclusión inesperada.",
     "ejemplos": [
         "Al fin y al cabo, todos cometemos errores; lo importante es aprender de ellos.",
         "Al fin y al cabo, eso es lo que realmente importa.",
     ], "nivel": "B2"},
    {"conector": "en suma",
     "funcion": "Conclusión y cierre",
     "matiz": "Resume de forma concisa y formal. Más culto que 'en resumidas cuentas'.",
     "ejemplos": [
         "En suma, la propuesta es sólida y merece ser considerada seriamente.",
         "En suma, se trata de una oportunidad que no debemos dejar pasar.",
     ], "nivel": "C1"},
    {"conector": "a modo de cierre",
     "funcion": "Conclusión y cierre",
     "matiz": "Señala explícitamente que se está cerrando el discurso. Habitual en presentaciones orales o ensayos.",
     "ejemplos": [
         "A modo de cierre, cabe recordar que todo proceso de cambio requiere tiempo y consenso.",
         "A modo de cierre, quisiera agradecer la atención prestada.",
     ], "nivel": "C1"},

    # 10. Énfasis y afirmación
    {"conector": "cabe destacar que",
     "funcion": "Énfasis y afirmación",
     "matiz": "Señala algo que merece atención especial. Registro académico o formal.",
     "ejemplos": [
         "Cabe destacar que los resultados superaron todas las previsiones iniciales.",
         "Cabe destacar que esta es la primera vez que se aplica esta metodología.",
     ], "nivel": "C1"},
    {"conector": "de hecho",
     "funcion": "Énfasis y afirmación",
     "matiz": "Refuerza o confirma lo dicho con un dato concreto o una realidad verificable.",
     "ejemplos": [
         "Se dijo que era imposible; de hecho, se logró en la mitad del tiempo previsto.",
         "De hecho, ya lo habíamos advertido hace meses.",
     ], "nivel": "B2"},
    {"conector": "esencialmente",
     "funcion": "Énfasis y afirmación",
     "matiz": "Señala lo nuclear, lo fundamental del argumento, dejando lo accesorio de lado.",
     "ejemplos": [
         "El debate es, esencialmente, una cuestión de valores, no de datos.",
         "Esencialmente, lo que se les pide es coherencia.",
     ], "nivel": "C1"},
    {"conector": "sobre todo",
     "funcion": "Énfasis y afirmación",
     "matiz": "Destaca un elemento por encima de los demás. Más coloquial que 'esencialmente' o 'cabe destacar'.",
     "ejemplos": [
         "Valoro su honestidad, sobre todo en momentos tan difíciles.",
         "Sobre todo, hay que evitar que la situación se repita.",
     ], "nivel": "B2"},
]


# ─────────────────────────────────────────────
#  EJERCICIOS — RELLENA EL HUECO
# ─────────────────────────────────────────────

GAP_EJERCICIOS: List[Dict] = [
    {"frase": "___ los plazos han vencido, no cabe otra alternativa que iniciar el proceso legal.",
     "respuesta": ["Habida cuenta de que"],
     "alternativas": ["Ya que", "Habida cuenta de que", "Merced a", "Dado que"],
     "explicacion": "'Habida cuenta de que' es la única opción de registro plenamente C2 aquí. 'Ya que' o 'dado que' son causales válidos pero de registro inferior.",
     "nivel": "C2"},
    {"frase": "La propuesta era técnicamente correcta; ___, adolecía de una falta total de visión estratégica.",
     "respuesta": ["no obstante", "sin embargo"],
     "alternativas": ["sin embargo", "no obstante", "por el contrario", "es más"],
     "explicacion": "✅ Válidos: 'no obstante' y 'sin embargo' (ambos introducen un matiz o límite a lo anterior). ❌ 'Por el contrario' implicaría oposición total; 'es más' añadiría en vez de contrastar.",
     "nivel": "C1"},
    {"frase": "La demanda cayó un 40 % en un trimestre, ___ se hayan paralizado todas las inversiones.",
     "respuesta": ["de ahí que"],
     "alternativas": ["por consiguiente", "de ahí que", "así pues", "en consecuencia"],
     "explicacion": "'De ahí que' es el único que exige subjuntivo ('hayan'). Los demás consecutivos van con indicativo y no encajan con la forma verbal de la frase.",
     "nivel": "C2"},
    {"frase": "El modelo es insostenible a largo plazo; ___, colapsará en menos de cinco años si no se reforma.",
     "respuesta": ["dicho de otro modo", "es decir"],
     "alternativas": ["mejor dicho", "dicho de otro modo", "a saber", "es más"],
     "explicacion": "✅ Válidos: 'dicho de otro modo' (reformulación más contundente) y 'es decir' (reformulación neutra). ❌ 'Mejor dicho' corregiría lo anterior; 'es más' añadiría, no reformularía.",
     "nivel": "C1"},
    {"frase": "Participaremos en el proyecto ___ se respeten los términos acordados en la reunión inicial.",
     "respuesta": ["siempre y cuando", "en caso de que"],
     "alternativas": ["a menos que", "siempre y cuando", "en caso de que", "suponiendo que"],
     "explicacion": "✅ Válidos: 'siempre y cuando' (condición positiva restrictiva) y 'en caso de que' (escenario posible). ❌ 'A menos que' sería condición negativa; 'suponiendo que' plantea una hipótesis, no una condición de participación.",
     "nivel": "C1"},
    {"frase": "No solo no colaboró con el equipo; ___, obstaculizó activamente el proceso desde el principio.",
     "respuesta": ["es más", "para colmo"],
     "alternativas": ["para colmo", "es más", "por añadidura", "asimismo"],
     "explicacion": "✅ Válidos: 'es más' (gradación ascendente, neutro) y 'para colmo' (añade algo negativo que agrava). ❌ 'Por añadidura' funciona pero es más formal y menos habitual aquí; 'asimismo' no encaja con la estructura adversativa.",
     "nivel": "C1"},
    {"frase": "___, lo que se les pide no es un esfuerzo extraordinario, sino simplemente coherencia.",
     "respuesta": ["En definitiva", "En resumidas cuentas", "En suma", "Al fin y al cabo"],
     "alternativas": ["En resumidas cuentas", "En definitiva", "Al fin y al cabo", "En suma"],
     "explicacion": "✅ Las cuatro opciones son válidas para concluir. Matices: 'En definitiva' y 'en suma' son más formales y rotundos; 'en resumidas cuentas' es más coloquial; 'al fin y al cabo' tiene un tono más reflexivo.",
     "nivel": "C1"},
    {"frase": "Los datos apuntan en la misma dirección; ___, la reforma es urgente e ineludible.",
     "respuesta": ["por ende", "así pues", "por consiguiente", "en consecuencia"],
     "alternativas": ["por ende", "así pues", "por consiguiente", "en consecuencia"],
     "explicacion": "✅ Las cuatro son consecutivas válidas. Matices de registro: 'por ende' es el más culto o literario; 'por consiguiente' y 'en consecuencia' son formales; 'así pues' es el más ligero.",
     "nivel": "C2"},
    {"frase": "Se identificaron cuatro ejes de actuación, ___ formación, innovación, sostenibilidad y digitalización.",
     "respuesta": ["a saber", "es decir"],
     "alternativas": ["es decir", "a saber", "dicho de otro modo", "mejor dicho"],
     "explicacion": "✅ Válidos: 'a saber' (el más formal y preciso para enumeraciones) y 'es decir' (válido aunque más genérico). ❌ 'Dicho de otro modo' reformula con otras palabras, no enumera; 'mejor dicho' corrige.",
     "nivel": "C2"},
    {"frase": "Lograron sacar el proyecto adelante ___ la solidaridad del equipo en los momentos más críticos.",
     "respuesta": ["merced a"],
     "alternativas": ["a causa de", "merced a", "habida cuenta de que", "dado que"],
     "explicacion": "'Merced a' equivale a 'gracias a': la única opción válida para una causa positiva. ❌ 'A causa de' se usa para causas negativas; 'habida cuenta de que' y 'dado que' son causales pero van seguidos de frase, no de sustantivo.",
     "nivel": "C2"},
    {"frase": "La situación es preocupante; ___, esta semana han cerrado tres empresas del sector.",
     "respuesta": ["sin ir más lejos", "dicho sea de paso"],
     "alternativas": ["pongamos por caso", "sin ir más lejos", "dicho sea de paso", "a propósito"],
     "explicacion": "✅ Válidos: 'sin ir más lejos' (ejemplo cercano y real) y 'dicho sea de paso' (acotación relevante sobre el margen). ❌ 'Pongamos por caso' sería para ejemplos hipotéticos; 'a propósito' introduce una digresión más independiente.",
     "nivel": "C1"},
    {"frase": "Acepto la propuesta, ___ que se me garantice acceso completo a la documentación.",
     "respuesta": ["a condición de", "siempre y cuando"],
     "alternativas": ["siempre y cuando", "a condición de", "a menos que", "en caso de que"],
     "explicacion": "✅ Válidos: 'a condición de que' (condición formal y explícita) y 'siempre y cuando' (equivalente, ligeramente menos formal). ❌ 'A menos que' es condición negativa; 'en caso de que' contempla un escenario, no impone una condición.",
     "nivel": "C1"},
]

# ─────────────────────────────────────────────
#  EJERCICIOS — CLASIFICA EL CONECTOR
# ─────────────────────────────────────────────

CLASIFICACION_EJERCICIOS: List[Dict] = [
    {"conector": "habida cuenta de que", "correcta": "Causa y origen",
     "opciones": ["Causa y origen", "Hipótesis y condición", "Estructuración y orden", "Contraste y concesión"],
     "explicacion": "'Habida cuenta de que' es un conector causal muy formal. Introduce una causa que se da por sabida."},
    {"conector": "de ahí que", "correcta": "Consecuencia y resultado",
     "opciones": ["Reformulación y aclaración", "Consecuencia y resultado", "Conclusión y cierre", "Causa y origen"],
     "explicacion": "'De ahí que' introduce una consecuencia que se deriva de forma natural. Siempre exige subjuntivo."},
    {"conector": "por añadidura", "correcta": "Adición y continuidad",
     "opciones": ["Énfasis y afirmación", "Adición y continuidad", "Ejemplificación y digresión", "Consecuencia y resultado"],
     "explicacion": "'Por añadidura' añade algo extra e inesperado a lo ya dicho, generalmente negativo."},
    {"conector": "ahora bien", "correcta": "Contraste y concesión",
     "opciones": ["Estructuración y orden", "Conclusión y cierre", "Contraste y concesión", "Hipótesis y condición"],
     "explicacion": "'Ahora bien' acepta algo y a continuación introduce una reserva o condición importante."},
    {"conector": "a saber", "correcta": "Reformulación y aclaración",
     "opciones": ["Ejemplificación y digresión", "Reformulación y aclaración", "Adición y continuidad", "Estructuración y orden"],
     "explicacion": "'A saber' introduce una enumeración o especificación explícita de lo anterior. Registro formal."},
    {"conector": "dicho sea de paso", "correcta": "Ejemplificación y digresión",
     "opciones": ["Reformulación y aclaración", "Énfasis y afirmación", "Ejemplificación y digresión", "Conclusión y cierre"],
     "explicacion": "'Dicho sea de paso' introduce una digresión o acotación que el hablante considera secundaria."},
    {"conector": "merced a", "correcta": "Causa y origen",
     "opciones": ["Causa y origen", "Adición y continuidad", "Hipótesis y condición", "Énfasis y afirmación"],
     "explicacion": "'Merced a' es un conector causal positivo (= gracias a). Registro muy culto o literario."},
    {"conector": "siempre y cuando", "correcta": "Hipótesis y condición",
     "opciones": ["Contraste y concesión", "Hipótesis y condición", "Estructuración y orden", "Causa y origen"],
     "explicacion": "'Siempre y cuando' establece una condición positiva y restrictiva."},
    {"conector": "por ende", "correcta": "Consecuencia y resultado",
     "opciones": ["Conclusión y cierre", "Énfasis y afirmación", "Consecuencia y resultado", "Adición y continuidad"],
     "explicacion": "'Por ende' es un consecutivo formal o literario. Equivale a 'por tanto'."},
    {"conector": "acto seguido", "correcta": "Estructuración y orden",
     "opciones": ["Estructuración y orden", "Consecuencia y resultado", "Adición y continuidad", "Reformulación y aclaración"],
     "explicacion": "'Acto seguido' indica que algo ocurre inmediatamente después, en el tiempo o en el discurso."},
    {"conector": "cabe destacar que", "correcta": "Énfasis y afirmación",
     "opciones": ["Ejemplificación y digresión", "Conclusión y cierre", "Énfasis y afirmación", "Reformulación y aclaración"],
     "explicacion": "'Cabe destacar que' señala algo que merece atención especial. Registro académico o formal."},
    {"conector": "al fin y al cabo", "correcta": "Conclusión y cierre",
     "opciones": ["Contraste y concesión", "Conclusión y cierre", "Adición y continuidad", "Énfasis y afirmación"],
     "explicacion": "'Al fin y al cabo' concluye relativizando o aceptando algo después de considerarlo todo."},
    {"conector": "pongamos por caso", "correcta": "Ejemplificación y digresión",
     "opciones": ["Hipótesis y condición", "Ejemplificación y digresión", "Reformulación y aclaración", "Estructuración y orden"],
     "explicacion": "'Pongamos por caso' introduce un ejemplo hipotético para ilustrar un argumento."},
    {"conector": "mejor dicho", "correcta": "Reformulación y aclaración",
     "opciones": ["Conclusión y cierre", "Adición y continuidad", "Reformulación y aclaración", "Énfasis y afirmación"],
     "explicacion": "'Mejor dicho' corrige o matiza lo que se acaba de decir, buscando mayor precisión."},
    {"conector": "es más", "correcta": "Adición y continuidad",
     "opciones": ["Énfasis y afirmación", "Adición y continuidad", "Consecuencia y resultado", "Contraste y concesión"],
     "explicacion": "'Es más' añade algo que refuerza o supera lo anterior. Introduce una gradación ascendente."},
]

# ─────────────────────────────────────────────
#  EJERCICIOS — ORDENA EL TEXTO
# ─────────────────────────────────────────────

TEXTOS_ORDEN: List[Dict] = [
    {
        "titulo": "La educación digital y el pensamiento crítico",
        "partes": [
            "En primer lugar, es indudable que la tecnología ha transformado el modo en que los jóvenes acceden al conocimiento.",
            "No obstante, cabe preguntarse si esta transformación ha venido acompañada de una educación crítica suficiente.",
            "De hecho, estudios recientes apuntan a que el consumo acrítico de información digital genera más confusión que comprensión.",
            "Por consiguiente, no basta con dotar a las aulas de dispositivos; es necesario enseñar a usarlos con criterio.",
            "En definitiva, la clave no está en la herramienta, sino en la pedagogía que la acompaña.",
        ],
        "conectores": ["En primer lugar", "No obstante", "De hecho", "Por consiguiente", "En definitiva"],
        "pista": "Sigue la lógica: introducción → concesión → dato → consecuencia → conclusión.",
    },
    {
        "titulo": "Conciliación laboral y cambio cultural",
        "partes": [
            "Habida cuenta de que las jornadas laborales siguen siendo excesivamente largas en España, el debate sobre la conciliación es más urgente que nunca.",
            "Asimismo, el reparto desigual de las tareas domésticas continúa recayendo de forma desproporcionada sobre las mujeres.",
            "Es más, las políticas de conciliación existentes se revelan insuficientes para cambiar estructuras culturales arraigadas.",
            "Dicho de otro modo, sin una transformación de los valores sociales, ninguna medida legislativa será verdaderamente efectiva.",
            "Al fin y al cabo, la conciliación es una cuestión de justicia, no de productividad.",
        ],
        "conectores": ["Habida cuenta de que", "Asimismo", "Es más", "Dicho de otro modo", "Al fin y al cabo"],
        "pista": "El texto va ampliando el problema y reformulando hasta llegar a una conclusión.",
    },
    {
        "titulo": "El valor del silencio en la comunicación",
        "partes": [
            "En lo que respecta a la comunicación interpersonal, tendemos a sobrevalorar la palabra y a ignorar el poder del silencio.",
            "Sin ir más lejos, las culturas orientales utilizan el silencio como señal de respeto y reflexión, no de incomodidad.",
            "Puesto que en Occidente el silencio suele interpretarse como distancia o conflicto, rara vez lo empleamos de forma consciente.",
            "De ahí que muchas conversaciones fracasen no por lo que se dice, sino por la incapacidad de escuchar con pausa.",
            "En suma, aprender a estar en silencio es, quizás, la habilidad comunicativa más subestimada de nuestra época.",
        ],
        "conectores": ["En lo que respecta a", "Sin ir más lejos", "Puesto que", "De ahí que", "En suma"],
        "pista": "El texto introduce un tema, da un ejemplo, explica una causa y extrae una consecuencia antes de concluir.",
    },
]

# ─────────────────────────────────────────────
#  CONFIG Y ESTILOS
# ─────────────────────────────────────────────


FUNCIONES_CONECTORES = list(dict.fromkeys(c["funcion"] for c in CONECTORES))

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────


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
        border-radius: 20px; padding: 1.8rem 2rem; margin-bottom: 1.2rem; color: white;
    }
    .hero h1 { font-family: 'Playfair Display', serif; font-size: 2rem; margin: 0 0 0.3rem 0; color: white; }
    .hero p { margin: 0; color: #c7d2fe; font-size: 0.95rem; }
    .metric-card {
        background: white; border: 1px solid #e5e7eb; border-radius: 16px;
        padding: 0.85rem 1rem; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .metric-value { font-size: 1.6rem; font-weight: 700; color: #1e1b4b; }
    .metric-label { font-size: 0.82rem; color: #6b7280; margin-top: 0.15rem; }
    .card-box, .quiz-box {
        background: white; border: 1px solid #e5e7eb; border-radius: 18px;
        padding: 1.3rem; box-shadow: 0 4px 16px rgba(0,0,0,0.05);
    }
    .card-chip {
        display: inline-block; background: #ede9fe; color: #4c1d95;
        border-radius: 999px; padding: 0.3rem 0.75rem; font-size: 0.82rem;
        font-weight: 700; margin-bottom: 0.75rem;
    }
    .nivel-badge {
        display: inline-block; border-radius: 999px; padding: 0.2rem 0.6rem;
        font-size: 0.78rem; font-weight: 700; color: white; margin-left: 0.5rem;
    }
    .card-title {
        color: #312e81; font-size: 1.7rem; font-weight: 700; margin-bottom: 0.6rem;
        font-family: 'Playfair Display', serif;
    }
    .card-line { color: #374151; margin-bottom: 0.4rem; font-size: 0.97rem; }
    .example-block {
        background: #f5f3ff; border-left: 3px solid #7c3aed;
        border-radius: 0 10px 10px 0; padding: 0.55rem 0.9rem;
        margin: 0.35rem 0; font-style: italic; color: #3730a3; font-size: 0.93rem;
    }
    .nota-box {
        background: #fef3c7; border: 1px solid #fcd34d; border-radius: 10px;
        padding: 0.55rem 0.9rem; font-size: 0.88rem; color: #78350f; margin-top: 0.6rem;
    }
    .section-title {
        font-size: 1.1rem; font-weight: 700; color: #1e1b4b; margin-bottom: 0.2rem;
        font-family: 'Playfair Display', serif;
    }
    .section-sub { color: #6b7280; margin-bottom: 0.8rem; font-size: 0.9rem; }
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
    .feedback-ai {
        background: #f0f4ff; border: 1px solid #818cf8; color: #1e1b4b;
        padding: 0.85rem 1rem; border-radius: 14px; margin-top: 0.75rem; white-space: pre-wrap;
    }
    .double-prep-card {
        background: #fefce8; border: 1px solid #fde68a; border-radius: 14px;
        padding: 1rem 1.2rem; margin-bottom: 0.8rem;
    }
    .dp-verb { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #78350f; font-weight: 700; }
    .dp-row { margin: 0.45rem 0; }
    .dp-prep { display: inline-block; background: #fef3c7; color: #78350f; border-radius: 6px; padding: 0.15rem 0.45rem; font-weight: 700; font-size: 0.88rem; }
    .dp-sig { color: #374151; font-size: 0.9rem; }
    .dp-ex { color: #78350f; font-style: italic; font-size: 0.87rem; margin-top: 0.1rem; }
    .weak-tag { background: #fee2e2; color: #991b1b; border-radius: 6px; padding: 0.15rem 0.5rem; font-size: 0.78rem; font-weight: 700; }
    /* Conectores styles */
    .con-card-chip {
        display: inline-block; background: #fef3c7; color: #78350f;
        border-radius: 999px; padding: 0.3rem 0.75rem; font-size: 0.82rem;
        font-weight: 700; margin-bottom: 0.75rem;
    }
    .con-card-title {
        color: #78350f; font-size: 1.7rem; font-weight: 700; margin-bottom: 0.6rem;
        font-family: 'Playfair Display', serif;
    }
    .con-example-block {
        background: #fffbeb; border-left: 3px solid #d97706;
        border-radius: 0 10px 10px 0; padding: 0.55rem 0.9rem;
        margin: 0.35rem 0; font-style: italic; color: #78350f; font-size: 0.93rem;
    }
    .module-badge {
        display: inline-block; border-radius: 10px; padding: 0.4rem 1rem;
        font-weight: 700; font-size: 0.9rem; margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)



# ─────────────────────────────────────────────
#  FUNCIONES — VERBOS
# ─────────────────────────────────────────────

def init_state() -> None:
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
        "weak_items": {},
        "gap_index": None,
        "gap_feedback": None,
        "error_index": None,
        "error_feedback": None,
        "ai_feedback": None,
        "dp_index": 0,
        "dp_revealed": False,
        "dp_quiz_ans": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def normalize(text: str) -> str:
    return " ".join(text.lower().strip().split())


def active_items(selected_preps: List[str]):
    base = [i for i in st.session_state.all_items if i["prep"] in selected_preps]
    weighted = []
    for item in base:
        key = item["expresion"]
        fails = st.session_state.weak_items.get(key, 0)
        weighted.append(item)
        if fails >= 2:
            weighted.append(item)
    return base, weighted


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
        valid_preps = _VERB_TO_PREPS.get(item["verbo"], [item["prep"]])
        nota_multi = (f"\n\n💡 Este verbo acepta varias preposiciones: {', '.join(valid_preps)}"
                      if len(valid_preps) > 1 else "")
        st.session_state.quiz_data = {
            "type": chosen_mode, "item": item,
            "question": f"¿Qué preposición completa correctamente esta estructura?\n\n**{item['verbo']} + ___**{nota_multi}",
            "answer": valid_preps,
            "options": options,
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

    answer = quiz["answer"]
    if isinstance(answer, list):
        correct = any(normalize(user_answer) == normalize(a) for a in answer)
        answer_display = " / ".join(f"**{a}**" for a in answer)
    else:
        correct = normalize(user_answer) == normalize(answer)
        answer_display = f"**{answer}**"

    st.session_state.quiz_total += 1

    if correct:
        st.session_state.quiz_score += 1
        st.session_state.quiz_streak += 1
        register_ok(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        if isinstance(answer, list) and len(answer) > 1:
            otras = [a for a in answer if normalize(a) != normalize(user_answer)]
            if otras:
                nota += f"\n\n✅ También válido: {', '.join(otras)}"
        set_feedback("ok", f"✅ Correcto.\n\nEjemplo: {ejemplo}{nota}")
    else:
        st.session_state.quiz_streak = 0
        register_fail(quiz["item"])
        ejemplo = random.choice(quiz["item"]["ejemplos"])
        exp = quiz["item"].get("nota", "")
        nota = f"\n\n💡 {exp}" if exp else ""
        set_feedback("bad", f"❌ Respuesta correcta: {answer_display}\n\nEjemplo: {ejemplo}{nota}")


async def get_ai_feedback_async(verbo_expr: str, frase_usuario: str) -> str:
    import aiohttp
    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 350,
        "messages": [{"role": "user", "content": (
            f"Eres un profesor de español de nivel C2 experto en gramática. "
            f"El alumno debe escribir una frase usando la expresión '{verbo_expr}'. "
            f"Frase del alumno: «{frase_usuario}»\n\n"
            f"Evalúa brevemente (máximo 4 líneas):\n"
            f"1. ¿Usa correctamente la preposición y la estructura?\n"
            f"2. ¿Es natural y fluida para un hablante nativo?\n"
            f"3. Una sugerencia de mejora si la hay.\n"
            f"Responde SIEMPRE en español, de forma directa y constructiva."
        )}]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "https://api.anthropic.com/v1/messages",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=aiohttp.ClientTimeout(total=20)
        ) as resp:
            data = await resp.json()
            return data["content"][0]["text"]


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
#  ESTADO CONECTORES
# ─────────────────────────────────────────────

def init_con_state():
    defaults = {
        "con_card_index": 0,
        "cng_idx": None,
        "cng_fb": None,
        "cnc_idx": None,
        "cnc_fb": None,
        "cnc_score": 0,
        "cnc_total": 0,
        "cno_idx": 0,
        "cno_shuf": [],
        "cno_fb": None,
        "cnf_item": None,
        "cnf_fb": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def call_claude_conector(conector: str, frase: str) -> str:
    import asyncio
    async def _call():
        import aiohttp
        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 400,
            "messages": [{"role": "user", "content": (
                f"Eres un profesor de español de nivel C2 experto en discurso y conectores. "
                f"El alumno debe escribir una frase o mini-párrafo usando el conector \'{conector}\'. "
                f"Frase del alumno: «{frase}»\n\n"
                f"Evalúa en máximo 4 líneas:\n"
                f"1. ¿Usa el conector correctamente (función, posición, puntuación, modo verbal si aplica)?\n"
                f"2. ¿El registro y la sintaxis son adecuados para un C2?\n"
                f"3. Una sugerencia concreta de mejora si la hay.\n"
                f"Responde siempre en español, de forma directa y constructiva."
            )}]
        }
        try:
            async with aiohttp.ClientSession() as s:
                async with s.post(
                    "https://api.anthropic.com/v1/messages", json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=aiohttp.ClientTimeout(total=20),
                ) as r:
                    d = await r.json()
                    return d["content"][0]["text"]
        except Exception as e:
            return f"Error al conectar con la IA: {e}"
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as pool:
                return pool.submit(asyncio.run, _call()).result(timeout=25)
        return loop.run_until_complete(_call())
    except Exception as e:
        return f"Error: {e}"

def show_con_fb(kind: str, msg: str):
    css = {"ok": "feedback-ok", "bad": "feedback-bad",
           "neutral": "feedback-neutral", "ai": "feedback-ai"}.get(kind, "feedback-neutral")
    st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  STREAMLIT CONFIG
# ─────────────────────────────────────────────

init_state()
init_con_state()

# ─────────────────────────────────────────────
#  SIDEBAR — Selector de módulo
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📘 Cata Español C2")
    modulo = st.radio(
        "Módulo:",
        ["📗 Verbos + Preposición", "🔗 Conectores"],
        label_visibility="collapsed",
    )
    st.markdown("---")

    if modulo == "📗 Verbos + Preposición":
        selected_preps: List[str] = []
        for prep in PREPS:
            n = len(DATA.get(prep, []))
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
        n_weak = len([v for v, c in st.session_state.weak_items.items() if c >= 2])
        if n_weak:
            st.markdown(f'<span class="weak-tag">⚠️ {n_weak} verbo(s) con ≥2 fallos</span>', unsafe_allow_html=True)
            if st.button("Reiniciar repetición espaciada"):
                st.session_state.weak_items = {}
                st.rerun()
        else:
            st.caption("Sin verbos débiles aún.")
    else:
        st.caption("50 conectores · C1/C2 · 5 tipos de ejercicio")

st.markdown("""
<div class="hero">
    <h1>🇪🇸 Cata Español — Nivel C2</h1>
    <p>Verbos + preposición · Conectores del discurso · Ejercicios avanzados · Feedback de IA</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  RENDER SEGÚN MÓDULO
# ─────────────────────────────────────────────

if modulo == "📗 Verbos + Preposición":

    items = base_items

    if not items:
        st.warning("Activa al menos una categoría y nivel para empezar.")
        st.stop()

    if st.session_state.current_card_index >= len(items):
        st.session_state.current_card_index = 0

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
#  TAB 5 — DOBLE PREPOSICIÓN (ejercicio interactivo)
# ────────────────────────────────
with tab5:
    if "dp_index" not in st.session_state:
        st.session_state.dp_index = 0
    if "dp_revealed" not in st.session_state:
        st.session_state.dp_revealed = False
    if "dp_quiz_ans" not in st.session_state:
        st.session_state.dp_quiz_ans = None

    st.markdown('<div class="section-title">Verbos con doble preposición</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Estos verbos cambian de significado según la preposición. Adivina cuántas preposiciones acepta cada uno y qué significa cada combinación.</div>', unsafe_allow_html=True)

    dp = DOUBLE_PREP[st.session_state.dp_index]
    preps_str = " / ".join(f"<strong>+{caso['prep']}</strong>" for caso in dp["casos"])

    # Tarjeta principal — muestra el verbo y la pista
    st.markdown(f"""
    <div class="card-box" style="text-align:center;padding:2rem 1.5rem;">
        <div class="card-title" style="font-size:2.2rem;margin-bottom:0.5rem;">{dp['verbo']}</div>
        <div style="color:#6b7280;font-size:0.95rem;">
            Este verbo acepta <strong>{len(dp['casos'])}</strong> preposición{"es" if len(dp["casos"])>1 else ""}.
            ¿Sabes cuáles son y qué diferencia de significado hay?
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")

    if not st.session_state.dp_revealed:
        if st.button("👁 Revelar preposiciones y significados", use_container_width=True, key="dp_reveal"):
            st.session_state.dp_revealed = True
            st.rerun()
    else:
        # Mostrar cada caso como tarjeta
        for caso in dp["casos"]:
            st.markdown(f"""
            <div style="background:#f5f3ff;border-left:4px solid #7c3aed;border-radius:0 14px 14px 0;
                        padding:0.9rem 1.2rem;margin-bottom:0.7rem;">
                <div style="margin-bottom:0.3rem;">
                    <span class="dp-prep" style="font-size:1rem;">+ {caso['prep']}</span>
                    <span style="color:#374151;margin-left:0.5rem;">→ {caso['significado']}</span>
                </div>
                <div style="font-style:italic;color:#5b21b6;font-size:0.93rem;">&ldquo;{caso['ejemplo']}&rdquo;</div>
            </div>
            """, unsafe_allow_html=True)

        # Mini-quiz: elige qué preposición corresponde a un ejemplo
        st.markdown("---")
        st.markdown("**Mini-quiz:** ¿Con qué preposición se usa en este contexto?")

        # Tomar un ejemplo aleatorio de los casos (fijo por índice para no cambiar al rerenderizar)
        caso_quiz = dp["casos"][st.session_state.dp_index % len(dp["casos"])]
        frase_con_hueco = caso_quiz["ejemplo"].replace(
            f" {caso_quiz['prep']} ", " **___** ", 1
        )
        st.markdown(f'<div class="quiz-box"><p style="font-size:1rem;color:#1e1b4b;">{frase_con_hueco}</p></div>', unsafe_allow_html=True)

        opciones_dp = [caso["prep"] for caso in dp["casos"]]
        random.shuffle(opciones_dp)
        dp_sel = st.radio("Preposición:", opciones_dp, key=f"dp_radio_{st.session_state.dp_index}", horizontal=True)

        dq1, dq2 = st.columns(2)
        with dq1:
            if st.button("Comprobar ✓", key="dp_check", use_container_width=True):
                if dp_sel == caso_quiz["prep"]:
                    st.session_state.dp_quiz_ans = ("ok", f"✅ Correcto. **+{caso_quiz['prep']}** → {caso_quiz['significado']}")
                else:
                    correct_caso = next(ca for ca in dp["casos"] if ca["prep"] == caso_quiz["prep"])
                    st.session_state.dp_quiz_ans = ("bad",
                        f"❌ En este contexto es **+{caso_quiz['prep']}** → {correct_caso['significado']}")
                st.rerun()
        with dq2:
            if st.button("Ver solución 👁", key="dp_sol", use_container_width=True):
                st.session_state.dp_quiz_ans = ("neutral",
                    f"**+{caso_quiz['prep']}** → {caso_quiz['significado']}")
                st.rerun()

        if st.session_state.dp_quiz_ans:
            kind, msg = st.session_state.dp_quiz_ans
            css = {"ok": "feedback-ok", "bad": "feedback-bad", "neutral": "feedback-neutral"}[kind]
            st.markdown(f'<div class="{css}">{msg}</div>', unsafe_allow_html=True)

    # Navegación
    st.markdown("")
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("← Anterior", use_container_width=True, key="dp_prev"):
            st.session_state.dp_index = (st.session_state.dp_index - 1) % len(DOUBLE_PREP)
            st.session_state.dp_revealed = False
            st.session_state.dp_quiz_ans = None
            st.rerun()
    with nav2:
        st.markdown(f'<p style="text-align:center;color:#6b7280;margin-top:0.6rem;">{st.session_state.dp_index+1} / {len(DOUBLE_PREP)}</p>', unsafe_allow_html=True)
    with nav3:
        if st.button("Siguiente →", use_container_width=True, key="dp_next"):
            st.session_state.dp_index = (st.session_state.dp_index + 1) % len(DOUBLE_PREP)
            st.session_state.dp_revealed = False
            st.session_state.dp_quiz_ans = None
            st.rerun()


# ─────────────────────────────────────────────
if modulo == "🔗 Conectores":
    ctab1, ctab2, ctab3, ctab4, ctab5, ctab6, ctab7 = st.tabs([
        "📖 Tarjetas",
        "🏷️ Clasifica el conector",
        "🧩 Rellena el hueco",
        "📝 Ordena el texto",
        "✍️ Escritura libre + IA",
        "📊 Tabla de referencia",
        "🗒️ Tabla para rellenar",
    ])

    # ══════════════════════════════
    #  TAB 1 — TARJETAS
    # ══════════════════════════════
    with ctab1:
        st.markdown('<div class="section-title">Explorador de conectores</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Estudia función, matiz y ejemplos en contexto real.</div>', unsafe_allow_html=True)

        funcion_sel = st.selectbox("Filtra por categoría:", ["Todas"] + FUNCIONES, key="cn_funcion_sel")
        lista = CONECTORES if funcion_sel == "Todas" else [c for c in CONECTORES if c["funcion"] == funcion_sel]

        if lista:
            idx = st.session_state.con_card_index % len(lista)
            con = lista[idx]
            nc = NIVEL_COLORS.get(con.get("nivel", "C1"), "#8b5cf6")

            st.markdown(f"""
            <div class="card-box">
                <div>
                    <span class="con-card-chip">{con['funcion']}</span>
                    <span class="nivel-badge" style="background:{nc};">{con.get('nivel','C1')}</span>
                </div>
                <div class="con-card-title">{con['conector']}</div>
                <div class="card-line"><strong>Matiz:</strong> {con['matiz']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Ejemplos en contexto:**")
            for ej in con["ejemplos"]:
                st.markdown(f'<div class="con-example-block">{ej}</div>', unsafe_allow_html=True)

            c1, c2, c3 = st.columns(3)
            with c1:
                if st.button("← Anterior", use_container_width=True, key="cn_card_prev"):
                    st.session_state.con_card_index = (idx - 1) % len(lista)
                    st.rerun()
            with c2:
                if st.button("Siguiente →", use_container_width=True, key="cn_card_next"):
                    st.session_state.con_card_index = (idx + 1) % len(lista)
                    st.rerun()
            with c3:
                if st.button("Aleatorio 🎲", use_container_width=True, key="cn_card_rand"):
                    st.session_state.con_card_index = random.randrange(len(lista))
                    st.rerun()

            st.caption(f"Conector {idx + 1} de {len(lista)}")

    # ══════════════════════════════
    #  TAB 2 — CLASIFICA EL CONECTOR
    # ══════════════════════════════
    with ctab2:
        st.markdown('<div class="section-title">Clasifica el conector</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige la función discursiva de cada conector. Fundamental para usarlos con precisión.</div>', unsafe_allow_html=True)

        if st.session_state.cnc_idx is None:
            st.session_state.cnc_idx = random.randrange(len(CLASIFICACION_EJERCICIOS))

        ej = CLASIFICACION_EJERCICIOS[st.session_state.cnc_idx]

        st.markdown(f"""
        <div class="quiz-box">
            <p style="font-size:1.1rem;color:#374151;">¿Cuál es la función de</p>
            <div class="con-card-title" style="font-size:2rem;margin:0.2rem 0 0.8rem 0;">{ej['conector']}</div>
        </div>
        """, unsafe_allow_html=True)

        opciones_mezcladas = ej["opciones"][:]
        sel = st.radio("Selecciona la función:", opciones_mezcladas,
                       key=f"clas_{st.session_state.cnc_idx}")

        cg1, cg2, cg3 = st.columns(3)
        with cg1:
            if st.button("Comprobar ✓", key="cn_clas_check", use_container_width=True):
                st.session_state.cnc_total += 1
                if sel == ej["correcta"]:
                    st.session_state.cnc_score += 1
                    st.session_state.cnc_fb = ("ok",
                        f"✅ Correcto: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                else:
                    st.session_state.cnc_fb = ("bad",
                        f"❌ La función correcta es: **{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg2:
            if st.button("Ver solución 👁", key="cn_clas_sol", use_container_width=True):
                st.session_state.cnc_fb = ("neutral",
                    f"**{ej['correcta']}**\n\n💡 {ej['explicacion']}")
                st.rerun()
        with cg3:
            if st.button("Nuevo →", key="cn_clas_next", use_container_width=True):
                st.session_state.cnc_idx = random.randrange(len(CLASIFICACION_EJERCICIOS))
                st.session_state.cnc_fb = None
                st.rerun()

        if st.session_state.cnc_fb:
            show_fb(*st.session_state.cnc_fb)

        if st.session_state.cnc_total:
            pct = int(st.session_state.cnc_score / st.session_state.cnc_total * 100)
            st.progress(st.session_state.cnc_score / st.session_state.cnc_total)
            st.caption(f"Precisión: {st.session_state.cnc_score}/{st.session_state.cnc_total} ({pct} %)")
            if st.button("Reiniciar marcador", key="cn_clas_reset"):
                st.session_state.cnc_score = 0
                st.session_state.cnc_total = 0
                st.session_state.cnc_fb = None
                st.rerun()

    # ══════════════════════════════
    #  TAB 3 — RELLENA EL HUECO
    # ══════════════════════════════
    with ctab3:
        st.markdown('<div class="section-title">Rellena el hueco</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Elige el conector más adecuado para cada contexto. Atención a los matices.</div>', unsafe_allow_html=True)

        if st.session_state.cng_idx is None:
            st.session_state.cng_idx = random.randrange(len(GAP_EJERCICIOS))

        gap = GAP_EJERCICIOS[st.session_state.cng_idx]
        nc_gap = NIVEL_COLORS.get(gap.get("nivel", "C1"), "#8b5cf6")

        frase_html = gap["frase"].replace("___",
            '<span style="background:#fef3c7;color:#78350f;padding:2px 10px;border-radius:6px;font-weight:700;">___</span>')
        st.markdown(f'<div class="quiz-box"><p style="font-size:1.05rem;color:#1e1b4b;">{frase_html}</p>'
                    f'<span class="nivel-badge" style="background:{nc_gap};">{gap.get("nivel","C1")}</span></div>',
                    unsafe_allow_html=True)

        gap_sel = st.radio("Elige el conector:", gap["alternativas"],
                           key=f"cn_gap_{st.session_state.cng_idx}")

        gg1, gg2, gg3 = st.columns(3)
        with gg1:
            if st.button("Comprobar ✓", key="cn_gap_check", use_container_width=True):
                validas = gap["respuesta"]  # lista
                validas_str = " / ".join(f"**{v}**" for v in validas)
                es_correcta = any(normalize(gap_sel) == normalize(v) for v in validas)
                if es_correcta:
                    otras = [v for v in validas if normalize(v) != normalize(gap_sel)]
                    extra = ("\n\n✅ También válido: " + " / ".join(f"**{v}**" for v in otras)) if otras else ""
                    st.session_state.cng_fb = ("ok",
                        f"✅ Correcto: **{gap_sel}**{extra}\n\n💡 {gap['explicacion']}")
                else:
                    st.session_state.cng_fb = ("bad",
                        f"❌ Opciones válidas: {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg2:
            if st.button("Ver solución 👁", key="cn_gap_sol", use_container_width=True):
                validas = gap["respuesta"]
                validas_str = " / ".join(f"**{v}**" for v in validas)
                st.session_state.cng_fb = ("neutral",
                    f"Válido(s): {validas_str}\n\n💡 {gap['explicacion']}")
                st.rerun()
        with gg3:
            if st.button("Nueva frase →", key="cn_gap_next", use_container_width=True):
                st.session_state.cng_idx = random.randrange(len(GAP_EJERCICIOS))
                st.session_state.cng_fb = None
                st.rerun()

        if st.session_state.cng_fb:
            show_fb(*st.session_state.cng_fb)

    # ══════════════════════════════
    #  TAB 4 — ORDENA EL TEXTO
    # ══════════════════════════════
    with ctab4:
        st.markdown('<div class="section-title">Ordena el texto</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Los conectores son tu brújula. Úsalos para reconstruir la estructura argumentativa.</div>', unsafe_allow_html=True)

        texto = TEXTOS_ORDEN[st.session_state.cno_idx]

        if not st.session_state.cno_shuf:
            shuffled = list(enumerate(texto["partes"]))
            random.shuffle(shuffled)
            st.session_state.cno_shuf = shuffled

        st.markdown(f"**Texto:** *{texto['titulo']}*")
        st.markdown("Conectores clave: " + " · ".join(f"**{c}**" for c in texto["conectores"]))
        st.markdown(f'<div style="background:#fef3c7;border-radius:10px;padding:0.6rem 1rem;color:#78350f;font-size:0.9rem;margin-bottom:0.8rem;">💡 Pista: {texto["pista"]}</div>', unsafe_allow_html=True)

        st.markdown("**Fragmentos (en orden aleatorio):**")
        for i, (_, parte) in enumerate(st.session_state.cno_shuf):
            st.markdown(f'<div class="con-example-block"><strong>{i+1}.</strong> {parte}</div>', unsafe_allow_html=True)

        st.markdown("**Escribe el orden correcto** (ej: `3,1,4,2,5`):")
        order_ans = st.text_input("Tu orden:", key=f"cn_order_{st.session_state.cno_idx}",
                                  placeholder="1,2,3,4,5")

        oo1, oo2, oo3 = st.columns(3)
        with oo1:
            if st.button("Comprobar ✓", key="cn_order_check", use_container_width=True):
                try:
                    user_order = [int(x.strip()) - 1 for x in order_ans.split(",")]
                    orig_indices = [oi for oi, _ in st.session_state.cno_shuf]
                    correct = sorted(range(len(orig_indices)), key=lambda x: orig_indices[x])
                    if user_order == correct:
                        st.session_state.cno_fb = ("ok", "✅ ¡Perfecto! El orden es correcto.")
                    else:
                        correct_str = ",".join(str(x + 1) for x in correct)
                        partes_ord = "\n".join(
                            f"{i+1}. {p}" for i, p in enumerate(texto["partes"])
                        )
                        st.session_state.cno_fb = ("bad",
                            f"❌ El orden correcto es: **{correct_str}**\n\n{partes_ord}")
                except Exception:
                    st.session_state.cno_fb = ("neutral",
                        "⚠️ Escribe los números separados por comas, sin espacios extra.")
                st.rerun()
        with oo2:
            if st.button("Ver solución 👁", key="cn_order_sol", use_container_width=True):
                partes_ord = "\n".join(f"{i+1}. {p}" for i, p in enumerate(texto["partes"]))
                st.session_state.cno_fb = ("neutral", f"Texto ordenado:\n\n{partes_ord}")
                st.rerun()
        with oo3:
            if st.button("Otro texto →", key="cn_order_next", use_container_width=True):
                st.session_state.cno_idx = (st.session_state.cno_idx + 1) % len(TEXTOS_ORDEN)
                st.session_state.cno_shuf = []
                st.session_state.cno_fb = None
                st.rerun()

        if st.session_state.cno_fb:
            show_fb(*st.session_state.cno_fb)

    # ══════════════════════════════
    #  TAB 5 — ESCRITURA LIBRE + IA
    # ══════════════════════════════
    with ctab5:
        st.markdown('<div class="section-title">Escritura libre + feedback de IA</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Escribe una frase o mini-párrafo usando el conector propuesto. Claude evaluará función, registro y puntuación.</div>', unsafe_allow_html=True)

        if st.session_state.cnf_item is None:
            st.session_state.cnf_item = random.choice(CONECTORES)

        fc = st.session_state.cnf_item
        nc_fc = NIVEL_COLORS.get(fc.get("nivel", "C1"), "#8b5cf6")

        col_card, col_write = st.columns([1, 1.2], gap="large")

        with col_card:
            st.markdown(f"""
            <div class="card-box">
                <span class="con-card-chip">{fc['funcion']}</span>
                <span class="nivel-badge" style="background:{nc_fc};">{fc.get('nivel','C1')}</span>
                <div class="con-card-title">{fc['conector']}</div>
                <div class="card-line" style="color:#6b7280;font-style:italic;">{fc['matiz']}</div>
                <div style="margin-top:0.8rem;"><strong>Ejemplo:</strong></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f'<div class="con-example-block">{fc["ejemplos"][0]}</div>', unsafe_allow_html=True)

            if st.button("Cambiar conector 🔄", use_container_width=True, key="free_change"):
                st.session_state.cnf_item = random.choice(CONECTORES)
                st.session_state.cnf_fb = None
                st.rerun()

        with col_write:
            frase_libre = st.text_area(
                "Tu frase o mini-párrafo:",
                height=120,
                key="cn_free_frase",
                placeholder=f"Escribe aquí usando '{fc['conector']}'…",
            )

            if st.button("Pedir feedback a Claude 🤖", use_container_width=True, key="free_ai"):
                if frase_libre.strip():
                    with st.spinner("Claude está evaluando tu uso del conector…"):
                        fb = call_claude(fc["conector"], frase_libre.strip())
                    st.session_state.cnf_fb = fb
                else:
                    st.session_state.cnf_fb = "⚠️ Escribe una frase primero."
                st.rerun()

            if st.session_state.cnf_fb:
                st.markdown(
                    f'<div class="feedback-ai">🤖 <strong>Feedback de Claude:</strong>\n\n{st.session_state.cnf_fb}</div>',
                    unsafe_allow_html=True,
                )

    # ══════════════════════════════
    #  TAB 6 — TABLA DE REFERENCIA
    # ══════════════════════════════
    with ctab6:
        st.markdown('<div class="section-title">Tabla de referencia</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Todos los conectores organizados por función. Úsala para estudiar y consultar.</div>', unsafe_allow_html=True)

        # Build grouped data
        from collections import defaultdict
        grouped = defaultdict(list)
        for c in CONECTORES:
            grouped[c["funcion"]].append(c)

        # Color per function (cycling palette)
        funcion_colors = {
            "Contraste y concesión":    ("#fef3c7", "#78350f"),
            "Causa y origen":           ("#dbeafe", "#1e3a8a"),
            "Consecuencia y resultado": ("#dcfce7", "#14532d"),
            "Adición y continuidad":    ("#ede9fe", "#4c1d95"),
            "Hipótesis y condición":    ("#fce7f3", "#831843"),
            "Estructuración y orden":   ("#e0f2fe", "#0c4a6e"),
            "Reformulación y aclaración":("#f0fdf4","#166534"),
            "Ejemplificación y digresión":("#fff7ed","#7c2d12"),
            "Conclusión y cierre":      ("#f5f3ff", "#3b0764"),
            "Énfasis y afirmación":     ("#fef9c3", "#713f12"),
        }

        for funcion, items in grouped.items():
            bg, fg = funcion_colors.get(funcion, ("#f8fafc", "#1e293b"))
            # Sort by nivel then conector
            nivel_order = {"B2": 0, "C1": 1, "C2": 2}
            items_sorted = sorted(items, key=lambda x: (nivel_order.get(x.get("nivel","B2"), 1), x["conector"]))

            rows_html = ""
            for item in items_sorted:
                nivel = item.get("nivel", "C1")
                nc = NIVEL_COLORS.get(nivel, "#6b7280")
                rows_html += f"""
                <tr>
                  <td style="padding:0.45rem 0.8rem;font-weight:700;color:{fg};white-space:nowrap;">
                    {item['conector']}
                    <span style="background:{nc};color:white;border-radius:4px;
                                 padding:1px 6px;font-size:0.72rem;font-weight:700;
                                 margin-left:0.4rem;">{nivel}</span>
                  </td>
                  <td style="padding:0.45rem 0.8rem;color:#374151;font-size:0.88rem;">
                    {item['matiz']}
                  </td>
                </tr>"""

            st.markdown(f"""
            <div style="margin-bottom:1.2rem;">
              <div style="background:{bg};border-radius:12px 12px 0 0;
                          padding:0.55rem 1rem;font-weight:700;color:{fg};font-size:0.95rem;">
                {funcion} <span style="font-weight:400;font-size:0.85rem;margin-left:0.5rem;">
                ({len(items)} conectores)</span>
              </div>
              <table style="width:100%;border-collapse:collapse;background:white;
                            border:1px solid #e5e7eb;border-radius:0 0 12px 12px;
                            overflow:hidden;">
                <thead>
                  <tr style="background:#f8fafc;border-bottom:1px solid #e5e7eb;">
                    <th style="padding:0.4rem 0.8rem;text-align:left;color:#6b7280;
                               font-size:0.8rem;font-weight:600;width:30%;">CONECTOR</th>
                    <th style="padding:0.4rem 0.8rem;text-align:left;color:#6b7280;
                               font-size:0.8rem;font-weight:600;">MATIZ / USO</th>
                  </tr>
                </thead>
                <tbody>{rows_html}</tbody>
              </table>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            '<div style="color:#6b7280;font-size:0.82rem;margin-top:0.5rem;">'
            '🔵 B2 &nbsp;|&nbsp; 🟣 C1 &nbsp;|&nbsp; 🔴 C2</div>',
            unsafe_allow_html=True,
        )


    # ══════════════════════════════
    #  TAB 7 — TABLA PARA RELLENAR
    # ══════════════════════════════
    with ctab7:
        st.markdown('<div class="section-title">Tabla para rellenar</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Se muestra la función y el matiz. Escribe el conector que corresponde a cada descripción. Comprueba tus respuestas al final.</div>', unsafe_allow_html=True)

        # Build exercise: shuffle all connectors, present matiz → student writes conector
        if "tabla_ejercicio" not in st.session_state or not st.session_state.tabla_ejercicio:
            ejercicio = [{"conector": c["conector"], "funcion": c["funcion"], "matiz": c["matiz"],
                          "nivel": c.get("nivel", "C1")} for c in CONECTORES]
            random.shuffle(ejercicio)
            st.session_state.tabla_ejercicio = ejercicio
            st.session_state.tabla_checked = False
            st.session_state.tabla_answers = {}

        ejercicio = st.session_state.tabla_ejercicio

        # Group by function for display
        from collections import defaultdict as _dd
        by_funcion = _dd(list)
        for i, item in enumerate(ejercicio):
            by_funcion[item["funcion"]].append((i, item))

        funcion_colors2 = {
            "Contraste y concesión":    "#fef3c7",
            "Causa y origen":           "#dbeafe",
            "Consecuencia y resultado": "#dcfce7",
            "Adición y continuidad":    "#ede9fe",
            "Hipótesis y condición":    "#fce7f3",
            "Estructuración y orden":   "#e0f2fe",
            "Reformulación y aclaración":"#f0fdf4",
            "Ejemplificación y digresión":"#fff7ed",
            "Conclusión y cierre":      "#f5f3ff",
            "Énfasis y afirmación":     "#fef9c3",
        }

        for funcion, items in by_funcion.items():
            bg = funcion_colors2.get(funcion, "#f8fafc")
            st.markdown(
                f'<div style="background:{bg};border-radius:10px 10px 0 0;padding:0.5rem 1rem;'
                f'font-weight:700;font-size:0.92rem;color:#1e293b;margin-top:1rem;">'
                f'{funcion}</div>',
                unsafe_allow_html=True,
            )
            for idx, item in items:
                nivel = item["nivel"]
                nc = NIVEL_COLORS.get(nivel, "#6b7280")
                col_matiz, col_input, col_result = st.columns([3, 1.5, 1.2])

                with col_matiz:
                    st.markdown(
                        f'<div style="padding:0.45rem 0;font-size:0.88rem;color:#374151;">'
                        f'{item["matiz"]}'
                        f'<span style="background:{nc};color:white;border-radius:4px;'
                        f'padding:1px 6px;font-size:0.72rem;font-weight:700;margin-left:0.5rem;">'
                        f'{nivel}</span></div>',
                        unsafe_allow_html=True,
                    )

                with col_input:
                    val = st.text_input(
                        label="conector",
                        label_visibility="collapsed",
                        placeholder="escribe aquí…",
                        key=f"tabla_inp_{idx}",
                    )
                    st.session_state.tabla_answers[idx] = val

                with col_result:
                    if st.session_state.tabla_checked:
                        user = " ".join(val.lower().strip().split())
                        correct = " ".join(item["conector"].lower().strip().split())
                        if user == correct:
                            st.markdown(
                                f'<div style="color:#065f46;font-weight:700;padding-top:0.45rem;">✅</div>',
                                unsafe_allow_html=True,
                            )
                        elif user:
                            st.markdown(
                                f'<div style="color:#991b1b;font-size:0.82rem;padding-top:0.3rem;">'
                                f'❌ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<div style="color:#6b7280;font-size:0.82rem;padding-top:0.3rem;">'
                                f'→ <strong>{item["conector"]}</strong></div>',
                                unsafe_allow_html=True,
                            )

        st.markdown("<br>", unsafe_allow_html=True)
        b1, b2, b3 = st.columns(3)

        with b1:
            if st.button("Comprobar todo ✓", use_container_width=True, key="tabla_check_btn"):
                st.session_state.tabla_checked = True
                st.rerun()

        with b2:
            if st.button("Ver soluciones 👁", use_container_width=True, key="tabla_sol_btn"):
                st.session_state.tabla_checked = True
                # Clear answers so all show as "→ correct"
                st.session_state.tabla_answers = {}
                st.rerun()

        with b3:
            if st.button("Nueva tabla 🔀", use_container_width=True, key="tabla_new_btn"):
                st.session_state.tabla_ejercicio = []
                st.session_state.tabla_checked = False
                st.session_state.tabla_answers = {}
                st.rerun()

        if st.session_state.tabla_checked:
            answers = st.session_state.tabla_answers
            total = len(ejercicio)
            correct_count = sum(
                1 for i, item in enumerate(ejercicio)
                if " ".join(answers.get(i, "").lower().strip().split()) ==
                   " ".join(item["conector"].lower().strip().split())
            )
            pct = int(correct_count / total * 100) if total else 0
            color = "#065f46" if pct >= 80 else "#92400e" if pct >= 50 else "#991b1b"
            st.markdown(
                f'<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;'
                f'padding:0.9rem 1.2rem;margin-top:0.5rem;text-align:center;">'
                f'<span style="font-size:1.3rem;font-weight:700;color:{color};">'
                f'{correct_count}/{total}</span>'
                f'<span style="color:#6b7280;font-size:0.9rem;margin-left:0.5rem;">correctos ({pct} %)</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
