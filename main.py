import numpy as np
import sounddevice as sd
import random
import time

samplerate = 44100

moods = {
    "chill": {"notes": [220, 261.63, 293.66], "speed": (1.5, 2.5)},
    "focus": {"notes": [261.63, 329.63, 392.00], "speed": (0.8, 1.5)},
    "sleep": {"notes": [174, 196, 220], "speed": (2.0, 3.5)}
}

def play_tone(freq, duration):
    t = np.linspace(0, duration, int(samplerate * duration), False)
    tone = np.sin(freq * t * 2 * np.pi)

    # mjuk fade
    envelope = np.linspace(0, 1, len(tone))
    tone *= envelope

    sd.play(tone * 0.2, samplerate)
    sd.wait()

# välj mood
mood = input("Välj mood (chill / focus / sleep): ").lower()

if mood not in moods:
    print("Ogiltigt mood, kör chill istället.")
    mood = "chill"

settings = moods[mood]

while True:
    note = random.choice(settings["notes"])
    duration = random.uniform(*settings["speed"])

    play_tone(note, duration)
    time.sleep(0.2)
