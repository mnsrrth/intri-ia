# app.py (o code.py)
import streamlit as st
# Importa los datos del cuestionario que definimos en el otro archivo
from quiz_data import QUIZ_DATA 

# ----------------------------------------------------
# 1. Configuración inicial y manejo de estado
# ----------------------------------------------------

st.set_page_config(layout="wide")
st.title("🧠 Quiz Interactivo: Impacto del Suicidio en Familias Latinoamericanas")
st.markdown("---")

# Inicializar variables de estado de la sesión si no existen
# 'current_question': índice de la pregunta actual (0 a 9)
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
# 'score': puntuación total
if 'score' not in st.session_state:
    st.session_state.score = 0
# 'feedback': mensaje de retroalimentación
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""

# ----------------------------------------------------
# 2. Funciones de Navegación y Lógica
# ----------------------------------------------------

def check_answer(user_selection):
    """Verifica la respuesta y actualiza el estado y el feedback."""
    
    current_index = st.session_state.current_question
    current_item = QUIZ_DATA[current_index]
    
    # Prepara el mensaje de retroalimentación
    if user_selection is None:
        st.session_state.feedback = "⚠️ Por favor, selecciona una opción para continuar."
        return

    # Si la respuesta es correcta
    if user_selection == current_item["respuesta_correcta"]:
        st.session_state.score += 1
        st.session_state.feedback = (
            f"✅ **¡Respuesta Correcta!** Muy bien. \n\n"
            f"**Justificación:** {current_item['justificacion']}"
        )
        
        # Avanza a la siguiente pregunta después de la retroalimentación
        st.session_state.current_question += 1
        
    # Si la respuesta es incorrecta
    else:
        st.session_state.feedback = (
            f"❌ **Respuesta Incorrecta.** Tu respuesta fue: {user_selection}. \n\n"
            f"**Respuesta Correcta:** {current_item['respuesta_correcta']} \n\n"
            f"**Justificación:** {current_item['justificacion']}"
        )
        
        # Avanza a la siguiente pregunta después de la retroalimentación
        st.session_state.current_question += 1

# ----------------------------------------------------
# 3. Renderizado del Dashboard
# ----------------------------------------------------

total_questions = len(QUIZ_DATA)

# 3.1. Mostrar el resultado final
if st.session_state.current_question >= total_questions:
    st.header("¡Cuestionario Terminado!")
    final_score = st.session_state.score
    
    st.metric(
        label="Puntuación Final", 
        value=f"{final_score} / {total_questions}", 
        delta=f"{(final_score/total_questions)*100:.0f}% de aciertos"
    )
    
    if final_score == total_questions:
        st.balloons()
        st.success("¡Perfecto! Demuestras un dominio excepcional del tema.")
    elif final_score >= total_questions * 0.7:
        st.info("Buen trabajo. Tienes un sólido conocimiento del impacto psicosocial.")
    else:
        st.warning("Puedes repasar algunos conceptos. ¡Sigue estudiando!")

    # Botón para reiniciar el quiz
    if st.button("Reiniciar Cuestionario"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.feedback = ""
        st.experimental_rerun()

# 3.2. Mostrar la pregunta actual
else:
    current_index = st.session_state.current_question
    item = QUIZ_DATA[current_index]

    st.subheader(f"Pregunta {current_index + 1} de {total_questions}")
    st.markdown(f"#### {item['pregunta']}")
    
    # Contenedor para la radio box y el botón
    with st.container(border=True):
        
        # El radio selecciona la opción del usuario
        selected_option = st.radio(
            label="Selecciona la respuesta correcta:",
            options=item['opciones'],
            key=f"q_{current_index}_radio",
            index=None,
            label_visibility="collapsed"
        )
        
        # Botón para verificar la respuesta
        # Usa el callback de la función check_answer
        st.button(
            "Responder y Siguiente",
            on_click=check_answer,
            args=(selected_option,), # Pasa la selección a la función
            type="primary"
        )

    # 3.3. Mostrar el feedback
    if st.session_state.feedback:
        st.markdown("---")
        st.markdown(st.session_state.feedback)
        
# ----------------------------------------------------
# FIN
# ----------------------------------------------------
