from flask import Flask, render_template, request
from modules.text_generator import generate_text
from modules.text_to_speech import text_to_speech
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    generated_text = None
    audio_file = None

    if request.method == "POST":
        user_input = request.form["text"]

        # Generate AI response
        generated_text = generate_text(user_input)

        # Convert AI-generated text to speech
        audio_file = text_to_speech(generated_text)

    return render_template("index.html", text=generated_text, audio_file=audio_file)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)
