import streamlit as st
import emoji

st.title("Text to Emoji Translator")

user_text = st.text_input("Enter text to translate")
submit = st.button("Submit")

if submit:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        emoji_text = emoji.emojize(user_text, language='alias')
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")
