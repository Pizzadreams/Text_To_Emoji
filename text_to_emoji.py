import streamlit as st
from transformers import pipeline

# Load text generation pipeline (e.g., GPT-2 or similar)
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

st.title("Text to Emoji Translator (No Mapping)")

with st.form("emoji_form"):
    user_text = st.text_input("Enter a sentence (e.g., 'Red bull gives you wings')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        prompt = f"Translate this sentence to emojis: {user_text}"
        outputs = generator(prompt, max_length=50, num_return_sequences=1)
        # Extract generated text after the prompt
        generated_text = outputs[0]['generated_text'][len(prompt):].strip()
        st.markdown(f"### Emoji Translation:\n\n{generated_text}")
