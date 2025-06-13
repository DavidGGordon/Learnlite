import streamlit as st
from modules.lesson_generator import generate_lesson

st.title("📚 LearnLite – AI-Powered Microlearning")

topic = st.text_input("Enter a topic you'd like to learn about:")
level = st.selectbox("Choose your level:", ["Beginner", "Intermediate", "Advanced"])
style = st.selectbox("Preferred learning style:", ["Summary", "Analogy", "Q&A", "Visual (coming soon)"])

if st.button("Generate Lesson"):
    with st.spinner("Generating your lesson..."):
        lesson = generate_lesson(topic, level, style)
        st.markdown(lesson, unsafe_allow_html=True)
