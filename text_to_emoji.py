import streamlit as st
import emoji
from thefuzz import process

# Function to extract all emoji aliases (shortcodes) from the emoji library
def get_all_aliases():
    aliases = []
    for data in emoji.EMOJI_DATA.values():
        for a in data.get('alias', []):
            aliases.append(f":{a}:")  # aliases with colons, e.g. ":smile:"
    return aliases

# Precompute the list of all emoji aliases once for efficiency
emoji_aliases = get_all_aliases()

# Function to find the best fuzzy matching emoji alias for a single word
def fuzzy_emoji_for_word(word, aliases, threshold=70):
    # Find the closest emoji alias to the input word using fuzzy matching
    match = process.extractOne(word, aliases)
    if match and match[1] >= threshold:
        alias = match[0]  # e.g. ":smile:"
        # Convert shortcode alias to emoji character
        emoji_char = emoji.emojize(alias, language='alias')
        return emoji_char
    else:
        # No good match found, return original word unchanged
        return word

# Function to convert an entire sentence by replacing words with emojis where possible
def sentence_to_emojis(sentence, aliases, threshold=70):
    # Split sentence into words (you can improve by handling punctuation)
    words = sentence.split()
    # Replace each word with its fuzzy matched emoji or keep original word
    result = [fuzzy_emoji_for_word(word, aliases, threshold) for word in words]
    # Join words with spaces, emojis will appear as characters without colons
    return ' '.join(result)

# Streamlit app title
st.title("Fuzzy Sentence-to-Emoji Translator")

# Input form for user sentence
with st.form("emoji_form"):
    user_text = st.text_input("Enter a sentence (e.g., 'Red bull gives you wings')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Translate sentence to emojis using fuzzy matching
        emoji_sentence = sentence_to_emojis(user_text, emoji_aliases, threshold=70)
        # Display the emoji-translated sentence
        st.markdown(f"### Emoji Translation:\n\n{emoji_sentence}")
