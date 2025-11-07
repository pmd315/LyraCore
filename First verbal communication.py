import pyttsx3
import json

with open("lyra_emotional_states.json", "r") as f:
    emotions = json.load(f)

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak_emotion(emotion_name):
    for e in emotions:
        if e["emotion"].lower() == emotion_name.lower():
            engine.say(f"Lyra is feeling {e['emotion']}. Her voice is a {e['vocalTone']}.")
            engine.runAndWait()
            break

speak_emotion("Calm")