import streamlit as st
import requests
import json

# Function to get some random emoji samples from emoji-helper API (optional)
def get_random_emojis(n=5):
    url = f"https://emojihelper-1-v4897410.deta.app/random?n={n}&skintones=False&nogroup=Symbols,Flags"
    response = requests.get(url)
    return json.loads(response.text)

# Your own mapping function: converts words to emojis if present in dictionary
def text_to_custom_emojis(text):
    emoji_map = {
        "red": "🟥",
        "bull": "🐂",
        "wings": "🪽",
        "you": "👉",
        "gives": "🤲"
    }
    words = text.lower().split()
    return " ".join([emoji_map.get(word, word) for word in words])

st.title("Text to Emoji Translator")

# Single-line text input
user_text = st.text_input("Enter text to translate", placeholder="Type a phrase here...")

# Multi-line text input if you want (longer text)
# user_text = st.text_area("Enter text to translate", placeholder="Type a phrase here...")

if user_text:
    emoji_text = text_to_custom_emojis(user_text)
    st.markdown(f"### Emoji Translation:\n\n{emoji_text}")

    # # Optionally show some random emojis from API for inspiration
    # r_emojis = get_random_emojis(5)
    # st.write("Random Emojis from API:", " ".join(r_emojis))
