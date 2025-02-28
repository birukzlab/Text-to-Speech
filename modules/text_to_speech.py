from gtts import gTTS
import os

def text_to_speech(text):
    """Convert text to speech and save as an audio file."""
    output_path = "static/output.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(output_path)
    return output_path
