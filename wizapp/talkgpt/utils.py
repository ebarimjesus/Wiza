import pyttsx3



def get_voice_options():
    voices = pyttsx3.init().getProperty('voices')
    voice_options = []
    for voice in voices:
        name = voice.name
        gender = voice.gender
        language = voice.languages[0]
        voice_options.append({'name': name, 'gender': gender, 'language': language})
    return voice_options

