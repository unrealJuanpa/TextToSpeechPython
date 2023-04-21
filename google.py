import os

msg = "Esta es una pregunta de cultura general de dificultad baja. La capital de Venezuela es Caracas."

os.system(f"gtts-cli '{msg}' --lang es | play -t mp3 -")
