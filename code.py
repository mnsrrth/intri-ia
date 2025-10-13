import streamlit as st
import pandas as pd

# -------------------------------
# DATOS DEL CUESTIONARIO
# -------------------------------
QUIZ_DATA = [
    {
        "pregunta": "¿Cuál suele ser una reacción emocional común entre los familiares tras un suicidio?",
        "opciones": ["Alegría y alivio", "Culpa y confusión", "Indiferencia"],
        "respuesta_correcta": "Culpa y confusión",
        "justificacion": "Los familiares suelen experimentar sentimientos intensos de culpa y confusión al intentar comprender las razones del suicidio y su posible papel en el hecho."
    },
    {
        "pregunta": "En el contexto latinoamericano, ¿qué factor sociocultural puede aumentar el estigma hacia las familias afectadas por un suicidio?",
        "opciones": ["Las creencias religiosas tradicionales", "La apertura al diálogo sobre salud mental", "La educación emocional en las escuelas"],
        "respuesta_correcta": "Las creencias religiosas tradicionales",
        "justificacion": "En muchas comunidades latinoamericanas, las creencias religiosas pueden considerar el suicidio como un pecado, generando culpa y rechazo social hacia la familia."
    },
    {
        "pregunta": "¿Qué impacto puede tener el suicidio de un familiar en la dinámica familiar?",
        "opciones": ["Fortalece automáticamente la unión familiar", "Puede generar conflictos, distanciamiento o silencios prolongados", "No altera la dinámica familiar"],
        "respuesta_correcta": "Puede generar conflictos, distanciamiento o silencios prolongados",
        "justificacion": "La falta de comunicación y el duelo no elaborado pueden afectar la cohesión familiar y aumentar los conflictos o el aislamiento."
    },
    {
        "pregunta": "¿Cuál es una consecuencia frecuente en los hijos o hermanos de la persona fallecida por suicidio?",
        "opciones": ["Desinterés temporal por el estudio o trabajo", "Mejora automática en su desempeño escolar", "Incremento en su vida social"],
        "respuesta_correcta": "Desinterés temporal por el estudio o trabajo",
        "justificacion": "El duelo puede provocar dificultades en la concentración, apatía y desmotivación en actividades cotidianas."
    },
    {
        "pregunta": "¿Qué rol cumple el apoyo comunitario o social en las familias en duelo por suicidio?",
        "opciones": ["No tiene relevancia significativa", "Ayuda a disminuir el aislamiento y el estigma", "Sustituye completamente la ayuda profesional"],
        "respuesta_correcta": "Ayuda a disminuir el aislamiento y el estigma",
        "justificacion": "El acompañamiento de la comunidad permite que las familias sientan apoyo y comprensión, reduciendo el sentimiento de exclusión."
    },
    {
        "pregunta": "¿Por qué es importante brindar atención psicológica a la familia sobreviviente?",
        "opciones": ["Porque el duelo por suicidio suele ser más complejo y prolongado", "Porque es una formalidad social", "Porque garantiza que no vuelvan a sufrir pérdidas"],
        "respuesta_correcta": "Porque el duelo por suicidio suele ser más complejo y prolongado",
        "justificacion": "El suicidio genera un tipo de duelo llamado ‘duelo complicado’, con emociones intensas que requieren acompañamiento profesional."
    },
    {
        "pregunta": "¿Qué papel juega el silencio en muchas familias latinoamericanas tras un suicidio?",
        "opciones": ["Favorece la aceptación del duelo", "Evita la comunicación y dificulta la elaboración emocional", "Mejora las relaciones familiares"],
        "respuesta_correcta": "Evita la comunicación y dificulta la elaboración emocional",
        "justificacion": "El silencio y la negación impiden expresar el dolor y pueden cronificar el sufrimiento emocional."
    },
    {
        "pregunta": "¿Cuál de las siguientes acciones puede ayudar a una familia a afrontar la pérdida por suicidio?",
        "opciones": ["Evitar hablar del tema completamente", "Buscar grupos de apoyo y acompañamiento psicológico", "Reprimir las emociones dolorosas"],
        "respuesta_correcta": "Buscar grupos de apoyo y acompañamiento psicológico",
        "justificacion": "Compartir la experiencia con otros y recibir orientación terapéutica ayuda a procesar el duelo de manera más saludable."
    },
    {
        "pregunta": "En el contexto latinoamericano, ¿qué barrera común enfrentan las familias para buscar ayuda psicológica?",
        "opciones": ["La falta de empatía de los profesionales", "El estigma y la falta de información sobre salud mental", "El exceso de recursos disponibles"],
        "respuesta_correcta": "El estigma y la falta de información sobre salud mental",
        "justificacion": "Persisten prejuicios culturales que asocian la atención psicológica con ‘locura’ o debilidad, lo que dificulta pedir ayuda."
    },
    {
        "pregunta": "¿Qué efecto puede tener la intervención psicosocial en familias que han vivido un suicidio?",
        "opciones": ["Promueve la resiliencia y la reconstrucción del sentido de vida", "Aumenta la culpa familiar", "Genera dependencia emocional del terapeuta"],
        "respuesta_correcta": "Promueve la resiliencia y la reconstrucción del sentido de vida",
        "justificacion": "Las intervenciones psicosociales facilitan la expresión emocional, la resignificación de la pérdida y el fortalecimiento de recursos personales y familiares."
    }
]

