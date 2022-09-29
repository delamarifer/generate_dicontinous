
import os

imgs_dir = "output_stimuli/original_videos/"
sound_dir = "output_stimuli/all_sounds_normalized/"
imgs_dir2 = "output_stimuli/final_stimuli/"
for vidfile in os.listdir(imgs_dir):
    for audiofile in os.listdir(sound_dir):
        if os.path.join(imgs_dir, vidfile).endswith(".mp4") and os.path.join(sound_dir, audiofile).endswith(".wav"):
           
            out_name = imgs_dir2 + vidfile.replace(".mp4","") + "_" + audiofile.replace(".wav","") + ".mp4"
            # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4
            cmd = "ffmpeg -i " +  imgs_dir + vidfile + " -i " + sound_dir + audiofile + " -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 " + out_name

            # ffmpeg -i "movie.mp4" -itsoffset 3.84 -i "movie.mp4" -map 0:v -map 1:a -c copy "movie-audio-delayed.mp4"

            os.system(cmd)
            print("done")

# imgs_dir2 = "/Users/mdelatorre/Developer/MotionContinuityPerception/merged_videos2"
# for vidfile in os.listdir(imgs_dir2):
#      if os.path.join(imgs_dir2, vidfile).endswith(".mp4"):
#         cmd = "ffmpeg -i " + os.path.join(imgs_dir2, vidfile) + " -itsoffset 1.2 -i " + os.path.join(imgs_dir2, vidfile) + " -map 1:v -map 0:a -vcodec copy -acodec copy " +  imgs_dir2 + "delayed_" + vidfile
#         # cmd = "ffmpeg -i " + os.path.join(imgs_dir2, vidfile) + " loop=60:1:0, setpts=N/FRAME_RATE/TB -vcodec copy -acodec copy " +  imgs_dir2 + "delayed_" + vidfile
#         # cmd = "ffmpeg -i " +  os.path.join(imgs_dir2, vidfile) + ' -filter_complex "loop=loop=15:size=1:start=0" ' + "looped/looped_" + vidfile
#         os.system(cmd)
#         print(cmd)