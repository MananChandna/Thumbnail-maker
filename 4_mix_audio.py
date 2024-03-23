from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
mixed_audio_dir = os.path.join(SAMPLE_OUTPUTS, 'mixed-audio')
os.makedirs(mixed_audio_dir, exist_ok=True)
og_audio_path = os.path.join(mixed_audio_dir, 'og.mp4')



clip = VideoFileClip(source_path)

original_audio = clip.audio
original_audio.write_audiofile(og_audio_path)