from flask import Flask, request, jsonify, send_from_directory
import moviepy.editor as mp
import os
from flask_cors import CORS
from gtts import gTTS
import re

app = Flask(__name__)
CORS(app)

os.environ["IMAGEMAGICK_BINARY"] = "/usr/local/bin/magick"

@app.route('/generate-video', methods=['POST'])
def generate_video():
    try:
        data = request.get_json()
        print("Received data:", data)

        text = data['text']
        voice = data.get('voice', 'en')  # Default voice is English
        font_color = data.get('font_color', 'white')  # Default font color is white
        background_color = data.get('background_color', 'black')  # Default background color is black
        background_opacity = data.get('background_opacity', 1.0)  # Default opacity is 1.0 (no transparency)
        font_size = data.get('font_size', 70)  # Default font size is 70
        text_speed = data.get('text_speed', 0.5)  # Default text speed (adjust as needed)
        background_image_path = data.get('background_image_path')  # Path to background image (optional)

        # Generate voiceover using gTTS with the specified voice
        tts = gTTS(text=text, lang=voice)
        tts.save('voiceover.mp3')
        print("Voiceover generated")

        # Split the text into sentences using commas (',') and punctuation
        sentences = re.split(r'[.,!?]', text)

        # Create a list to store TextClips for each sentence
        sentence_clips = []

        # Calculate the duration for each sentence based on audio duration
        audio_duration = mp.AudioFileClip('voiceover.mp3').duration
        sentence_duration = audio_duration / len(sentences)

        current_time = 0

        for sentence in sentences:
            # Skip empty sentences
            if not sentence.strip():
                continue

            # Create a TextClip centered on the screen
            if background_image_path:
                # Load the background image and resize it to match the text clip size
                bg_image = mp.ImageClip(background_image_path)
                bg_image = bg_image.resize(size=(1500, 1000))  # Adjust the size as needed

                # Create a TextClip with background image
                word_clip = mp.TextClip(
                    sentence.strip(),
                    fontsize=font_size,
                    color=font_color,
                    bg_color=background_color,
                    size=(1500, 1000)
                )
                word_clip = word_clip.set_duration(sentence_duration)
                word_clip = word_clip.set_start(current_time)

                # Create a semi-transparent background color clip
                bg_color_clip = mp.ColorClip(
                    size=(1500, 1000),
                    color=background_color,
                    duration=sentence_duration,
                    is_mask=True,
                    opacity=background_opacity
                )

                # Composite the background color clip, background image, and text clip
                sentence_clip = mp.CompositeVideoClip([bg_color_clip, bg_image.set_duration(sentence_duration), word_clip])
            else:
                # Create a TextClip without background image
                sentence_clip = mp.TextClip(
                    sentence.strip(),
                    fontsize=font_size,
                    color=font_color,
                    bg_color=background_color,
                    size=(1500, 1000)
                )
                sentence_clip = sentence_clip.set_duration(sentence_duration)
                sentence_clip = sentence_clip.set_start(current_time)

            sentence_clips.append(sentence_clip)
            current_time += sentence_duration

        # Create a final CompositeVideoClip for all sentences
        text_clip = mp.concatenate_videoclips(sentence_clips, method="compose")

        # Create an audio clip from the generated voiceover
        audio_clip = mp.AudioFileClip('voiceover.mp3')

        # Set the audio for the text clip
        text_clip = text_clip.set_audio(audio_clip)

        # Set the duration for the text clip (same as audio duration)
        text_clip = text_clip.set_duration(audio_duration)

        # Set the fps for the text clip (e.g., 24 fps)
        text_clip = text_clip.set_fps(24)  # Adjust the value as needed

        # Define the directory for saving the video file
        output_directory = 'VSL'
        os.makedirs(output_directory, exist_ok=True)  # Ensure the directory exists

        # Write the video file using moviepy
        video_output_path = os.path.join(output_directory, 'voiceover_output.mp4')
        text_clip.write_videofile(video_output_path, codec='libx264', audio_codec='aac')
        print("Video generated")

        # Clean up temporary files
        os.remove('voiceover.mp3')
        print("Temporary files cleaned up")

        # Return the generated video file path
        return send_from_directory(output_directory, 'voiceover_output.mp4')

    except Exception as e:
        error_message = f'Error: {e}'
        print(error_message)  # Log the specific error message
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)