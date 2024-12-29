from melo.api import TTS
import nltk
nltk.download('averaged_perceptron_tagger_eng')
# Speed is adjustable
def synthesize_speech(script_text, output_path="data/audio/audio.mp3"):
    speed = 1.0

    # CPU is sufficient for real-time inference.
    # You can set it manually to 'cpu' or 'cuda' or 'cuda:0' or 'mps'
    device = 'auto' # Will automatically use GPU if available

    # English 
    #TODD: add utils that changes AITA to "Am I the asshole "
    model = TTS(language='EN', device=device)
    speaker_ids = model.hps.data.spk2id

    # American accent
    output_path = 'en-us.wav'
    model.tts_to_file(script_text, speaker_ids['EN-US'], output_path, speed=speed)

