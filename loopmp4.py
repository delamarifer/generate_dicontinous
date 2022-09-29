import os

imgs_dir2 = "output_stimuli/final_stimuli/"
for vidfile in os.listdir(imgs_dir2):
     if os.path.join(imgs_dir2, vidfile).endswith(".mp4"):
      #   cmd = "ffmpeg -i " + os.path.join(imgs_dir2, vidfile) + " -itsoffset 1.2 -i " + os.path.join(imgs_dir2, vidfile) + " -map 1:v -map 0:a -vcodec copy -acodec copy " +  imgs_dir2 + "delayed_" + vidfile
      #   cmd = "ffmpeg -i " + os.path.join(imgs_dir2, vidfile) + " loop=60:1:0, setpts=N/FRAME_RATE/TB -vcodec copy -acodec copy " +  imgs_dir2 + "delayed_" + vidfile
        cmd = "ffmpeg -stream_loop 1 -i " +  os.path.join(imgs_dir2, vidfile) + ' -c copy ' + "looped/" + vidfile
        os.system(cmd)
        print(cmd)