import os
from re import L 

dir = "/Users/mdelatorre/tdw_example_controller_output/stimuli/"



# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(dir):
    # for dir in dirs:
    #     latest_file_index = len(os.listdir(dir))
    #     print(latest_file_index)
    path = root.split(os.sep)
    if os.path.basename(root).endswith("images"):
        print((len(path) - 1) * '---', os.path.basename(root))
        imgs_dir = dir + os.path.basename(root) + '/a/'
        latest_file_index = len(os.listdir(imgs_dir))
        print(latest_file_index)
        for file in files:
            for i in range(4):
                cmd = 'sudo rm ' + imgs_dir + 'img_000' + str(i) + '.jpg' 
                os.system(cmd)

            # for i in range(5):

            #     cmd = 'sudo rm ' + imgs_dir + 'img_00' + str(latest_file_index-i) + '.jpg' 
            #     # os.system(cmd)
            #     # cmd = 'sudo rm ' + imgs_dir + 'img_00' + str(latest_file_index-1) + '.jpg' 
            #     # os.system(cmd)
            #     # cmd = 'sudo rm ' + imgs_dir + 'img_00' + str(latest_file_index-2) + '.jpg' 
            #     # os.system(cmd)
            #     # cmd = 'sudo rm ' + imgs_dir + 'img_00' + str(latest_file_index-3) + '.jpg' 
            #     os.system(cmd)
                
            # ffmpeg -i img_%04d.jpg -vcodec libx264 -pix_fmt yuv420p image_only_video.mp4
            cmd = "ffmpeg  -i " + imgs_dir + "img_%04d.jpg  -vcodec libx264 -pix_fmt yuv420p " + "output_stimuli/original_videos/" + os.path.basename(root).replace("_scrape_images","") + ".mp4"
            os.system(cmd)