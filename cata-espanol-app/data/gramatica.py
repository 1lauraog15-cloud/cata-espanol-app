from typing import Dict, List

GR_SUBJUNTIVO: List[Dict] = [
    {"frase": "Es importante que todos los miembros ___ (estar) de acuerdo antes de presentar la propuesta.",
     "respuesta": "estén", "tipo": "Expresiones impersonales",
     "explicacion": "Las expresiones impersonales de valoración (es importante, es necesario, es fundamental...) exigen subjuntivo en la subordinada.",
     "trampa": "Contrasta con 'es evidente que + indicativo', que afirma un hecho.",
     "nivel": "C1"},
    {"frase": "Me sorprende que todavía no ___ (publicarse) los resultados del estudio.",
     "respuesta": "se hayan publicado", "tipo": "Verbos de emoción",
     "explicacion": "Verbos de sentimiento (sorprender, alegrar, molestar, extrañar...) rigen subjuntivo cuando el sujeto de la subordinada es distinto al principal.",
     "trampa": "El perfecto de subjuntivo (hayan publicado) expresa una acción anterior al momento presente.",
     "nivel": "C1"},
    {"frase": "No creo que la situación ___ (mejorar) sin una intervención decidida.",
     "respuesta": "mejore", "tipo": "Verbos de opinión negados",
     "explicacion": "Creer, pensar, opinar + negación → subjuntivo. Sin negación → indicativo: 'Creo que mejorará'.",
     "trampa": "'Creo que mejorará' (indicativo) vs 'No creo que mejore' (subjuntivo).",
     "nivel": "C1"},
    {"frase": "Aunque ___ (llover) mañana, el acto se celebrará al aire libre según lo previsto.",
     "respuesta": "llueva", "tipo": "Aunque + subjuntivo (hipótesis)",
     "explicacion": "'Aunque' + subjuntivo: condición hipotética o no confirmada. 'Aunque' + indicativo: hecho conocido ('aunque llueve, salgo').",
     "trampa": "Si se sabe que lloverá → indicativo. Si es hipótesis → subjuntivo.",
     "nivel": "C1"},
    {"frase": "Buscan un candidato que ___ (tener) experiencia en gestión de equipos internacionales.",
     "respuesta": "tenga", "tipo": "Antecedente indefinido",
     "explicacion": "Cuando el antecedente es indefinido (buscan alguien que...) o negado, la relativa lleva subjuntivo.",
     "trampa": "'Tengo un candidato que tiene experiencia' (indicativo, conocido) vs 'busco uno que tenga' (subjuntivo, indefinido).",
     "nivel": "C1"},
    {"frase": "Te lo digo para que ___ (poder) prepararte con tiempo suficiente.",
     "respuesta": "puedas", "tipo": "Conjunciones de finalidad",
     "explicacion": "Para que, a fin de que, con el objetivo de que → siempre subjuntivo.",
     "trampa": "No confundir con 'para + infinitivo' cuando el sujeto es el mismo: 'para poder prepararte'.",
     "nivel": "B2"},
    {"frase": "Cuando ___ (terminar) de revisar el informe, envíamelo por correo.",
     "respuesta": "termines", "tipo": "Cuando + subjuntivo (futuro)",
     "explicacion": "'Cuando' + subjuntivo: acción futura o hipotética. 'Cuando' + indicativo: acción habitual o pasada.",
     "trampa": "'Cuando llegué' (pasado, indicativo) vs 'cuando llegues' (futuro, subjuntivo).",
     "nivel": "B2"},
    {"frase": "Si ___ (saber) lo que iba a pasar, nunca habría firmado ese contrato.",
     "respuesta": "hubiera sabido / hubiese sabido", "tipo": "Condicional irreal de pasado",
     "explicacion": "Si + pluscuamperfecto de subjuntivo → condicional compuesto. Expresa condición imposible en el pasado.",
     "trampa": "Nunca se usa 'si + condicional': *si habría sabido* es incorrecto.",
     "nivel": "C1"},
    {"frase": "Ojalá ___ (llegar) a un acuerdo antes de que expire el plazo.",
     "respuesta": "lleguen / llegaran / llegasen", "tipo": "Ojalá + subjuntivo",
     "explicacion": "'Ojalá' siempre rige subjuntivo. Presente para deseos realizables; imperfecto para poco probables.",
     "trampa": "*Ojalá llegarán* es incorrecto en español normativo.",
     "nivel": "B2"},
    {"frase": "Le pidió que ___ (guardar) la información con absoluta discreción.",
     "respuesta": "guardara / guardase", "tipo": "Petición en pasado",
     "explicacion": "Verbos de influencia (pedir, rogar, ordenar...) en pasado → imperfecto de subjuntivo en la subordinada.",
     "trampa": "Si el verbo principal está en presente: 'Le pide que guarde'.",
     "nivel": "C1"},
    {"frase": "Habla como si ___ (conocer) personalmente a todos los miembros del consejo.",
     "respuesta": "conociera / conociese", "tipo": "Como si",
     "explicacion": "'Como si' siempre lleva imperfecto o pluscuamperfecto de subjuntivo: expresa una comparación irreal.",
     "trampa": "*Como si conoce* es incorrecto. Siempre subjuntivo después de 'como si'.",
     "nivel": "C1"},
    {"frase": "En cuanto usted ___ (recibir) la notificación oficial, procederemos a tramitar los permisos.",
     "respuesta": "reciba", "tipo": "Conjunciones temporales + futuro",
     "explicacion": "En cuanto, tan pronto como, una vez que + subjuntivo cuando la acción es futura.",
     "trampa": "'En cuanto llegué' (pasado, indicativo) vs 'en cuanto recibamos' (futuro, subjuntivo).",
     "nivel": "C1"},
    {"frase": "Por mucho que ___ (esforzarse), no consiguió superar el obstáculo.",
     "respuesta": "se esforzara / se esforzase", "tipo": "Concesivas de grado",
     "explicacion": "'Por mucho que', 'por más que' + subjuntivo expresan concesión de grado. Contexto pasado → imperfecto de subjuntivo.",
     "trampa": "Contexto presente/futuro: 'por mucho que se esfuerce, no lo conseguirá'.",
     "nivel": "C1"},
    {"frase": "Me alegra que finalmente ella ___ (decidirse) a dar ese paso tan importante.",
     "respuesta": "se haya decidido", "tipo": "Perfecto de subjuntivo",
     "explicacion": "Emoción presente + acción ya ocurrida → perfecto de subjuntivo (haya/hayas + participio).",
     "trampa": "El perfecto de subjuntivo sitúa la acción antes del momento de habla.",
     "nivel": "C1"},
    {"frase": "No hay ningún experto que ___ (poder) predecir con certeza lo que ocurrirá.",
     "respuesta": "pueda", "tipo": "Antecedente negado",
     "explicacion": "Con antecedente negado (ningún, nadie, nada...), la oración de relativo siempre lleva subjuntivo.",
     "trampa": "Si el antecedente existe y es conocido: 'Hay expertos que pueden predecirlo' (indicativo).",
     "nivel": "C1"},
    {"frase": "Antes de que ___ (llegar) los demás, necesitamos hablar de algo importante.",
     "respuesta": "lleguen", "tipo": "Antes de que",
     "explicacion": "'Antes de que' siempre rige subjuntivo porque introduce una acción que aún no ha ocurrido.",
     "trampa": "No confundir con 'después de que + indicativo' (acción ya ocurrida): 'después de que llegaron'.",
     "nivel": "B2"},
    {"frase": "Es una pena que no ___ (poder) asistir a la ceremonia de premiación.",
     "respuesta": "hayas podido", "tipo": "Expresiones de valoración negativa",
     "explicacion": "'Es una pena', 'es una lástima', 'qué pena' + que → subjuntivo. El tiempo depende del contexto.",
     "trampa": "Con 'es una pena' (presente) → perfecto de subjuntivo. Si fuera 'era una pena' (pasado) → imperfecto: pudieras/pudieses.",
     "nivel": "C1"},
    {"frase": "Dondequiera que ___ (ir), siempre encuentra a alguien conocido.",
     "respuesta": "vaya", "tipo": "Pronombres relativos indefinidos",
     "explicacion": "Quienquiera que, dondequiera que, comoquiera que, cuandoquiera que → siempre subjuntivo.",
     "trampa": "Estas formas son propias de registro formal o literario, pero el DELE C1 las incluye.",
     "nivel": "C1"},
    {"frase": "Si ___ (tener) más tiempo, habría revisado el informe con más detenimiento.",
     "respuesta": "hubiera tenido / hubiese tenido", "tipo": "Condicional irreal de pasado (recursos y oportunidad)",
     "explicacion": "Si + pluscuamperfecto de subjuntivo → condicional compuesto. Situación imposible en el pasado.",
     "trampa": "*Si habría tenido* es incorrecto. Nunca 'si + condicional'.",
     "nivel": "C1"},
    {"frase": "Conviene que todos los participantes ___ (revisar) el material antes de la sesión.",
     "respuesta": "revisen", "tipo": "Verbos impersonales de conveniencia",
     "explicacion": "Conviene, importa, basta, interesa + que → subjuntivo porque expresan valoración o necesidad.",
     "trampa": "Contrasta con verbos de percepción o conocimiento + indicativo: 'parece que viene'.",
     "nivel": "C1"},
    {"frase": "No es que ___ (estar) en desacuerdo, sino que necesito más información.",
     "respuesta": "esté", "tipo": "No es que",
     "explicacion": "'No es que' + subjuntivo introduce una negación matizada. No niega el hecho, sino que lo reformula.",
     "trampa": "'No es que esté' (subjuntivo: niega la interpretación) ≠ 'no es que está' (incorrecto).",
     "nivel": "C1"},
    {"frase": "Lo hará, a no ser que algo ___ (impedírselo) en el último momento.",
     "respuesta": "se lo impida", "tipo": "A no ser que",
     "explicacion": "'A no ser que', 'salvo que', 'excepto que' → siempre subjuntivo. Son equivalentes a 'a menos que'.",
     "trampa": "Son condiciones negativas: la acción ocurre salvo que se cumpla la condición.",
     "nivel": "C1"},
    {"frase": "Quizás ___ (tener) razón, pero necesito comprobarlo antes de confirmarlo.",
     "respuesta": "tenga / tiene", "tipo": "Quizás / tal vez",
     "explicacion": "'Quizás' y 'tal vez' admiten indicativo o subjuntivo. Con subjuntivo, la duda es mayor. Con indicativo, el hablante se inclina más a creer que es cierto.",
     "trampa": "Ambas formas son correctas. El subjuntivo expresa más incertidumbre que el indicativo.",
     "nivel": "C1"},
    {"frase": "Por más dinero que ___ (tener), nunca se siente satisfecho.",
     "respuesta": "tenga", "tipo": "Concesivas de grado (presente)",
     "explicacion": "'Por más... que' + subjuntivo: concesión de grado máximo en contexto presente o habitual.",
     "trampa": "Contexto pasado: 'por más que tuviera dinero, nunca se sentía satisfecho' (imperfecto de subjuntivo).",
     "nivel": "C1"},
    {"frase": "Necesito que alguien me ___ (explicar) paso a paso cómo funciona este sistema.",
     "respuesta": "explique", "tipo": "Necesitar que",
     "explicacion": "'Necesitar que' + subjuntivo cuando el sujeto de la subordinada es distinto. Si es el mismo sujeto: 'necesito explicarlo' (infinitivo).",
     "trampa": "Mismo sujeto → infinitivo: 'necesito entenderlo'. Distinto sujeto → subjuntivo: 'necesito que lo entiendas'.",
     "nivel": "B2"},
]

