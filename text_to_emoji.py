import streamlit as st
import emoji
# Testing the text_to_custom_emojis function with some sample input
def text_to_custom_emojis(text):
    emoji_map = {
        'happy': '😊',
        'sad': '😢',
        'love': '❤️',
        'python': '🐍',
        'fire': '🔥',
    }
    words = text.split()
    result = []
    for w in words:
        lw = w.lower()
        if lw in emoji_map:
            result.append(emoji_map[lw])
        else:
            result.append(w)
    return ' '.join(result)

st.title("Text to Emoji Translator")

with st.form("emoji_form"):
    user_text = st.text_input("Enter text to translate")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        emoji_text = text_to_custom_emojis(user_text)
        st.markdown(f"### Emoji Translation:\n\n{emoji_text}")
