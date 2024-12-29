import whisper
import srt
from datetime import timedelta

def split_text_into_chunks(text, max_words=10):
    """
    Split text into smaller chunks, each containing at most `max_words` words.
    """
    words = text.split()
    chunks = [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks

def generate_subtitles_with_whisper_and_prompt(audio_file, text_prompt, output_srt_file):
    # Load Whisper model
    model = whisper.load_model("base")  # Options: "tiny", "base", "small", "medium", "large"
    
    # Transcribe audio with text prompt
    result = model.transcribe(audio_file, initial_prompt=text_prompt, language="en")
    
    # Extract segments for subtitles
    segments = result["segments"]  # Contains timing information and text
    
    # Generate fine-grained subtitles
    subtitles = []
    subtitle_index = 1
    for segment in segments:
        start_time = segment["start"]
        end_time = segment["end"]
        text = segment["text"]
        
        # Split the segment into smaller chunks
        chunks = split_text_into_chunks(text, max_words=10)
        chunk_duration = (end_time - start_time) / len(chunks)
        
        for i, chunk in enumerate(chunks):
            start = timedelta(seconds=start_time + i * chunk_duration)
            end = timedelta(seconds=start_time + (i + 1) * chunk_duration)
            subtitle = srt.Subtitle(index=subtitle_index, start=start, end=end, content=chunk)
            subtitles.append(subtitle)
            subtitle_index += 1
    
    # Write SRT file
    with open(output_srt_file, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))


def create_subtitles(audio_file, text_prompt, output_srt_file):
    generate_subtitles_with_whisper_and_prompt(audio_file, text_prompt, output_srt_file)
