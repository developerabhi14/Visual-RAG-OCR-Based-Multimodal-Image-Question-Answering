import re
import os
from TTS.api import TTS
import streamlit as st

# Path config
SPEAKER_WAV = "abhi.wav"
OUTPUT_WAV = "outputs/output.wav"

def clean_text(text):
    text = re.sub(r'[\*\_\~\`\#\@\[\]\{\}]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

@st.cache_resource  # Cache the TTS model in Streamlit session
def load_tts_model():
    return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False)

def speak_text(text):
    try:
        # Load the model only once per Streamlit session
        tts = load_tts_model()

        # Limit text length to reduce memory
        cleaned_text = clean_text(text)[:250]

        os.makedirs("outputs", exist_ok=True)

        tts.tts_to_file(
            text=cleaned_text,
            speaker_wav=SPEAKER_WAV,
            language="en",
            file_path=OUTPUT_WAV
        )

        os.system(f"aplay {OUTPUT_WAV}")
    except Exception as e:
        st.error(f"Voice synthesis failed: {e}")