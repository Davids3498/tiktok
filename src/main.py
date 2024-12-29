# main.py

from llm.llm_generate import generate_script
from tts.tts_convert import synthesize_speech
from subtitles.generate_subtitles import create_subtitles
# from video.combine_video import assemble_video
# from upload.upload_tiktok import upload_video

def main():
    # 1. Generate text (script)
    script_text = generate_script("generate me a AITA type post.", "llm/promp_templates/AITA.json")
    
    # 2. Convert text to speech (TTS)
    audio_file_path = synthesize_speech(script_text, output_path="data/audio/audio.mp3")

    # 3. Generate subtitles
    # Option A: Basic timing (based on word count or TTS duration)
    subtitle_file_path = create_subtitles(script_text, audio_file_path, output_path="data/subtitles/subtitle.srt")

    # 4. Combine everything into video
    # video_file_path = assemble_video(
    #     audio_path=audio_file_path,
    #     subtitle_path=subtitle_file_path,
    #     background="data/backgrounds/static_bg.jpg",
    #     output_path="data/videos/output.mp4"
    # )

    # # 5. Upload to TikTok (optional MVP step)
    # upload_video(video_file_path, caption="Your daily motivation!")
    
if __name__ == "__main__":
    main()
