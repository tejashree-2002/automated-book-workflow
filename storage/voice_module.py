
# === storage/voice_module.py ===

from gtts import gTTS
import os

def read_aloud_text(text, filename="outputs/final_audio.mp3"):
    print("\n>> Generating voice audio...")
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    tts = gTTS(text)
    tts.save(filename)
    print(f"Audio saved to {filename}")
