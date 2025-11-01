import streamlit as st
import emoji
from thefuzz import process

# Function to extract all emoji aliases (shortcodes) from the emoji library
def get_all_aliases():
    aliases = []
    # Iterate over all emoji data entries
    for data in emoji.EMOJI_DATA.values():
        # Each emoji may have multiple aliases (shortcodes without colons)
        for a in data.get('alias', []):
            # Format alias with colons to match emoji.emojize() syntax
            aliases.append(f":{a}:")
    return aliases

# Precompute the list of all emoji aliases once for efficiency
emoji_aliases = get_all_aliases()

# Function to find the best fuzzy matching emoji alias for a single word
def fuzzy_emoji_for_word(word, aliases, threshold=70):
    # Use fuzzy matching to find the closest alias to the input word
    match = process.extractOne(word, aliases)
    # If a match is found and similarity score exceeds threshold, convert to emoji
    if match and match[1] >= threshold:
        return emoji.emojize(match[0], language='alias')
    else:
        # Otherwise, return the original word unchanged
        return word

# Function to convert an entire sentence by replacing words with emojis where possible
def sentence_to_emojis(sentence, aliases, threshold=70):
    # Split the sentence into individual words
    words = sentence.split()
    # Replace each word with its fuzzy matched emoji or keep original word
    result = [fuzzy_emoji_for_word(word, aliases, threshold) for word in words]
    # Join the transformed words back into a single string
    return ' '.join(result)

# Streamlit app title
st.title("Fuzzy Sentence-to-Emoji Translator")

# Create a form for user input to allow submission via Enter key or button
with st.form("emoji_form"):
    user_text = st.text_input("Enter a sentence (e.g., 'Red bull gives you wings')")
    submitted = st.form_submit_button("Submit")

# When the form is submitted
if submitted:
    if not user_text.strip():
        # Warn user if input is empty or only whitespace
        st.warning("Please enter some text before submitting.")
    else:
        # Convert the input sentence to emojis using fuzzy matching
        emoji_sentence = sentence_to_emojis(user_text, emoji_aliases, threshold=70)
        # Display the emoji-translated sentence
        st.markdown(f"### Emoji Translation:\n\n{emoji_sentence}")
