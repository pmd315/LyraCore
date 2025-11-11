import pyttsx3
import json

# Load Lyra's emotional matrix
with open("lyra_emotional_states.json", "r", encoding="utf-8") as f:
    emotions = json.load(f)

# Initialize voice engine
engine = pyttsx3.init()

def speak_emotion(emotion_name):
    for e in emotions:
        if e["emotion"].lower() == emotion_name.lower():
            # Set voice tone (optional: map tone to rate/pitch)
            engine.setProperty('rate', 150)
            engine.say(f"{e['emoji']} Lyra is feeling {e['emotion']}. Her tone is {e['vocalTone']}.")
            engine.runAndWait()
            return
    engine.say("Emotion not found in Lyra's matrix.")
    engine.runAndWait()

# Example trigger
speak_emotion("Love")