from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import VideoFileClip
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half-frame')
os.makedirs(thumbnail_dir, exist_ok=True)
os.makedirs(thumbnail_per_frame_dir, exist_ok=True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok=True)

clip = VideoFileClip(source_path)
print(clip.reader.fps)#frames per second
print(clip.reader.nframes)
print(clip.duration)#seconds
duration = clip.duration
max_duration = int(duration)+1
for i in range(0 , max_duration):
    frame = clip.get_frame(i)
    new_image_path = os.path.join(thumbnail_dir, f"{i}.jpg")
    #print(f"Frames at {i} seconds saved at {new_image_path}")
    # print(frame)
    new_image = Image.fromarray(frame)
    new_image.save(new_image_path)

print(clip.reader.fps)#frames per second
print(clip.reader.nframes)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps*1.0)

for i, frame in enumerate(clip.iter_frames()):
    if i%fps==0:
        current_ms =int(( i/fps)*1000)
        new_image_path = os.path.join(thumbnail_per_frame_dir, f"{current_ms}.jpg")
        #print(f"Frames at {i} seconds saved at {new_image_path}")
        # print(frame)
        new_image = Image.fromarray(frame)
        new_image.save(new_image_path)

for i, frame in enumerate(clip.iter_frames()):
    fphs = int(fps/2)
    if i%fphs==0:
        current_ms =int(( i/fps)*1000)
        new_image_path = os.path.join(thumbnail_per_half_second_dir, f"{current_ms}.jpg")
        #print(f"Frames at {i} seconds saved at {new_image_path}")
        # print(frame)
        new_image = Image.fromarray(frame)
        new_image.save(new_image_path)