GR_PERIFRASIS: List[Dict] = [
    {"perifrasis": "llevar + gerundio",
     "significado": "Duración acumulada de una acción en curso en el momento de referencia.",
     "ejemplos": ["Llevo tres horas esperando sin que nadie me atienda.",
                  "Cuando llegaste, llevaba trabajando toda la tarde."],
     "trampa": "El complemento responde a '¿cuánto tiempo llevas...?'. No confundir con 'llevar + participio'.",
     "ejercicio": "Lleva ___ (trabajar) en esa empresa más de diez años sin que le hayan ofrecido una promoción.",
     "respuesta": "trabajando", "nivel": "C1"},
    {"perifrasis": "seguir + gerundio",
     "significado": "Indica que una acción continúa sin interrupción.",
     "ejemplos": ["Siguen debatiendo el mismo punto desde hace horas.",
                  "Siguió trabajando hasta el amanecer aunque le aconsejaron que parara."],
     "trampa": "Sinónimo de 'continuar + gerundio', pero más coloquial.",
     "ejercicio": "A pesar de las advertencias, ___ (cometer) los mismos errores una y otra vez.",
     "respuesta": "sigue cometiendo", "nivel": "B2"},
    {"perifrasis": "dejar de + infinitivo",
     "significado": "Interrupción definitiva o temporal de una acción.",
     "ejemplos": ["Dejó de fumar hace tres años.", "No dejes de informarme si hay novedades."],
     "trampa": "Con negación ('no dejes de + inf.') adquiere valor de recomendación: 'no dejes de verla' = asegúrate de verla.",
     "ejercicio": "___ (hablar) con ella desde que tuvieron aquella discusión tan tensa.",
     "respuesta": "Ha dejado de hablar", "nivel": "B2"},
    {"perifrasis": "ponerse a + infinitivo",
     "significado": "Inicio brusco o inesperado de una acción.",
     "ejemplos": ["Sin previo aviso, se puso a llover con una intensidad tremenda.",
                  "En cuanto se sentó, se puso a leer sin saludar a nadie."],
     "trampa": "Indica inicio súbito, no planificado. Contrasta con 'empezar a', más neutro.",
     "ejercicio": "Nada más recibir la noticia, ___ (llorar) sin poder contenerse.",
     "respuesta": "se puso a llorar", "nivel": "B2"},
    {"perifrasis": "volver a + infinitivo",
     "significado": "Repetición de una acción ya realizada anteriormente.",
     "ejemplos": ["Volvió a cometer el mismo error que le habían señalado.",
                  "No quiero volver a pasar por una situación tan incómoda."],
     "trampa": "En negativo expresa voluntad de no repetir: 'no quiero volver a verle' = nunca más.",
     "ejercicio": "Tras años de silencio, ___ (publicar) una novela que ha sorprendido a todos.",
     "respuesta": "ha vuelto a publicar", "nivel": "B2"},
    {"perifrasis": "acabar de + infinitivo",
     "significado": "Acción completada en un momento muy reciente.",
     "ejemplos": ["Acabo de hablar con el director y me ha confirmado los cambios.",
                  "Cuando llegué, acababan de cerrar la puerta."],
     "trampa": "Solo en presente (recién) e imperfecto (antes de otra acción pasada). No en futuro.",
     "ejercicio": "___ (confirmar) que el evento se celebrará tal y como estaba previsto.",
     "respuesta": "Acaban de confirmar", "nivel": "B2"},
    {"perifrasis": "acabar por + infinitivo",
     "significado": "Tras un proceso o resistencia, se llega finalmente a una acción.",
     "ejemplos": ["Aunque al principio se resistía, acabó por aceptar las condiciones.",
                  "Después de tanto debatirlo, acabamos por no tomar ninguna decisión."],
     "trampa": "No confundir con 'acabar de' (reciente) ni 'acabar + gerundio' (resultado gradual).",
     "ejercicio": "Tras meses de negociaciones, ___ (firmar) un acuerdo que nadie esperaba.",
     "respuesta": "acabaron por firmar", "nivel": "C1"},
    {"perifrasis": "andar + gerundio",
     "significado": "Acción habitual o persistente, con matiz de dispersión o actividad continua.",
     "ejemplos": ["Anda buscando trabajo desde que lo despidieron.",
                  "No me gusta que anden comentando mis asuntos a mis espaldas."],
     "trampa": "Más coloquial que 'estar + gerundio'. Implica cierta repetición o dispersión.",
     "ejercicio": "Últimamente ___ (quejarse) de todo sin proponer ninguna alternativa.",
     "respuesta": "anda quejándose", "nivel": "C1"},
    {"perifrasis": "deber de + infinitivo",
     "significado": "Deducción lógica o probabilidad (con 'de'). Sin 'de': obligación moral.",
     "ejemplos": ["Debe de ser muy tarde; no hay nadie en las calles.",
                  "A juzgar por su cara, debe de estar agotada."],
     "trampa": "'Deber + inf.' = obligación. 'Deber DE + inf.' = deducción. El DELE exige distinguirlos.",
     "ejercicio": "No ha contestado ningún mensaje en todo el día; ___ (estar) muy ocupado.",
     "respuesta": "debe de estar", "nivel": "C1"},
    {"perifrasis": "ir a + infinitivo",
     "significado": "Intención, plan o predicción inmediata sobre el futuro.",
     "ejemplos": ["Vamos a revisar todos los puntos antes de decidir.",
                  "Con esa actitud, va a perder la confianza de todo el equipo."],
     "trampa": "En imperfecto expresa algo que iba a ocurrir pero se interrumpió: 'iba a llamarte pero se me fue'.",
     "ejercicio": "Según las previsiones, ___ (producirse) un cambio significativo en el sector.",
     "respuesta": "va a producirse", "nivel": "B2"},
    {"perifrasis": "tener que + infinitivo",
     "significado": "Obligación o necesidad impuesta externamente, o deducción del hablante.",
     "ejemplos": ["Tienes que entregar el formulario antes del viernes sin falta.",
                  "Tiene que haber algún malentendido; esto no puede ser correcto."],
     "trampa": "Segundo uso (deducción) equivale a 'deber de': 'tiene que haber un error' = deduzco que hay un error.",
     "ejercicio": "Con tan pocos recursos, ___ (priorizar) muy bien cada gasto para llegar a fin de mes.",
     "respuesta": "tendrán que priorizar", "nivel": "B2"},
    {"perifrasis": "quedar en + infinitivo",
     "significado": "Acuerdo o compromiso adoptado entre dos o más personas.",
     "ejemplos": ["Quedamos en llamarnos el lunes para confirmar los detalles.",
                  "¿No habíais quedado en no comentar nada hasta que fuera oficial?"],
     "trampa": "No confundir con 'quedar + gerundio' (resultado) ni 'quedar con' (citarse con alguien).",
     "ejercicio": "Según lo acordado, habíamos ___ (vernos) aquí a las seis en punto.",
     "respuesta": "quedado en vernos", "nivel": "C1"},
    {"perifrasis": "terminar de + infinitivo",
     "significado": "Completar una acción o proceso. Con negación: no llegar a comprender algo.",
     "ejemplos": ["Cuando termines de leer el informe, dime qué piensas.",
                  "No termino de entender por qué tomaron esa decisión."],
     "trampa": "'No terminar de + infinitivo' expresa perplejidad o resistencia: 'no termino de creerlo' = me cuesta creerlo.",
     "ejercicio": "No ___ (entender) por qué rechazaron una propuesta tan sólida.",
     "respuesta": "termino de entender", "nivel": "C1"},
    {"perifrasis": "echar a + infinitivo",
     "significado": "Inicio repentino de una acción, especialmente involuntaria o emocional.",
     "ejemplos": ["Al oír la noticia, echó a correr sin mirar atrás.",
                  "Se echó a reír en el momento más inapropiado."],
     "trampa": "Similar a 'ponerse a', pero más literario y con verbos concretos: correr, volar, andar, reír, llorar.",
     "ejercicio": "Cuando le contaron el chiste, ___ (reír) sin poder contenerse.",
     "respuesta": "echó a reír", "nivel": "C1"},
    {"perifrasis": "estar a punto de + infinitivo",
     "significado": "Acción inminente que está a punto de ocurrir o que estuvo a punto de ocurrir.",
     "ejemplos": ["Estábamos a punto de marcharnos cuando llegaste.",
                  "Está a punto de firmar el contrato más importante de su carrera."],
     "trampa": "En imperfecto expresa una acción que estuvo a punto de suceder: 'estaba a punto de llamarte'.",
     "ejercicio": "Cuando sonó el teléfono, ___ (quedarse) dormida en el sofá.",
     "respuesta": "estaba a punto de quedarse", "nivel": "C1"},
    {"perifrasis": "llevar + participio",
     "significado": "Cantidad acumulada de objetos o resultados de una acción completada. El participio concuerda en género y número con el objeto directo.",
     "ejemplos": ["Llevo leídas tres novelas este mes.",
                  "Llevan escritas más de veinte páginas del informe."],
     "trampa": "No confundir con 'llevar + gerundio' (duración de acción en curso). El participio concuerda con el OD.",
     "ejercicio": "Para cuando lleguen, nosotros ya ___ (preparar) todas las presentaciones.",
     "respuesta": "llevaremos preparadas", "nivel": "C2"},
    {"perifrasis": "acabar + gerundio",
     "significado": "Resultado final gradual de un proceso: se llega a ese estado de forma progresiva.",
     "ejemplos": ["Acabó creyendo que tenía razón después de tanto insistir.",
                  "Si sigues así, acabarás arrepintiéndote de esta decisión."],
     "trampa": "Contrasta con 'acabar por + infinitivo' (tras resistencia) y 'acabar de + infinitivo' (acción reciente).",
     "ejercicio": "Aunque al principio no le gustaba, ___ (enamorarse) de la ciudad.",
     "respuesta": "acabó enamorándose", "nivel": "C1"},
    {"perifrasis": "parar de + infinitivo",
     "significado": "Interrupción de una acción, generalmente de forma más brusca que 'dejar de'.",
     "ejemplos": ["No para de hablar desde que llegó.",
                  "¿Puedes parar de hacer ruido un momento?"],
     "trampa": "En negativo, 'no parar de + infinitivo' expresa que la acción es continua e incesante.",
     "ejercicio": "La alarma no ___ (sonar) desde las cinco de la mañana; ha sido desesperante.",
     "respuesta": "ha parado de sonar", "nivel": "B2"},
    {"perifrasis": "venir + gerundio",
     "significado": "Acción que se ha ido desarrollando de forma gradual a lo largo de un período.",
     "ejemplos": ["Vengo diciéndole lo mismo desde hace meses, pero no escucha.",
                  "Esto viene ocurriendo desde mucho antes de que llegáramos nosotros."],
     "trampa": "Indica proceso gradual y acumulativo, a diferencia de 'llevar + gerundio' (duración puntual medible).",
     "ejercicio": "Los expertos ___ (advertir) sobre este riesgo desde hace más de una década.",
     "respuesta": "vienen advirtiendo", "nivel": "C1"},
]

