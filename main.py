import io
from PIL import Image
import requests
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np



def record_audio(file_path, duration=10, sample_rate=44100):
    print("Recording audio... Speak now!")

    # Record audio
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()

    print("Recording complete. Saving to", file_path)

    # Save audio to file
    write(file_path, sample_rate, audio_data)

    print("Audio saved successfully!")

if __name__ == "__main__":
    file_path = "recorded_audio.wav"
    record_audio(file_path)

#Audio to text
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json().get('text', '')


output_text = query("recorded_audio.wav")
print(output_text)



#text to image
API_URL = "https://api-inference.huggingface.co/models/dataautogpt3/OpenDalleV1.1"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def generate_image(text):
	return query({"inputs": text})

text_prompt = output_text
image_bytes=generate_image(text_prompt)
print(image_bytes)

# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()
