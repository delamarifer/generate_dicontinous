import os
from re import L 

dir = "/Users/mdelatorre/tdw_example_controller_output/stimuli/"



# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(dir):
    # for dir in dirs:
    #     latest_file_index = len(os.listdir(dir))
    #     print(latest_file_index)
    path = root.split(os.sep)
    if os.path.basename(root).endswith("sound"):
        sound_dir = dir + os.path.basename(root) + '/stimuli/'
        for root, dirs, files in os.walk(sound_dir):
            for f in files:
                cmd = "mv " + sound_dir + f + " output_stimuli/original_sounds/."
                print(f)
                os.system(cmd)