import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json
import numpy as np
from utils.session_utils import save_chat_history, get_chat_history

# Load the model and data
with open('train.json', 'r') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
answers = [item['answer'] for item in data]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)
model = LogisticRegression()
model.fit(X, answers)

def qa_page():
    st.title("Q&A Model")

    # Display chat history
    chat_history = get_chat_history()
    st.write("**Chat History:**")
    for q, a in chat_history:
        st.write(f"**Q:** {q}")
        st.write(f"**A:** {a}")

    # Create a container to keep the question input field fixed at the bottom
    with st.container():
        st.write("### Ask a question:")
        question = st.text_input("Type your question here:")
        if st.button("Submit"):
            if question:
                X_question = vectorizer.transform([question])
                answer = model.predict(X_question)[0]
                st.write(f"**A:** {answer}")

                # Save the chat history
                save_chat_history(question, answer)
            else:
                st.error("Please enter a question.")