# -------------------------------
# CONFIGURACIÓN DE LA APP
# -------------------------------
st.set_page_config(page_title="Cuestionario: Impacto del Suicidio en Familias Latinoamericanas", page_icon="🧠", layout="centered")

st.title("🧠 Cuestionario: Impacto del Suicidio en Familias Latinoamericanas")
st.write("Responde las siguientes preguntas. Recibirás retroalimentación inmediata y al final verás tu puntaje total.")

# Inicializar estado
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntaje = 0
    st.session_state.finalizado = False

# Mostrar pregunta actual
if not st.session_state.finalizado:
    pregunta_actual = QUIZ_DATA[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1} de {len(QUIZ_DATA)}")
    st.write(pregunta_actual["pregunta"])

    opcion = st.radio("Selecciona una respuesta:", pregunta_actual["opciones"], key=f"pregunta_{st.session_state.indice}")

    if st.button("Responder"):
        if opcion == pregunta_actual["respuesta_correcta"]:
            st.success("✅ ¡Correcto!")
            st.session_state.puntaje += 1
        else:
            st.error(f"❌ Incorrecto. La respuesta correcta es: **{pregunta_actual['respuesta_correcta']}**")

        st.info(f"💡 Justificación: {pregunta_actual['justificacion']}")

        if st.session_state.indice + 1 < len(QUIZ_DATA):
            if st.button("➡️ Siguiente pregunta"):
                st.session_state.indice += 1
                st.rerun()
        else:
            if st.button("🏁 Ver resultados finales"):
                st.session_state.finalizado = True
                st.rerun()

# Mostrar resultado final
if st.session_state.finalizado:
    total = len(QUIZ_DATA)
    puntaje = st.session_state.puntaje
    st.success(f"🎉 Has completado el cuestionario. Tu puntaje final es {puntaje} de {total}.")

    porcentaje = (puntaje / total) * 100
    if porcentaje == 100:
        st.balloons()
        st.write("🌟 Excelente dominio del tema. Has respondido todo correctamente.")
    elif porcentaje >= 70:
        st.write("👍 Buen trabajo, tienes un conocimiento sólido sobre el tema.")
    else:
        st.write("📘 Te recomiendo repasar algunos conceptos sobre el impacto del suicidio en las familias.")

    if st.button("🔄 Reiniciar cuestionario"):
        st.session_state.indice = 0
        st.session_state.puntaje = 0
        st.session_state.finalizado = False
        st.rerun()
