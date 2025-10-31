import streamlit as st
import emoji
# Testing the text_to_custom_emojis function with some sample input
def text_to_custom_emojis(text):
    # Custom word-to-emoji mapping
    emoji_map = {
        'happy': '😊',
        'sad': '😢',
        'love': '❤️',
        'python': '🐍',
        'fire': '🔥',
        'dog': ':dog:',  # Example: use emoji shortcodes too!
        'cat': ':cat:'
    }
    words = text.split()
    result = []
    # Iterate over each word in the input text, check if it matches any key in the emoji_map (case-insensitive), and replace it with the corresponding emoji if found
    for w in words:
        lw = w.lower()
        if lw in emoji_map:
            result.append(emoji_map[lw])
        else:
            result.append(w)
    # Join back to a sentence
    sentence = ' '.join(result)
    # Now convert any shortcodes to emojis using the emoji library
    return emoji.emojize(sentence, language='alias')