import os


# call get audio visual 
cmd = "python generation_scripts/run_tdw/get_audio_visual.py"
os.system(cmd)



path = "output_stimuli/original_videos"
if os.path.exists(path):
    cmd = "rm -r " + path
    os.system(cmd)
os.mkdir(path)
# image to video 
cmd = "python generation_scripts/extract_vid/imagetovideo.py"
os.system(cmd)


# sounds to tones
# move sounds
path = "output_stimuli/original_sounds"
if os.path.exists(path):
    cmd = "rm -r " + path
    os.system(cmd)
os.mkdir(path)
cmd = "python generation_scripts/extract_sound/bring_sounds.py"
os.system(cmd)

# get hillbert
path = "output_stimuli/new_tones"
if os.path.exists(path):
    cmd = "rm -r " + path
    os.system(cmd)
os.mkdir(path)
cmd = "python generation_scripts/generate_tones/hillbert_transform.py"
os.system(cmd)



# merge sounds and tones folder 
path = "output_stimuli/all_sounds/"
if os.path.exists(path):
    cmd = "rm -r " + path
    os.system(cmd)
os.mkdir(path)
cmd = "python generation_scripts/extract_sound/bringtonestogether.py"
os.system(cmd)

path2 = "output_stimuli/all_sounds_normalized/"
if os.path.exists(path2):
    cmd = "rm -r " + path2
    os.system(cmd)
os.mkdir(path2)
# normalize sounds 
cmd = "ffmpeg-normalize " + path + "*.wav -of output_stimuli/all_sounds_normalized -ext wav"
# print(cmd)
os.system(cmd)


# merge video and audio 
path = "output_stimuli/final_stimuli/"
if os.path.exists(path):
    cmd = "rm -r " + path
    os.system(cmd)
os.mkdir(path)
cmd = "python generation_scripts/generate_audiovisual/mergevideosound.py"
os.system(cmd)


cmd = "python generation_scripts/generate_audiovisual/delayed_stimuli.py"
os.system(cmd)

# ORGANIZE SUBFOLDERS




