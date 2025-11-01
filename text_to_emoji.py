import streamlit as st
import emoji
from thefuzz import process
from transformers import pipeline

# Load text generation pipeline
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

# Emoji aliases from the emoji library
emoji_aliases = [alias.strip(":") for alias in emoji.EMOJI_ALIAS_UNICODE_ENGLISH.keys()]

def fuzzy_match(word, aliases, threshold=70):
    match = process.extractOne(word.lower(), aliases)
    if match and match[1] >= threshold:
        return emoji.emojize(f":{match[0]}:", language="alias")
    return word

def translate_to_emojis(sentence):
    words = sentence.split()
    emojis = [fuzzy_match(word, emoji_aliases) for word in words]
    return " ".join(emojis)

st.title("Emoji Translator")

with st.form("emoji_form"):
    user_text = st.text_input("Enter a sentence (e.g., 'I love pizza')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Generate emojis using fuzzy matching
        emoji_translation = translate_to_emojis(user_text)
        # Test with GPT-2 for refined output
        prompt = f"Translate this sentence to emojis: {user_text}"
        gpt_output = generator(prompt, max_length=50, truncation=True)
        refined_output = gpt_output[0]['generated_text'][len(prompt):].strip()
        st.markdown(f"### Emoji Translation:\n\n{emoji_translation}")
        st.markdown(f"### Refined Output:\n\n{refined_output}")
