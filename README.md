# Audio-to-Image Converter

This Python script converts audio recordings into images using state-of-the-art AI models from Hugging Face. It seamlessly integrates audio-to-text and text-to-image functionalities, enabling creative possibilities and enhancing user experiences.

## Usage

1. **Record Audio**: Execute the script to record audio. The recorded audio will be saved as a WAV file (`recorded_audio.wav` by default).

2. **Convert Audio to Text**: The recorded audio is then converted to text using the OpenAI Whisper-Large-v3 model.

3. **Generate Image from Text**: The generated text is used as a prompt to generate an image using the DataAutoGPT3's OpenDalleV1.1 model.

4. **View Generated Image**: The generated image is displayed using the PIL library.

## Requirements

- requests==2.26.0
- sounddevice==0.4.2
- scipy==1.7.3
- numpy==1.21.2
- Pillow==8.4.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kaustic-user/Audio-to-Image-Generator-HuggingFace-API.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage

3. Run the script:
```bash
python main.py
```

4. Follow the on-screen instructions to record audio and generate images.