GR_SER_ESTAR: List[Dict] = [
    {"frase": "El cielo ___ muy azul esta mañana.",
     "respuesta": "está", "tipo": "Estado temporal vs característica",
     "explicacion": "'Estar' para estados temporales o perceptibles en un momento concreto. 'Esta mañana' indica temporalidad → estar. 'El cielo es azul' (en general) también sería válido sin marcador temporal.",
     "trampa": "Cuando hay marcador temporal (hoy, esta mañana, ahora...) la tendencia es estar.",
     "nivel": "B2"},
    {"frase": "Mi vecino ___ médico, pero últimamente ___ muy cansado.",
     "respuesta": "es / está", "tipo": "Profesión vs estado",
     "explicacion": "Profesión o identidad permanente → ser. Estado físico o emocional temporal → estar.",
     "trampa": "Con adjetivos que cambian de significado: 'es aburrido' (su carácter) vs 'está aburrido' (ahora).",
     "nivel": "B2"},
    {"frase": "La reunión ___ en la sala de conferencias del tercer piso.",
     "respuesta": "es", "tipo": "Ubicación de eventos vs cosas",
     "explicacion": "La ubicación de EVENTOS → ser ('la reunión es en...'). La ubicación de COSAS o PERSONAS → estar ('el libro está en...').",
     "trampa": "Es el error más frecuente de anglohablantes. En inglés siempre 'is' → los estudiantes usan 'está' para todo.",
     "nivel": "C1"},
    {"frase": "Este ejercicio ___ muy difícil para el nivel que tiene.",
     "respuesta": "es", "tipo": "Característica inherente",
     "explicacion": "Dificultad como característica del ejercicio → ser. Si dijéramos 'está muy difícil hoy' implicaría que normalmente no lo es (cambio de estado).",
     "trampa": "'El examen estuvo muy difícil' (valoración del resultado, con indefinido) → estar. 'Es muy difícil' (característica) → ser.",
     "nivel": "C1"},
    {"frase": "La fruta ___ muy cara en este mercado.",
     "respuesta": "está", "tipo": "Precio como estado",
     "explicacion": "Los precios en español se expresan con 'estar' porque son condiciones variables y no características permanentes: 'el pan está a 2 euros'.",
     "trampa": "Anglohablantes suelen decir *'es cara'*. En español, los precios y condiciones del mercado → estar.",
     "nivel": "C1"},
    {"frase": "Todos ___ invitados a la ceremonia de inauguración.",
     "respuesta": "están", "tipo": "Participio como resultado",
     "explicacion": "Estar + participio expresa el resultado de una acción: 'están invitados' = han sido invitados y se encuentran en ese estado. No confundir con la pasiva (ser + participio).",
     "trampa": "'Son invitados' = voz pasiva (los invitan). 'Están invitados' = resultado, estado.",
     "nivel": "C1"},
    {"frase": "La película ___ basada en hechos reales.",
     "respuesta": "está", "tipo": "Participio adjetival",
     "explicacion": "'Estar + participio' describe el estado resultante: 'está basada' = ha sido basada y se encuentra en ese estado. 'Ser basada' sería una pasiva rara sin agente; en esta estructura solo 'estar' es natural.",
     "trampa": "Cuidado: 'es una película basada en...' sí es correcto, pero cambia la estructura. En 'La película ___ basada', el único verbo posible es 'estar'.",
     "nivel": "C1"},
    {"frase": "¡___ listo! Nos vamos en cinco minutos.",
     "respuesta": "Está listo", "tipo": "Adjetivos con doble significado",
     "explicacion": "'Ser listo' = ser inteligente. 'Estar listo' = estar preparado/terminado. El contexto ('nos vamos') indica preparación → estar.",
     "trampa": "Otros pares: ser malo vs estar malo (enfermo); ser bueno vs estar bueno (sabroso/atractivo); ser vivo vs estar vivo.",
     "nivel": "C1"},
    {"frase": "El acuerdo ___ firmado por ambas partes el pasado martes.",
     "respuesta": "fue", "tipo": "Pasiva perifrástica (ser + participio)",
     "explicacion": "La pasiva perifrástica usa SER + participio para indicar que el sujeto paciente recibe la acción. 'Fue firmado' = alguien lo firmó. No confundir con estar + participio (resultado).",
     "trampa": "'Fue firmado' (pasiva, acción) vs 'está firmado' (estado resultante). El DELE puede preguntar esta diferencia.",
     "nivel": "C1"},
    {"frase": "Después de la operación, ___ mucho mejor que antes.",
     "respuesta": "está", "tipo": "Estado de salud",
     "explicacion": "El estado de salud, tanto bueno como malo, siempre va con estar: 'está bien', 'está mejor', 'está peor', 'está enfermo'.",
     "trampa": "*Es mejor* podría referirse a su calidad como persona. 'Está mejor' se refiere inequívocamente al estado de salud.",
     "nivel": "B2"},
    {"frase": "La conferencia ___ muy interesante; aprendimos muchísimo.",
     "respuesta": "estuvo", "tipo": "Valoración de un evento",
     "explicacion": "La valoración de un evento puntual ya concluido → estar en indefinido ('estuvo'). Si fuera una característica permanente → ser ('es interesante como persona').",
     "trampa": "'Es interesante' (característica habitual) vs 'estuvo interesante' (valoración de algo ya terminado).",
     "nivel": "C1"},
    {"frase": "No ___ segura de si debo aceptar la oferta o no.",
     "respuesta": "estoy", "tipo": "Estado de certeza",
     "explicacion": "'Estar seguro/a de' expresa un estado de certeza o duda momentáneo. 'Ser seguro' significaría algo o alguien que inspira seguridad o que es fiable.",
     "trampa": "'Estar seguro de algo' (certeza) vs 'ser una persona segura' (confiada, fiable).",
     "nivel": "C1"},
    {"frase": "___ de Barcelona, pero llevo diez años viviendo en Madrid.",
     "respuesta": "Soy", "tipo": "Origen y procedencia",
     "explicacion": "El origen o procedencia geográfica → siempre ser: 'soy de Barcelona', 'es de Argentina'.",
     "trampa": "No confundir con la ubicación actual: 'estoy en Barcelona' (lugar donde estoy ahora).",
     "nivel": "B2"},
    {"frase": "La casa ___ muy bien situada: cerca del metro y del parque.",
     "respuesta": "está", "tipo": "Ubicación de cosas y personas",
     "explicacion": "La ubicación de cosas, personas y animales → estar. Solo los eventos van con ser ('la boda es en el jardín').",
     "trampa": "Error frecuente: *'la casa es cerca del metro'*. La ubicación de objetos físicos siempre es estar.",
     "nivel": "B2"},
    {"frase": "Ayer la sopa ___ buenísima. ¿Cómo la hiciste?",
     "respuesta": "estaba / estuvo", "tipo": "Adjetivos de percepción sensorial",
     "explicacion": "Para describir cómo está algo al probarlo, olerlo o tocarlo → estar: 'está bueno/rico/frío/caliente'.",
     "trampa": "'Ser bueno' = tener buen carácter/calidad general. 'Estar bueno' = saber bien o tener buen aspecto.",
     "nivel": "B2"},
    {"frase": "Su padre ___ abogado, pero ___ de baja desde el accidente.",
     "respuesta": "es / está", "tipo": "Profesión vs estado temporal",
     "explicacion": "Profesión permanente → ser. Situación laboral temporal (de baja, de vacaciones, de viaje) → estar.",
     "trampa": "Estar de baja, estar de vacaciones, estar de guardia: estas expresiones fijas siempre usan estar.",
     "nivel": "B2"},
    {"frase": "La frontera entre los dos países ___ a unos 50 kilómetros de aquí.",
     "respuesta": "está", "tipo": "Ubicación con distancia",
     "explicacion": "La ubicación física, incluso expresada con distancia → estar. 'La frontera está a 50 km'.",
     "trampa": "No existe excepción para ubicaciones con distancia: siempre estar para cosas y personas.",
     "nivel": "B2"},
    {"frase": "No me gusta cómo ___ pintadas las paredes de ese edificio.",
     "respuesta": "están", "tipo": "Estado resultante + participio",
     "explicacion": "Estar + participio = estado resultado de una acción previa. Las paredes han sido pintadas y se encuentran en ese estado.",
     "trampa": "'Las paredes son pintadas' sería pasiva (alguien las pinta). 'Las paredes están pintadas' = resultado.",
     "nivel": "C1"},
    {"frase": "Este artículo ___ escrito en un español muy formal y académico.",
     "respuesta": "está", "tipo": "Participio adjetival de modo",
     "explicacion": "'Estar escrito de cierta manera' describe el estado o modo del texto como resultado. El participio funciona como adjetivo.",
     "trampa": "'Fue escrito por Cervantes' (pasiva, agente) vs 'está escrito en latín' (estado, modo).",
     "nivel": "C1"},
    {"frase": "Me parece que ___ equivocado en su interpretación de los datos.",
     "respuesta": "está", "tipo": "Estado de error o acierto",
     "explicacion": "Estar equivocado/acertado/confundido/perdido → estados temporales → estar.",
     "trampa": "*'Es equivocado'* implicaría que equivocarse es parte de su identidad permanente, lo cual es raro.",
     "nivel": "B2"},
]


# ═══════════════════════════════════════════════════════════
#  DATOS — GRAMÁTICA C1 · PRONOMBRES, ERRORES, LECTURA
# ═══════════════════════════════════════════════════════════

