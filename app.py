import streamlit as st

st.set_page_config(page_title="Morse Code Translator", page_icon="🔤")
st.title("🔤 Morse Code Translator")
st.write("Translate between English and Morse Code (Press Enter only)")

# Morse dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

mode = st.radio(
    "Select Translation Mode",
    ("English → Morse", "Morse → English")
)

text = st.text_input("Enter text and press Enter")

# Auto-translate when Enter is pressed
if text:
    if mode == "English → Morse":
        result = []
        for char in text.upper():
            if char == " ":
                result.append("/")
            elif char in MORSE_CODE:
                result.append(MORSE_CODE[char])

        st.subheader("📟 Morse Code")
        st.success(" ".join(result))

    else:
        result = []
        words = text.split(" / ")
        for word in words:
            letters = word.split()
            for l in letters:
                if l in REVERSE_MORSE:
                    result.append(REVERSE_MORSE[l])
            result.append(" ")

        st.subheader("🔤 English Text")
        st.success("".join(result))
