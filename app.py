import streamlit as st
from modules.lesson_generator import generate_lesson

st.set_page_config(page_title="LearnLite – AI-Powered Microlearning", page_icon="📚")

st.title("📚 LearnLite – AI-Powered Microlearning")

# Input fields
topic = st.text_input("Enter a topic you'd like to learn about:")
level = st.selectbox("Choose your level:", ["Beginner", "Intermediate", "Advanced"])
style = st.selectbox("Preferred learning style:", ["Summary", "Analogy", "Q&A", "Visual (coming soon)"])

# Button to generate lesson
if st.button("Generate Lesson"):
    if not topic:
        st.warning("Please enter a topic to get started.")
    else:
        with st.spinner("Generating your lesson..."):
            lesson = generate_lesson(topic, level, style)
            st.markdown(lesson, unsafe_allow_html=True)
