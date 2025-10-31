import streamlit as st
import emoji

st.title("Text to Emoji Translator")

with st.form("emoji_form"):
    user_text = st.text_input("Enter text with emoji shortcodes (e.g., ':rocket:', ':smile:')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Convert all emoji shortcodes in the sentence to emojis
        emoji_text = emoji.emojize(user_text, language='alias')
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")