GR_PRONOMBRES = [
    {"tipo": "Combinación OI + OD",
     "pregunta": "¿Cuál es la forma correcta?\n\n«Le di el libro a María» → con pronombres completos:",
     "opciones": ["Le lo di", "Se lo di", "Lo le di", "Le di lo"],
     "respuesta": "Se lo di",
     "explicacion": "Cuando el OI (le/les) precede al OD (lo/la/los/las), el OI se convierte en 'se'. Nunca *le lo, le la, les lo...*",
     "nivel": "B2"},
    {"tipo": "Posición con infinitivo",
     "pregunta": "¿Cuál es la opción correcta?\n\n«Quiero decir la verdad a ti» → con pronombres:",
     "opciones": ["Te quiero decirla", "Quiero decírtela", "Las dos son correctas", "Quiero la decirte"],
     "respuesta": "Las dos son correctas",
     "explicacion": "Con perífrasis o verbo + infinitivo, los pronombres pueden ir delante del conjugado O enclíticos al infinitivo: 'te lo quiero decir' = 'quiero decírtelo'.",
     "nivel": "B2"},
    {"tipo": "Leísmo aceptado",
     "pregunta": "¿Cuál es la opción normativa según la RAE?\n\n«Vi a tu hermano ayer»",
     "opciones": ["Le vi ayer", "Lo vi ayer", "Las dos son aceptadas por la RAE", "Solo 'lo' es correcto"],
     "respuesta": "Las dos son aceptadas por la RAE",
     "explicacion": "El leísmo de persona masculina singular está aceptado por la RAE. 'Le vi' y 'lo vi' son ambos válidos. El leísmo de cosa (*le compré* para un objeto) no está aceptado.",
     "nivel": "C1"},
    {"tipo": "Posición con gerundio",
     "pregunta": "Elige la opción correcta:\n\n«Está explicando el problema a los estudiantes»",
     "opciones": ["Se los está explicando", "Está explicándoselo", "Las dos son correctas", "Les lo está explicando"],
     "respuesta": "Las dos son correctas",
     "explicacion": "Con estar + gerundio, los pronombres van delante de 'está' O enclíticos al gerundio: 'se lo está explicando' = 'está explicándoselo'.",
     "nivel": "C1"},
    {"tipo": "Duplicación de OI obligatoria",
     "pregunta": "¿Cuál de estas frases es correcta en español estándar?",
     "opciones": ["A María compré un regalo", "A María le compré un regalo",
                  "Le compré a María", "Compré a María un regalo"],
     "respuesta": "A María le compré un regalo",
     "explicacion": "Cuando el OI aparece explícito ('a María'), el pronombre OI (le) TAMBIÉN debe aparecer. Esta duplicación es obligatoria en la mayoría de los dialectos.",
     "nivel": "C1"},
    {"tipo": "Se impersonal vs pasiva refleja",
     "pregunta": "¿Cuál es la diferencia?\n\n«Se busca secretaria» vs «Se buscan secretarias»",
     "opciones": [
         "Ninguna, son intercambiables",
         "La primera es pasiva refleja; la segunda es impersonal",
         "La primera puede ser impersonal; la segunda es pasiva refleja (concuerda con el sujeto)",
         "Ambas son pasivas reflejas",
     ],
     "respuesta": "La primera puede ser impersonal; la segunda es pasiva refleja (concuerda con el sujeto)",
     "explicacion": "'Se busca secretaria': impersonal, verbo en singular. 'Se buscan secretarias': pasiva refleja, el verbo concuerda con 'secretarias'.",
     "nivel": "C2"},
    {"tipo": "Imperativo con pronombres",
     "pregunta": "¿Cuál es la forma correcta?\n\n«Dile a tu hermana que venga» → con pronombre:",
     "opciones": ["Díla que venga", "Dísela que venga", "Dile que venga", "Se dile que venga"],
     "respuesta": "Dile que venga",
     "explicacion": "Solo hay OI ('a tu hermana' → le). La subordinada 'que venga' no se pronominaliza. El pronombre va enclítico al imperativo: 'dile'.",
     "nivel": "C1"},
    {"tipo": "Se aspectual-afectivo",
     "pregunta": "¿Qué añade 'se' en: «Se comió toda la pizza»?",
     "opciones": [
         "Reflexividad (la acción recae sobre el sujeto)",
         "Matiz de completitud o afectación total del sujeto",
         "Pasiva refleja",
         "Nada, es redundante",
     ],
     "respuesta": "Matiz de completitud o afectación total del sujeto",
     "explicacion": "El 'se' aspectual añade completitud: 'comió pizza' (algo de pizza) vs 'se comió la pizza' (toda entera, con mayor implicación del sujeto).",
     "nivel": "C2"},
    {"tipo": "OD con a personal",
     "pregunta": "¿Cuál es la forma correcta?",
     "opciones": [
         "Vi tu hermana en el mercado",
         "Vi a tu hermana en el mercado",
         "Le vi a tu hermana en el mercado",
         "Vi la tu hermana en el mercado",
     ],
     "respuesta": "Vi a tu hermana en el mercado",
     "explicacion": "En español, el OD de persona va introducido por 'a personal': 'vi a María', 'llamé a mi madre'. Sin la 'a', la frase es incorrecta.",
     "nivel": "B2"},
    {"tipo": "Pronombre con cambio de significado verbal",
     "pregunta": "¿Qué diferencia hay entre «fue» y «se fue»?",
     "opciones": [
         "Ninguna diferencia real",
         "'Fue' = desplazamiento hacia un lugar; 'se fue' = marcharse, alejarse con énfasis en la separación",
         "'Se fue' es incorrecto en español normativo",
         "'Fue' implica ida y vuelta; 'se fue' solo ida",
     ],
     "respuesta": "'Fue' = desplazamiento hacia un lugar; 'se fue' = marcharse, alejarse con énfasis en la separación",
     "explicacion": "El 'se' cambia el matiz: 'fue al médico' (se desplazó) vs 'se fue' (partió, se marchó, énfasis en el alejamiento definitivo).",
     "nivel": "C1"},
    {"tipo": "Posición en imperativo negativo",
     "pregunta": "¿Cuál es la forma correcta del imperativo negativo?",
     "opciones": ["No dímelo", "No me lo digas", "No digas me lo", "Dímelo no"],
     "respuesta": "No me lo digas",
     "explicacion": "En el imperativo negativo, los pronombres van DELANTE del verbo: 'no me lo digas', 'no te vayas'. Solo en el afirmativo van detrás: 'dímelo', 'vete'.",
     "nivel": "C1"},
    {"tipo": "Concordancia del participio",
     "pregunta": "¿Cuál es la frase correcta?\n\n«Los informes que te he enviado»",
     "opciones": [
         "Los informes que te he enviados",
         "Los informes que te he enviado",
         "Los informes que se los he enviado",
         "Los informes que le he enviado",
     ],
     "respuesta": "Los informes que te he enviado",
     "explicacion": "En los tiempos compuestos con haber, el participio NO concuerda con el OD: 'he enviado los informes'. La concordancia (*enviados*) es un arcaísmo.",
     "nivel": "C2"},
]

GR_ERRORES_INGLES = [
    {"categoria": "Falso amigo: embarazada",
     "error": "Estoy muy *embarazada* por lo que dijiste delante de todos.",
     "correccion": "Estoy muy avergonzada / me ha dado mucha vergüenza lo que dijiste.",
     "explicacion": "'Embarazada' = pregnant. 'Embarrassed' (inglés) = avergonzado/a.",
     "extra": "Más falsos amigos: 'sensible' (sensitivo ≠ sensible), 'actual' (real ≠ actual), 'library' (biblioteca ≠ librería).",
     "nivel": "B2"},
    {"categoria": "Falso amigo: excitado",
     "error": "Estoy muy *excitado* por el concierto de esta noche.",
     "correccion": "Estoy muy emocionado / ilusionado / entusiasmado con el concierto.",
     "explicacion": "'Excitado' en español tiene connotación sexual en muchos contextos. 'Excited' = emocionado, entusiasmado.",
     "extra": "Alternativas seguras: emocionado, ilusionado, entusiasmado, con muchas ganas.",
     "nivel": "B2"},
    {"categoria": "Haber impersonal",
     "error": "*Habían* muchas personas en la reunión de ayer.",
     "correccion": "Había muchas personas en la reunión de ayer.",
     "explicacion": "'Haber' existencial es impersonal: siempre en singular. *Habían, hubieron* (existencial) son incorrectos según la norma.",
     "extra": "Correcto: 'Hay mucha gente', 'Había varios problemas'. Incorrecto: *'habían cambios'*.",
     "nivel": "C1"},
    {"categoria": "Por vs Para: finalidad",
     "error": "Lo hice *por* impresionarte en la reunión.",
     "correccion": "Lo hice para impresionarte en la reunión.",
     "explicacion": "'Para + infinitivo' = finalidad o propósito consciente. 'Por + infinitivo' = causa: 'lo hice por miedo'.",
     "extra": "PARA = destino, finalidad, destinatario, plazo. POR = causa, duración, intercambio, agente pasiva.",
     "nivel": "C1"},
    {"categoria": "Ser vs Estar: ubicación de eventos",
     "error": "La boda *está* en el jardín del hotel.",
     "correccion": "La boda es en el jardín del hotel.",
     "explicacion": "Los EVENTOS se ubican con 'ser'. Solo cosas y personas usan 'estar' para ubicación.",
     "extra": "Truco: si puedes decir 'tiene lugar en', es un evento → ser.",
     "nivel": "C1"},
    {"categoria": "Queísmo",
     "error": "Estoy seguro *que* vendrá mañana.",
     "correccion": "Estoy seguro de que vendrá mañana.",
     "explicacion": "Queísmo: omitir 'de' donde sí corresponde. 'Estar seguro de que', 'acordarse de que', 'darse cuenta de que' requieren 'de'.",
     "extra": "Truco: sustituye por 'eso'. 'Estoy seguro de eso' → necesitas 'de'. 'Pienso eso' → no necesitas 'de'.",
     "nivel": "C1"},
    {"categoria": "Dequeísmo",
     "error": "Pienso *de que* es una decisión equivocada.",
     "correccion": "Pienso que es una decisión equivocada.",
     "explicacion": "Dequeísmo: añadir 'de' donde no corresponde. 'Pensar que', 'creer que', 'decir que' no llevan 'de'.",
     "extra": "Mismo truco: 'pienso eso' (sin 'de') → no lleva 'de'. 'Estoy seguro de eso' → sí lleva 'de'.",
     "nivel": "C1"},
    {"categoria": "Tiempos: habitual vs puntual",
     "error": "Cuando era pequeña, *fui* a la playa todos los veranos.",
     "correccion": "Cuando era pequeña, iba a la playa todos los veranos.",
     "explicacion": "Imperfecto para acciones habituales en el pasado. 'Todos los veranos' indica habitualidad → imperfecto.",
     "extra": "'El verano pasado fui' (puntual → indefinido) vs 'de pequeña iba' (habitual → imperfecto).",
     "nivel": "B2"},
    {"categoria": "Verbos de cambio de estado",
     "error": "Me *hice* muy cansada después del trabajo.",
     "correccion": "Me puse muy cansada / Me quedé agotada después del trabajo.",
     "explicacion": "'Hacerse' = cambios de identidad (hacerse médico, famoso). Para estados físicos temporales: 'ponerse' o 'quedarse'.",
     "extra": "PONERSE (cambio rápido, emocional), QUEDARSE (resultado, involuntario), VOLVERSE (carácter), HACERSE (identidad).",
     "nivel": "C1"},
    {"categoria": "Artículo con genéricos",
     "error": "*Vida* es muy corta para perder el tiempo.",
     "correccion": "La vida es muy corta para perder el tiempo.",
     "explicacion": "En español, los sustantivos en sentido genérico llevan artículo: 'la vida', 'el tiempo'. En inglés no: 'Life is short'.",
     "extra": "Más ejemplos: 'la música es universal', 'el dinero no da la felicidad', 'los niños aprenden rápido'.",
     "nivel": "B2"},
    {"categoria": "Preposición ante subordinada",
     "error": "*Depende si* vienes o no.",
     "correccion": "Depende de si vienes o no.",
     "explicacion": "Los verbos que rigen preposición la mantienen ante subordinadas. 'Depender de algo' → 'depender de si...'.",
     "extra": "Más: 'acordarse de que', 'asegurarse de que', 'convencerse de que', 'olvidarse de que'.",
     "nivel": "C1"},
    {"categoria": "Orden del adverbio",
     "error": "Estoy de acuerdo con usted *completamente*.",
     "correccion": "Estoy completamente de acuerdo con usted.",
     "explicacion": "Los adverbios de grado van generalmente antes del grupo verbal en español, no al final como en inglés.",
     "extra": "Más natural: 'Estoy totalmente de acuerdo', 'Coincido plenamente', 'No podría estar más de acuerdo'.",
     "nivel": "C1"},
    {"categoria": "Falso amigo: realizar",
     "error": "De repente *realicé* que había cometido un error.",
     "correccion": "De repente me di cuenta de que había cometido un error.",
     "explicacion": "'Realizar' en español = llevar a cabo ('realizar una tarea'). 'To realize' = darse cuenta. El calco es incorrecto en español normativo.",
     "extra": "También: 'to make a decision' ≠ *hacer una decisión* → 'tomar una decisión'.",
     "nivel": "C1"},
    {"categoria": "Pasiva: uso excesivo",
     "error": "El informe fue escrito *por mí* ayer por la tarde.",
     "correccion": "Yo escribí el informe ayer. / El informe lo escribí yo.",
     "explicacion": "El español prefiere la voz activa. El uso excesivo de la pasiva perifrástica con agente explícito es un anglicismo frecuente.",
     "extra": "La pasiva refleja (se + verbo) es más natural: 'se publicó el informe', 'se vendieron muchas entradas'.",
     "nivel": "C1"},
]

