import os

path = "/Users/mdelatorre/tdw_example_controller_output/stimuli"
cmd = "rm -r " + path
os.system(cmd)



os.mkdir(path)
# os.system(cmd)


cmd = "python generation_scripts/run_tdw/get_tdw_sound.py"
os.system(cmd)

cmd = "python generation_scripts/run_tdw/get_tdw_images.py"
os.system(cmd)




# if stimli folder exists delete 

# create stimuli folder 

# call sound 

# call images 