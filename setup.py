import os

# Define the project structure inside Text-to-Speech
project_structure = {
    "static": [],  # Stores generated speech files
    "templates": ["index.html"],  # HTML UI
    "modules": ["text_generator.py", "text_to_speech.py"]  # AI & TTS logic
}

# Create directories and files inside "Text-to-Speech"
for folder, files in project_structure.items():
    folder_path = os.path.join("Text-to-Speech", folder)
    os.makedirs(folder_path, exist_ok=True)  # Create directory
    for file in files:
        with open(os.path.join(folder_path, file), "w") as f:
            pass  # Create an empty file

# Create main files
main_files = ["app.py", "requirements.txt", "README.md"]
for file in main_files:
    with open(os.path.join("Text-to-Speech", file), "w") as f:
        pass

print("✅ Project structure updated successfully!")