GR_LECTURA = [
    {
        "titulo": "La paradoja de la elección",
        "fuente": "Texto adaptado · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "En las últimas décadas, la proliferación de opciones en todos los ámbitos de la vida cotidiana "
            "ha sido presentada como un síntoma inequívoco de progreso y libertad. Sin embargo, el psicólogo "
            "Barry Schwartz argumenta que el exceso de opciones no solo no nos hace más libres, sino que nos "
            "paraliza y nos hace, paradójicamente, menos satisfechos.\n\n"
            "Schwartz distingue entre dos tipos de personas: los \"maximizadores\", que exploran todas las "
            "opciones antes de decidir, y los \"satisficientes\", que eligen la primera alternativa que cumpla "
            "sus criterios mínimos. Los maximizadores toman mejores decisiones objetivamente, pero reportan menor "
            "satisfacción: cuantas más opciones consideraron, mayor es el pesar por las no elegidas.\n\n"
            "Este fenómeno, el \"coste de oportunidad psicológico\", se agrava en un mundo de infinitas opciones, "
            "donde conformarse se percibe como fracaso personal. La implicación es clara: más opciones no equivale "
            "necesariamente a más libertad real."
        ),
        "preguntas": [
            {"pregunta": "¿Cuál es la tesis principal del texto?",
             "opciones": ["a) Más opciones siempre mejora la calidad de vida.",
                          "b) El exceso de opciones puede reducir la satisfacción personal.",
                          "c) Los maximizadores son más felices que los satisficientes.",
                          "d) La libertad de elección es un mito moderno."],
             "respuesta": "b) El exceso de opciones puede reducir la satisfacción personal.",
             "explicacion": "El texto argumenta que más opciones genera más insatisfacción. Las otras opciones contradicen o exageran el argumento."},
            {"pregunta": "¿Por qué los maximizadores reportan menor satisfacción?",
             "opciones": ["a) Porque siempre toman peores decisiones.",
                          "b) Porque dedican demasiado tiempo a decidir.",
                          "c) Porque el pesar por las opciones no elegidas es mayor.",
                          "d) Porque no tienen criterios claros."],
             "respuesta": "c) Porque el pesar por las opciones no elegidas es mayor.",
             "explicacion": "El texto dice: 'mayor es el pesar por las no elegidas'. No es el tiempo invertido, sino el coste emocional de lo descartado."},
            {"pregunta": "¿Qué implica el texto sobre libertad y opciones?",
             "opciones": ["a) Más libertad siempre conlleva más opciones.",
                          "b) La libertad solo existe con pocas opciones.",
                          "c) A partir de cierto punto, más opciones no equivalen a más libertad real.",
                          "d) La libertad es incompatible con la satisfacción."],
             "respuesta": "c) A partir de cierto punto, más opciones no equivalen a más libertad real.",
             "explicacion": "La conclusión del texto: 'Más opciones no equivale necesariamente a más libertad real'."},
        ],
    },
    {
        "titulo": "La economía del sueño",
        "fuente": "Texto adaptado · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "Dormir bien no es solo una cuestión de bienestar individual. Es un factor estratégico para la "
            "productividad económica. Se estima que en países como Estados Unidos, Japón o Alemania, la "
            "privación de sueño cuesta entre el 1,5 y el 3% del PIB anual.\n\n"
            "La paradoja es notable: las mismas culturas que generan ese déficit de sueño lo penalizan "
            "socialmente. Quien duerme en el trabajo es tachado de perezoso; quien trabaja sin parar recibe "
            "aplausos. Esta glorificación del agotamiento —la \"cultura del hustle\"— no solo es "
            "contraproducente económicamente, sino que genera consecuencias negativas para la salud pública.\n\n"
            "Algunas empresas han implementado cabinas de siesta u horarios más flexibles. Sin embargo, los "
            "críticos señalan que, sin un cambio cultural profundo, estas medidas son parches estéticos. "
            "La conclusión científica es inequívoca: somos peores en creatividad, toma de decisiones y empatía "
            "cuando dormimos mal. Una sociedad que duerme mal toma peores decisiones colectivas."
        ),
        "preguntas": [
            {"pregunta": "¿Cuál es la paradoja principal del texto?",
             "opciones": ["a) Dormir bien mejora la productividad pero perjudica la economía.",
                          "b) Las culturas que generan déficit de sueño penalizan a quien duerme.",
                          "c) Las empresas invierten en el sueño pero los empleados lo rechazan.",
                          "d) El sueño es valorado en teoría pero ignorado por la ciencia."],
             "respuesta": "b) Las culturas que generan déficit de sueño penalizan a quien duerme.",
             "explicacion": "Las mismas culturas que producen el déficit castigan socialmente a quien duerme en el trabajo."},
            {"pregunta": "¿Qué crítica se hace a las medidas empresariales?",
             "opciones": ["a) Son demasiado caras.",
                          "b) Los empleados no las usan.",
                          "c) Son superficiales sin cambio cultural de fondo.",
                          "d) Generan desigualdad entre trabajadores."],
             "respuesta": "c) Son superficiales sin cambio cultural de fondo.",
             "explicacion": "El texto: 'sin un cambio cultural profundo, no son más que parches estéticos que no abordan la raíz del problema'."},
            {"pregunta": "¿Qué conclusión extrae el texto?",
             "opciones": ["a) Las empresas deben instalar salas de descanso.",
                          "b) El déficit de sueño perjudica al individuo y a la sociedad.",
                          "c) La economía moderna ha resuelto el problema del sueño.",
                          "d) Dormir bien es solo una cuestión personal."],
             "respuesta": "b) El déficit de sueño perjudica al individuo y a la sociedad.",
             "explicacion": "Somos peores en todo cuando dormimos mal, y 'una sociedad que duerme mal toma peores decisiones colectivas'."},
        ],
    },
    {
        "titulo": "El español en el mundo digital",
        "fuente": "Texto adaptado · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "El español es hoy la segunda lengua del mundo por número de hablantes nativos. Sin embargo, "
            "en el entorno digital su presencia es desproporcionadamente baja: solo el 4% de los contenidos "
            "de Internet está en español, frente al 60% en inglés, pese a que los hispanohablantes representan "
            "casi el 8% de la población mundial conectada.\n\n"
            "Esta brecha tiene consecuencias prácticas: menor disponibilidad de contenidos especializados y "
            "dependencia del inglés para acceder a ciencia y tecnología. Paradójicamente, el español crece "
            "en redes sociales y comunicación informal, pero su presencia en repositorios de conocimiento "
            "formal sigue siendo marginal.\n\n"
            "Parte del problema radica en la fragmentación del mercado hispanohablante: veinte países, "
            "múltiples variedades, estándares técnicos distintos. No obstante, el creciente volumen de "
            "contenido generado por usuarios —podcasts, vídeos, blogs— está comenzando a alterar el "
            "equilibrio, aunque de forma todavía insuficiente."
        ),
        "preguntas": [
            {"pregunta": "¿Cuál es la situación paradójica que describe el texto?",
             "opciones": ["a) El español tiene muchos hablantes pero pocos usuarios de internet.",
                          "b) El español crece en comunicación informal pero es marginal en conocimiento formal digital.",
                          "c) El español tiene muchos contenidos pero de baja calidad.",
                          "d) Los hispanohablantes prefieren consumir contenidos en inglés."],
             "respuesta": "b) El español crece en comunicación informal pero es marginal en conocimiento formal digital.",
             "explicacion": "El texto: 'mientras el español crece como lengua de comunicación interpersonal... su presencia en los repositorios de conocimiento formal sigue siendo marginal'."},
            {"pregunta": "¿Qué factor dificulta las plataformas digitales en español?",
             "opciones": ["a) La falta de inversión económica.",
                          "b) La preferencia de los usuarios por el inglés.",
                          "c) La fragmentación en veinte países con variedades y estándares distintos.",
                          "d) La ausencia de políticas lingüísticas comunes."],
             "respuesta": "c) La fragmentación en veinte países con variedades y estándares distintos.",
             "explicacion": "El texto señala explícitamente: 'la fragmentación del mercado hispanohablante: veinte países, múltiples variedades, estándares técnicos diferentes'."},
            {"pregunta": "¿Qué tendencia positiva menciona el texto?",
             "opciones": ["a) Los gobiernos invierten más en digitalización en español.",
                          "b) El inglés está perdiendo su posición dominante.",
                          "c) El contenido generado por usuarios en español comienza a cambiar el equilibrio.",
                          "d) Las plataformas tecnológicas adoptan el español como lengua principal."],
             "respuesta": "c) El contenido generado por usuarios en español comienza a cambiar el equilibrio.",
             "explicacion": "El último párrafo: 'el creciente volumen de contenido generado por usuarios... está comenzando a alterar ese equilibrio'."},
        ],
    },
    {
        "titulo": "La paradoja de la hiperconectividad",
        "fuente": "Texto original · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "La promesa de la tecnología digital era simple: más conexión, más eficiencia, más libertad. "
            "Sin embargo, una década después de la expansión masiva de los smartphones, los datos apuntan "
            "en una dirección incómoda. Lejos de liberarnos, la hiperconectividad parece haber generado "
            "nuevas formas de dependencia que los propios usuarios reconocen pero son incapaces de gestionar.\n\n"
            "El fenómeno tiene una explicación neurológica precisa. Las notificaciones, los 'me gusta' y los "
            "mensajes instantáneos activan el sistema dopaminérgico del cerebro de forma intermitente — "
            "exactamente el patrón que los neurocientíficos identifican como el más adictivo. No es accidental: "
            "los equipos de diseño de las grandes plataformas han estudiado durante años cómo maximizar el "
            "tiempo de pantalla, y los resultados hablan por sí solos. El usuario medio consulta su teléfono "
            "96 veces al día.\n\n"
            "Las consecuencias no se limitan al plano individual. En el entorno laboral, la expectativa de "
            "disponibilidad permanente ha difuminado los límites entre el tiempo de trabajo y el tiempo "
            "personal, generando lo que los psicólogos denominan 'fatiga de conectividad'. Estudios recientes "
            "en varios países europeos muestran que los trabajadores que reciben mensajes laborales fuera del "
            "horario establecido reportan niveles de estrés significativamente más elevados, incluso cuando "
            "deciden no responder.\n\n"
            "Frente a este panorama, han surgido movimientos que abogan por el 'derecho a la desconexión' "
            "como una necesidad regulada por ley. Francia fue pionera en legislar al respecto en 2017, "
            "obligando a las empresas de más de 50 empleados a negociar con sus trabajadores políticas de "
            "desconexión digital. Otros países han seguido su ejemplo, aunque la aplicación efectiva de "
            "estas normas sigue siendo, en muchos casos, más declarativa que real.\n\n"
            "Lo que está en juego no es solo la productividad o el bienestar individual, sino el modo en "
            "que las sociedades contemporáneas definen la frontera entre lo público y lo privado, entre "
            "el tiempo vendido y el tiempo vivido."
        ),
        "preguntas": [
            {
                "pregunta": "Según el texto, ¿qué tiene de particular el patrón de notificaciones de las redes sociales?",
                "opciones": [
                    "a) Que aparecen de forma constante y predecible",
                    "b) Que su carácter intermitente las hace especialmente adictivas",
                    "c) Que han sido diseñadas para reducir el tiempo de pantalla",
                    "d) Que afectan al sistema nervioso solo en usuarios vulnerables"
                ],
                "respuesta": "b) Que su carácter intermitente las hace especialmente adictivas",
                "explicacion": "El texto dice que las notificaciones activan el sistema dopaminérgico 'de forma intermitente' y que ese es 'exactamente el patrón que los neurocientíficos identifican como el más adictivo'."
            },
            {
                "pregunta": "¿Qué se entiende por 'fatiga de conectividad' según el texto?",
                "opciones": [
                    "a) El agotamiento físico producido por el uso prolongado de pantallas",
                    "b) La dificultad para concentrarse después de recibir muchas notificaciones",
                    "c) El estrés generado por la expectativa de estar siempre disponible laboralmente",
                    "d) La sensación de saturación que produce recibir demasiada información"
                ],
                "respuesta": "c) El estrés generado por la expectativa de estar siempre disponible laboralmente",
                "explicacion": "El texto lo define directamente: 'la expectativa de disponibilidad permanente ha difuminado los límites entre trabajo y tiempo personal, generando lo que los psicólogos denominan fatiga de conectividad'."
            },
            {
                "pregunta": "¿Qué crítica hace el texto a las leyes de desconexión digital?",
                "opciones": [
                    "a) Que solo se aplican en países europeos",
                    "b) Que las empresas se niegan a cumplirlas",
                    "c) Que su aplicación real es frecuentemente insuficiente",
                    "d) Que Francia las impuso sin consultar a los trabajadores"
                ],
                "respuesta": "c) Que su aplicación real es frecuentemente insuficiente",
                "explicacion": "El texto dice que 'la aplicación efectiva de estas normas sigue siendo, en muchos casos, más declarativa que real'."
            }
        ]
    },
    {
        "titulo": "El coste invisible del consumo digital",
        "fuente": "Texto original · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "Existe una creencia extendida de que la digitalización de la economía es, por naturaleza, "
            "más sostenible que el modelo industrial tradicional. Enviar un correo electrónico parece "
            "infinitamente menos contaminante que imprimir una carta. Escuchar música en streaming parece "
            "más ecológico que fabricar un disco. Sin embargo, esta intuición, aunque comprensible, ignora "
            "una realidad que los especialistas en sostenibilidad llevan años intentando visibilizar: "
            "la infraestructura digital tiene una huella ecológica enorme y creciente.\n\n"
            "Los centros de datos consumen actualmente entre el 1 y el 1,5% de la electricidad mundial, "
            "una cifra comparable al consumo total de algunos países de tamaño medio. A esto hay que añadir "
            "el impacto de las redes de telecomunicaciones y los propios dispositivos de los usuarios, "
            "cuya fabricación requiere minerales escasos extraídos en condiciones frecuentemente "
            "problemáticas desde el punto de vista medioambiental y social.\n\n"
            "El problema se agrava con la expansión de tecnologías intensivas en consumo energético. "
            "El entrenamiento de un modelo de inteligencia artificial de gran escala puede emitir tanto "
            "dióxido de carbono como cinco automóviles durante toda su vida útil. Las criptomonedas, "
            "por su parte, utilizan mecanismos de validación que requieren una cantidad de energía "
            "comparable a la de países enteros.\n\n"
            "Algunas empresas tecnológicas han respondido con compromisos ambiciosos: alimentar sus "
            "instalaciones con energía renovable al 100%, alcanzar la neutralidad de carbono antes de "
            "2030 o invertir en proyectos de reforestación. Los críticos, sin embargo, señalan que muchos "
            "de estos compromisos se basan en mecanismos de compensación cuya eficacia real es discutida, "
            "y que el crecimiento exponencial del sector neutraliza con frecuencia los avances conseguidos "
            "en eficiencia.\n\n"
            "La sostenibilidad digital no es, por tanto, un problema resuelto ni en vías de resolución "
            "sencilla. Exige repensar no solo cómo producimos energía, sino cuánta energía estamos "
            "dispuestos a consumir y para qué."
        ),
        "preguntas": [
            {
                "pregunta": "¿Cuál es la idea principal que defiende el texto?",
                "opciones": [
                    "a) Que la digitalización es más contaminante que la industria tradicional",
                    "b) Que la percepción de que lo digital es sostenible no se corresponde con la realidad",
                    "c) Que los centros de datos son el principal problema medioambiental del siglo XXI",
                    "d) Que las empresas tecnológicas mienten sobre sus compromisos ecológicos"
                ],
                "respuesta": "b) Que la percepción de que lo digital es sostenible no se corresponde con la realidad",
                "explicacion": "El texto no afirma que lo digital sea más contaminante (a), ni que los centros de datos sean el principal problema (c), ni acusa a las empresas de mentir (d)."
            },
            {
                "pregunta": "¿Qué crítica se hace a los compromisos medioambientales de las empresas tecnológicas?",
                "opciones": [
                    "a) Que son insuficientes porque no incluyen la fabricación de dispositivos",
                    "b) Que el crecimiento del sector puede anular las mejoras conseguidas",
                    "c) Que están diseñados para mejorar la imagen pública sin coste real",
                    "d) Que solo se aplican en países con legislación más estricta"
                ],
                "respuesta": "b) Que el crecimiento del sector puede anular las mejoras conseguidas",
                "explicacion": "El texto dice que 'el crecimiento exponencial del sector neutraliza con frecuencia los avances conseguidos en eficiencia'."
            },
            {
                "pregunta": "¿Qué conclusión extrae el texto sobre la sostenibilidad digital?",
                "opciones": [
                    "a) Que depende principalmente de la transición a energías renovables",
                    "b) Que es un problema que las empresas pueden resolver sin intervención política",
                    "c) Que requiere cuestionar tanto la producción como el consumo de energía",
                    "d) Que los avances técnicos la harán posible a medio plazo"
                ],
                "respuesta": "c) Que requiere cuestionar tanto la producción como el consumo de energía",
                "explicacion": "La última frase es explícita: 'exige repensar no solo cómo producimos energía, sino cuánta energía estamos dispuestos a consumir'."
            }
        ]
    },
    {
        "titulo": "El trabajo del futuro y la trampa de la adaptabilidad",
        "fuente": "Texto original · Nivel C1",
        "formato": "seleccion_multiple",
        "texto": (
            "Durante los últimos años, el discurso dominante sobre el futuro del trabajo ha girado en "
            "torno a un concepto: la adaptabilidad. Ante la automatización creciente y la transformación "
            "digital de la economía, se ha impuesto la idea de que los trabajadores deben reinventarse "
            "continuamente, adquirir nuevas competencias y abrazar el cambio como una constante. "
            "Lo que rara vez se cuestiona es quién asume el coste de esa adaptación.\n\n"
            "En los modelos económicos tradicionales, la formación continua era una responsabilidad "
            "compartida entre el Estado, las empresas y los trabajadores. Las grandes corporaciones "
            "invertían en la cualificación de sus empleados porque los concebían como activos a largo "
            "plazo. Este modelo ha erosionado significativamente en las últimas décadas. La proliferación "
            "de contratos temporales, el auge de la economía de plataformas y la externalización de "
            "servicios han trasladado el riesgo —y el coste de la formación— casi exclusivamente "
            "al individuo.\n\n"
            "El resultado es una paradoja: se exige más adaptabilidad precisamente a quienes tienen "
            "menos recursos para adaptarse. Los trabajadores con empleos precarios, que son los más "
            "expuestos a la automatización, son también los que menos tiempo, dinero y acceso a "
            "formación de calidad tienen. La brecha no es solo económica; es también una brecha "
            "de capacidad de respuesta ante el cambio.\n\n"
            "Frente a esta situación, algunos economistas proponen modelos alternativos como la "
            "flexiseguridad, que combinan mercados laborales más dinámicos con redes de protección "
            "social robustas. Dinamarca se cita habitualmente como ejemplo de este enfoque, aunque "
            "los intentos de trasplantar su modelo a otros contextos han topado con resistencias "
            "estructurales y culturales considerables.\n\n"
            "El debate de fondo no es tecnológico sino político: quién decide qué tipo de trabajo "
            "merece protección, quién paga por la transición y quién se queda atrás si la transición falla."
        ),
        "preguntas": [
            {
                "pregunta": "Según el texto, ¿qué ha cambiado respecto a la formación de los trabajadores?",
                "opciones": [
                    "a) Que las empresas invierten más en formación que antes",
                    "b) Que el Estado ha asumido un papel más activo en la formación continua",
                    "c) Que la responsabilidad de formarse recae ahora principalmente en el trabajador",
                    "d) Que la formación continua ya no es necesaria gracias a la automatización"
                ],
                "respuesta": "c) Que la responsabilidad de formarse recae ahora principalmente en el trabajador",
                "explicacion": "El texto dice que el coste de la formación se ha trasladado 'casi exclusivamente al individuo'."
            },
            {
                "pregunta": "¿En qué consiste la paradoja que describe el texto?",
                "opciones": [
                    "a) En que la tecnología crea más empleos de los que destruye",
                    "b) En que se pide más capacidad de cambio a quienes menos pueden cambiar",
                    "c) En que los trabajadores cualificados son los más afectados por la automatización",
                    "d) En que las empresas forman a sus empleados para que luego se vayan"
                ],
                "respuesta": "b) En que se pide más capacidad de cambio a quienes menos pueden cambiar",
                "explicacion": "El texto lo formula así: 'se exige más adaptabilidad precisamente a quienes tienen menos recursos para adaptarse'."
            },
            {
                "pregunta": "¿Cómo presenta el texto el modelo danés de flexiseguridad?",
                "opciones": [
                    "a) Como la solución definitiva al problema del trabajo precario",
                    "b) Como un modelo exportable a cualquier país desarrollado",
                    "c) Como un ejemplo útil pero difícil de replicar en otros contextos",
                    "d) Como un sistema que ha fracasado fuera de Dinamarca"
                ],
                "respuesta": "c) Como un ejemplo útil pero difícil de replicar en otros contextos",
                "explicacion": "El texto dice que 'los intentos de trasplantar su modelo a otros contextos han topado con resistencias estructurales y culturales considerables'."
            }
        ]
    },
    # ── VERDADERO / FALSO ─────────────────────────────────────────
    {
        "titulo": "La memoria no es un archivo",
        "fuente": "Texto original · Nivel C1",
        "formato": "verdadero_falso",
        "texto": (
            "Durante décadas, la metáfora dominante para explicar el funcionamiento de la memoria humana "
            "fue la del archivo o la grabación: el cerebro registraría los eventos, los almacenaría y, "
            "cuando fuera necesario, los reproduciría con fidelidad. Esta imagen, intuitiva y reconfortante, "
            "ha resultado ser fundamentalmente errónea.\n\n"
            "La neurociencia cognitiva ha demostrado que la memoria es un proceso reconstructivo, no "
            "reproductivo. Cada vez que recordamos algo, no recuperamos un fichero intacto: reactivamos "
            "fragmentos dispersos de información que el cerebro ensambla en tiempo real, rellenando las "
            "lagunas con inferencias, expectativas y conocimientos previos. Como consecuencia, el acto "
            "mismo de recordar puede alterar el recuerdo: cada evocación lo modifica ligeramente.\n\n"
            "Este mecanismo tiene implicaciones prácticas relevantes. Los testimonios oculares, durante "
            "mucho tiempo considerados pruebas sólidas en procesos judiciales, han sido revisados a la "
            "luz de estos hallazgos. Estudios sistemáticos muestran que testigos honestos y seguros de "
            "sí mismos pueden relatar versiones inexactas o incluso contradictorias de un mismo evento.\n\n"
            "La memoria emocional merece mención aparte. Los recuerdos ligados a experiencias de alta "
            "carga emocional suelen ser más vívidos y persistentes. Sin embargo, viveza e intensidad no "
            "equivalen a exactitud: la emoción hace que el recuerdo sea más difícil de olvidar, pero no "
            "garantiza que sea más fiel a lo ocurrido.\n\n"
            "Comprender la naturaleza reconstructiva de la memoria no implica que esta sea inútil o "
            "poco fiable en términos generales. Significa, más bien, que debemos tratarla como lo que "
            "es: una herramienta adaptativa, flexible y orientada al futuro, no un espejo fiel del pasado."
        ),
        "preguntas": [
            {
                "afirmacion": "La neurociencia ha confirmado que la memoria funciona como una grabación fiel de los eventos.",
                "respuesta": "Falso",
                "explicacion": "El texto afirma lo contrario: 'la memoria es un proceso reconstructivo, no reproductivo' y califica la metáfora del archivo de 'fundamentalmente errónea'."
            },
            {
                "afirmacion": "El acto de recordar algo puede modificar el propio recuerdo.",
                "respuesta": "Verdadero",
                "explicacion": "El texto lo dice explícitamente: 'el acto mismo de recordar puede alterar el recuerdo: cada evocación lo modifica ligeramente'."
            },
            {
                "afirmacion": "Según el texto, los recuerdos emocionalmente intensos son más precisos que los neutros.",
                "respuesta": "Falso",
                "explicacion": "El texto aclara que 'viveza e intensidad no equivalen a exactitud': la emoción hace el recuerdo más persistente, pero no más fiel a lo ocurrido."
            },
            {
                "afirmacion": "El texto concluye que la memoria es una herramienta poco fiable que no debería tomarse como referencia.",
                "respuesta": "Falso",
                "explicacion": "El texto matiza: comprender su naturaleza reconstructiva 'no implica que sea inútil o poco fiable en términos generales', sino que debe tratarse como 'una herramienta adaptativa'."
            },
        ]
    },
    {
        "titulo": "La soledad en las ciudades",
        "fuente": "Texto original · Nivel C1",
        "formato": "verdadero_falso",
        "texto": (
            "La ciudad moderna fue concebida, entre otras cosas, como espacio de encuentro: mercados, "
            "plazas, cafés, transportes colectivos. Sin embargo, los datos de las últimas encuestas "
            "sociológicas dibujan un panorama paradójico: cuanto más densa es la ciudad, mayor puede "
            "ser la sensación de aislamiento de sus habitantes.\n\n"
            "Este fenómeno, que los investigadores denominan 'soledad urbana', no debe confundirse con "
            "el aislamiento físico. Una persona puede estar rodeada de miles de personas y sentirse "
            "profundamente sola. Lo que define la soledad, en este contexto, no es la ausencia de "
            "presencias, sino la ausencia de vínculos significativos.\n\n"
            "Contra la intuición popular, los estudios muestran que los jóvenes adultos —entre 18 y "
            "35 años— son el grupo demográfico que reporta mayores niveles de soledad en entornos "
            "urbanos, por encima de los mayores de 65 años. La hiperconectividad digital puede "
            "contribuir a esta paradoja: muchas interacciones en redes sociales generan la ilusión "
            "de compañía sin satisfacer la necesidad de conexión real.\n\n"
            "El diseño urbano no es ajeno a este problema. Ciudades que priorizan el espacio privado "
            "sobre el público, con pocas zonas de encuentro espontáneo, producen entornos que "
            "dificultan la formación de lazos comunitarios. Algunas administraciones han comenzado "
            "a incorporar criterios de 'diseño para la cohesión social' en sus planes urbanísticos, "
            "con resultados prometedores aunque todavía limitados.\n\n"
            "Lo que está claro es que la soledad urbana no es un problema individual sino estructural, "
            "y que abordarlo requiere tanto políticas públicas como una relectura de lo que significa "
            "habitar juntos un mismo espacio."
        ),
        "preguntas": [
            {
                "afirmacion": "El texto define la soledad urbana como la ausencia física de otras personas.",
                "respuesta": "Falso",
                "explicacion": "El texto distingue expresamente ambos conceptos: 'lo que define la soledad no es la ausencia de presencias, sino la ausencia de vínculos significativos'."
            },
            {
                "afirmacion": "Los jóvenes adultos reportan niveles más altos de soledad urbana que las personas mayores de 65 años.",
                "respuesta": "Verdadero",
                "explicacion": "El texto lo afirma directamente: 'los jóvenes adultos —entre 18 y 35 años— son el grupo que reporta mayores niveles de soledad en entornos urbanos, por encima de los mayores de 65 años'."
            },
            {
                "afirmacion": "Según el texto, las redes sociales resuelven eficazmente la necesidad de conexión de los jóvenes.",
                "respuesta": "Falso",
                "explicacion": "El texto afirma lo contrario: las interacciones digitales 'generan la ilusión de compañía sin satisfacer la necesidad de conexión real'."
            },
            {
                "afirmacion": "El texto considera la soledad urbana un problema de naturaleza estructural, no solo individual.",
                "respuesta": "Verdadero",
                "explicacion": "La conclusión es explícita: 'la soledad urbana no es un problema individual sino estructural, y abordarlo requiere políticas públicas'."
            },
        ]
    },
    {
        "titulo": "El sesgo de confirmación",
        "fuente": "Texto original · Nivel C1",
        "formato": "verdadero_falso",
        "texto": (
            "Entre los numerosos sesgos cognitivos que los psicólogos han catalogado en las últimas "
            "décadas, el sesgo de confirmación ocupa un lugar central. Su mecanismo es sencillo: "
            "tendemos a buscar, interpretar y recordar la información de manera que confirme lo que "
            "ya creemos, ignorando o minimizando los datos que contradicen nuestras convicciones.\n\n"
            "Este sesgo no discrimina por nivel educativo ni inteligencia. Personas con alta formación "
            "académica y profesionales expertos lo manifiestan con la misma frecuencia que el resto "
            "de la población. De hecho, algunos estudios sugieren que una mayor capacidad intelectual "
            "puede hacer que el sesgo sea más sofisticado: los argumentos para defender la posición "
            "previa son más elaborados, no más objetivos.\n\n"
            "El entorno digital ha potenciado sus efectos. Los algoritmos de las plataformas de "
            "contenido aprenden rápidamente las preferencias del usuario y le ofrecen información "
            "coherente con sus puntos de vista, creando las llamadas 'burbujas de filtro'. El "
            "resultado es que muchos usuarios consumen exclusivamente contenidos que refuerzan "
            "sus creencias existentes, sin exposición significativa a perspectivas alternativas.\n\n"
            "¿Puede contrarrestarse? La respuesta es matizada. Ser consciente del sesgo reduce su "
            "influencia, pero no la elimina. El método científico ha sido diseñado, en parte, "
            "precisamente para combatirlo: la obligación de buscar activamente evidencias que "
            "puedan falsificar una hipótesis es el contrapeso institucionalizado al sesgo de "
            "confirmación natural del pensamiento humano.\n\n"
            "En un contexto de polarización creciente, entender este mecanismo no es un ejercicio "
            "académico: es una herramienta necesaria para cualquier forma de pensamiento crítico."
        ),
        "preguntas": [
            {
                "afirmacion": "Según el texto, el sesgo de confirmación afecta más a personas con menor nivel educativo.",
                "respuesta": "Falso",
                "explicacion": "El texto afirma lo contrario: 'no discrimina por nivel educativo ni inteligencia' y añade que una mayor capacidad intelectual puede hacerlo 'más sofisticado'."
            },
            {
                "afirmacion": "Los algoritmos de las plataformas digitales pueden reforzar el sesgo de confirmación.",
                "respuesta": "Verdadero",
                "explicacion": "El texto lo explica: los algoritmos 'ofrecen información coherente con los puntos de vista del usuario', creando 'burbujas de filtro' que refuerzan creencias existentes."
            },
            {
                "afirmacion": "El texto afirma que ser consciente del sesgo de confirmación lo elimina completamente.",
                "respuesta": "Falso",
                "explicacion": "El texto es explícito: 'ser consciente del sesgo reduce su influencia, pero no la elimina'."
            },
            {
                "afirmacion": "El método científico incorpora mecanismos para contrarrestar el sesgo de confirmación.",
                "respuesta": "Verdadero",
                "explicacion": "El texto lo afirma: 'la obligación de buscar activamente evidencias que puedan falsificar una hipótesis es el contrapeso institucionalizado al sesgo de confirmación'."
            },
        ]
    },
    # ── EMPAREJAMIENTO ────────────────────────────────────────────
    {
        "titulo": "La economía circular",
        "fuente": "Texto original · Nivel C1",
        "formato": "emparejamiento",
        "texto": (
            "El modelo económico predominante desde la revolución industrial puede describirse como "
            "'lineal': se extraen recursos naturales, se fabrican productos, se usan y se desechan. "
            "Este modelo, eficiente a corto plazo, genera una presión insostenible sobre los recursos "
            "del planeta y produce cantidades crecientes de residuos.\n\n"
            "La economía circular propone un enfoque radicalmente distinto: diseñar productos y "
            "sistemas de forma que los materiales permanezcan en uso el mayor tiempo posible y, "
            "al final de su vida útil, puedan reintegrarse en el ciclo productivo como nuevos "
            "recursos. El residuo de un proceso se convierte, idealmente, en el insumo del siguiente.\n\n"
            "Uno de los obstáculos más señalados es la obsolescencia programada: la práctica de "
            "diseñar productos con una vida útil artificialmente corta para estimular la compra "
            "recurrente. Este modelo, rentable para los fabricantes a corto plazo, es "
            "incompatible con los principios de la circularidad.\n\n"
            "El ecodiseño es una de las respuestas: incorporar criterios medioambientales desde "
            "la fase de concepción del producto, facilitando su reparación, reutilización y "
            "reciclaje. Otro concepto clave es la simbiosis industrial: acuerdos entre empresas "
            "de distintos sectores por los que los residuos o subproductos de una se convierten "
            "en materia prima de otra.\n\n"
            "La transición hacia la circularidad no es solo tecnológica. Implica cambios en los "
            "modelos de negocio, en los hábitos de consumo y en los marcos regulatorios, y exige "
            "una coordinación que va más allá de la voluntad individual de empresas o consumidores."
        ),
        "instruccion": "Relaciona cada concepto con su descripción según el texto.",
        "pares": [
            {
                "termino": "Economía lineal",
                "definicion": "Modelo basado en extraer, fabricar, usar y desechar sin recuperar los materiales."
            },
            {
                "termino": "Economía circular",
                "definicion": "Sistema en el que los materiales permanecen en uso el mayor tiempo posible y se reintegran al ciclo productivo al final de su vida útil."
            },
            {
                "termino": "Obsolescencia programada",
                "definicion": "Práctica de diseñar productos con vida útil reducida intencionalmente para fomentar nuevas compras."
            },
            {
                "termino": "Ecodiseño",
                "definicion": "Incorporación de criterios medioambientales en la concepción del producto para facilitar su reparación, reutilización y reciclaje."
            },
            {
                "termino": "Simbiosis industrial",
                "definicion": "Acuerdos entre empresas por los que los residuos de una se convierten en materia prima de otra."
            },
        ]
    },
    {
        "titulo": "Mecanismos del lenguaje persuasivo",
        "fuente": "Texto original · Nivel C1",
        "formato": "emparejamiento",
        "texto": (
            "El lenguaje no es nunca neutro. Incluso cuando se aspira a la objetividad, las elecciones "
            "léxicas, la estructura de las frases y los recursos retóricos utilizados construyen una "
            "perspectiva sobre la realidad. Conocer los mecanismos del lenguaje persuasivo no es solo "
            "una habilidad de escritor: es una herramienta de lectura crítica indispensable.\n\n"
            "La eufemización consiste en sustituir una expresión con connotaciones negativas por "
            "otra más suave o neutra. Los eufemismos sirven para atenuar realidades incómodas: "
            "un 'ajuste de plantilla' describe lo mismo que un 'despido masivo', pero activa "
            "respuestas emocionales muy distintas en quien lo escucha.\n\n"
            "El encuadre —o framing— se refiere a la forma en que se presenta la información: "
            "los mismos datos pueden generar percepciones opuestas según cómo se enmarquen. "
            "Decir que 'un tratamiento tiene un 90% de supervivencia' activa reacciones distintas "
            "a decir que 'tiene un 10% de mortalidad', aunque ambas frases sean equivalentes.\n\n"
            "La apelación a la autoridad es el recurso de citar a una fuente reconocida para "
            "reforzar un argumento, independientemente de si esa autoridad es relevante en "
            "el contexto específico del debate. Su contrapunto es el ad hominem: atacar la "
            "credibilidad personal del interlocutor en lugar de refutar sus argumentos.\n\n"
            "Finalmente, la falacia del hombre de paja consiste en distorsionar o simplificar "
            "la posición del adversario para hacer más fácil su refutación, atacando una versión "
            "caricaturizada en lugar del argumento real."
        ),
        "instruccion": "Relaciona cada recurso retórico con su descripción según el texto.",
        "pares": [
            {
                "termino": "Eufemización",
                "definicion": "Sustitución de una expresión de connotaciones negativas por otra más suave para atenuar realidades incómodas."
            },
            {
                "termino": "Encuadre (framing)",
                "definicion": "Presentación de la misma información de formas distintas para generar percepciones diferentes en el receptor."
            },
            {
                "termino": "Apelación a la autoridad",
                "definicion": "Uso de una fuente reconocida para reforzar un argumento, independientemente de su relevancia en el contexto."
            },
            {
                "termino": "Ad hominem",
                "definicion": "Ataque a la credibilidad personal del interlocutor en lugar de refutar sus argumentos."
            },
            {
                "termino": "Falacia del hombre de paja",
                "definicion": "Distorsión o simplificación de la posición del adversario para facilitar su refutación atacando una versión caricaturizada."
            },
        ]
    },
    {
        "titulo": "La inteligencia emocional en el entorno profesional",
        "fuente": "Texto original · Nivel C1",
        "formato": "emparejamiento",
        "texto": (
            "Desde que Daniel Goleman popularizó el concepto en los años noventa, la inteligencia "
            "emocional ha pasado de ser un término psicológico de nicho a convertirse en uno de "
            "los criterios más valorados en los procesos de selección de personal. Sin embargo, "
            "el concepto abarca componentes bien diferenciados que conviene distinguir.\n\n"
            "La autoconciencia es la capacidad de reconocer y comprender las propias emociones "
            "en el momento en que se producen, así como su efecto sobre el comportamiento y "
            "las decisiones. Es la base sobre la que se construyen las demás competencias "
            "emocionales: difícilmente puede gestionarse lo que no se reconoce.\n\n"
            "La autorregulación se refiere a la capacidad de controlar los impulsos y emociones "
            "perturbadoras de manera que no interfieran negativamente con la conducta. "
            "No implica suprimir las emociones, sino canalizarlas de forma constructiva.\n\n"
            "La empatía —frecuentemente confundida con la simpatía— es la capacidad de percibir "
            "y comprender las emociones ajenas adoptando la perspectiva del otro sin necesidad "
            "de compartir sus sentimientos. En entornos de trabajo, facilita la comunicación, "
            "la resolución de conflictos y el liderazgo efectivo.\n\n"
            "Las habilidades sociales designan la capacidad de gestionar relaciones e influir "
            "en los demás de forma positiva: comunicar con claridad, negociar, colaborar y "
            "construir redes de confianza. Son el componente más visible de la inteligencia "
            "emocional, aunque dependen de los anteriores para ser genuinas.\n\n"
            "Por último, la motivación intrínseca describe el impulso que lleva a las personas "
            "a perseguir metas por razones internas —satisfacción, propósito, crecimiento— más "
            "allá de recompensas externas como el salario o el reconocimiento."
        ),
        "instruccion": "Relaciona cada componente de la inteligencia emocional con su descripción según el texto.",
        "pares": [
            {
                "termino": "Autoconciencia",
                "definicion": "Capacidad de reconocer y comprender las propias emociones y su efecto sobre el comportamiento y las decisiones."
            },
            {
                "termino": "Autorregulación",
                "definicion": "Capacidad de controlar impulsos y emociones perturbadoras canalizándolas de forma constructiva sin suprimirlas."
            },
            {
                "termino": "Empatía",
                "definicion": "Capacidad de percibir y comprender las emociones ajenas adoptando la perspectiva del otro sin necesidad de compartir sus sentimientos."
            },
            {
                "termino": "Habilidades sociales",
                "definicion": "Capacidad de gestionar relaciones e influir positivamente en los demás mediante la comunicación, la negociación y la colaboración."
            },
            {
                "termino": "Motivación intrínseca",
                "definicion": "Impulso a perseguir metas por razones internas como la satisfacción o el propósito, más allá de recompensas externas."
            },
        ]
    },
]
