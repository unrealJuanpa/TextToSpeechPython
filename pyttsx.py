import pyttsx3

engine = pyttsx3.init()

def hablar(texto, indice):
    engine.setProperty('voice', engine.getProperty('voices')[indice].id)
    engine.say(texto)
    engine.runAndWait()
    engine.stop()

msg = "Esta es una pregunta de cultura general de dificultad baja. La capital de Venezuela es Caracas."

indices = [1]

for idx in indices:
    print(f'Voz {idx} hablando...')
    hablar(msg, idx)
