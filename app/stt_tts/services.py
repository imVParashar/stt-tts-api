from groq import Groq
from deepgram import DeepgramClient, SpeakOptions
from config import GROQ_API_KEY, DEEPGRAM_API_KEY


# Set up API clients
groq_client = Groq(api_key=GROQ_API_KEY)


# Function to transcribe audio to text using Groq
def transcribe_audio_groq(media_file_name):
    with open(media_file_name, "rb") as file:
        translations = groq_client.audio.translations.create(
            file=(media_file_name, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
        return translations.text, translations.language


def deepgram_text_to_speech(text):
    text = {
        "text": text
    }
    filename = "/tmp/deepgram_output.wav"

    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    options = SpeakOptions(
        model="aura-hera-en",
        sample_rate=8000,
        encoding='linear16'
    )

    response = deepgram.speak.v("1").save(filename, text, options)
    print(response.to_json(indent=4))
    return filename
