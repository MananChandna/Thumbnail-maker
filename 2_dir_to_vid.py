from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os
from moviepy.editor import *
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half-frame')
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths =[os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith('jpg')]

# print(filepaths)
# clip = ImageSequenceClip(filepaths, fps=4)
# clip.write_videofile(output_video)

directory = {}

for root, dirs, files in os.walk(thumbnail_per_frame_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key = float(fname.replace('.jpg',""))
        except:
            key = None
        if key != None:
            directory[key] = filepath

new_path = []
for k in sorted(directory.keys()):
    filepath = directory[k]
    new_path.append(filepath)
# clip = ImageSequenceClip(new_path, fps=10)
# clip.write_videofile(output_video)
    
my_clip = []
for path in list(new_path):
    frame = ImageClip(path)
    print(frame.img)
    my_clip.append(frame.img)

clip = ImageSequenceClip(my_clip, fps=22)
clip.write_videofile(output_video)