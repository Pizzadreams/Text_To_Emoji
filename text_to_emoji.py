import streamlit as st
import emoji
from thefuzz import process

# Extensive mapping of keywords/phrases to emoji shortcodes
# You can expand this dictionary as needed for your use case
EMOJI_MAPPING = {
    "happy": ":smile:",
    "sad": ":cry:",
    "love": ":heart:",
    "fire": ":fire:",
    "party": ":tada:",
    "cat": ":cat:",
    "dog": ":dog:",
    "rocket": ":rocket:",
    "money": ":moneybag:",
    "food": ":pizza:",
    "music": ":musical_note:",
    "sun": ":sunny:",
    "moon": ":crescent_moon:",
    "star": ":star:",
    "car": ":car:",
    "red": ":red_circle:",
    "bull": ":ox:",
    "wings": ":angel:",
    "drink": ":tropical_drink:",
    "sports": ":basketball:",
    "computer": ":computer:",
    "phone": ":iphone:",
    "book": ":book:",
    "sleep": ":sleeping:",
    "work": ":briefcase:",
    "school": ":school:",
    "travel": ":airplane:",
    "coffee": ":coffee:",
    "cake": ":cake:",
    "gift": ":gift:",
    "rain": ":cloud_rain:",
    "snow": ":snowflake:",
    "angry": ":angry:",
    "surprised": ":open_mouth:",
    "cool": ":sunglasses:",
    "laugh": ":joy:",
    "cry": ":sob:",
    "kiss": ":kissing_heart:",
    "clap": ":clap:",
    "ok": ":ok_hand:",
    "thumbs up": ":thumbsup:",
    "thumbs down": ":thumbsdown:",
    "question": ":question:",
    "exclamation": ":exclamation:",
    "eye": ":eyes:",
    "butterfly": ":butterfly:",
    "mountain": ":mountain:",
    "brain": ":brain:",
    "link": ":link:",
    "egg": ":egg:",
    "clock": ":clock2:",
    "star": ":star:",
    "key": ":key:",
    "prince": ":prince:",
    "blue": ":blue_heart:",
    "adult": ":adult:",
    # To Do: Add more mappings as needed
}

# Precompute the list of emoji shortcodes for fuzzy matching
emoji_aliases = list(EMOJI_MAPPING.values())

def fuzzy_emoji_for_word(word, aliases, threshold=70):
    """
    For a given word, find the closest matching emoji shortcode using fuzzy matching.
    If a good match is found (score >= threshold), convert shortcode to emoji character.
    Otherwise, return the original word.
    """
    match = process.extractOne(word.lower(), aliases)
    if match and match[1] >= threshold:
        shortcode = match[0]  # e.g. ":smile:"
        # Convert shortcode to emoji character
        return emoji.emojize(shortcode, language='alias')
    else:
        return word

def sentence_to_emojis(sentence, aliases, threshold=70):
    """
    Convert each word in the sentence to an emoji if a close match is found.
    Words without good matches remain unchanged.
    """
    words = sentence.split()
    result = [fuzzy_emoji_for_word(word, aliases, threshold) for word in words]
    return ' '.join(result)

# Streamlit app title
st.title("Text to Emoji Translator")

# Input form for user sentence
with st.form("emoji_form"):
    user_text = st.text_input("Enter a sentence (e.g., 'Red bull gives you wings')")
    submitted = st.form_submit_button("Submit")

if submitted:
    if not user_text.strip():
        st.warning("Please enter some text before submitting.")
    else:
        # Translate sentence to emojis using fuzzy matching against the extended mapping
        emoji_sentence = sentence_to_emojis(user_text, emoji_aliases, threshold=70)
        # Display the emoji-translated sentence
        st.markdown(f"### Emoji Translation:\n\n{emoji_sentence}")
