
import os 
from configparser import ConfigParser
import time 
import ast
#Read config.ini file
config_object = ConfigParser()
config_object.read("/Users/mdelatorre/Developer/generate_discont_demos/generation_scripts/run_tdw/tdw_config_images.ini")
configs = config_object["all"]



# single objects 
cont_names = ["cont","discont"]
short_long_names = ["", "long_"]
# forward_back = ["forward", "backward"]

cubesize = 0
obj = 0 
table = 0
table2 = 0
changemass = 0
changemat = 0
cont2 = 0
mass2 = 0
mass1 = 0
scrape1 = 0
pause_length = 20000


# for motion in range(2):
for length in range(2):
    for cont in range(2):
        # demoname = str(ast.literal_eval(configs['audiovisual'])) + \
        # '_' + str(ast.literal_eval(configs['object_num'])[obj]) + \
        # '_' + str(ast.literal_eval(configs['mass'])[mass1]) + \
        # '_' + str(ast.literal_eval(configs['secondmass'])[mass2]) + \
        # '_' + str(ast.literal_eval(configs['table1mat'])[table]) + \
        # '_' + str(ast.literal_eval(configs['table2mat'])[table2]) + \
        # '_' + str(ast.literal_eval(configs['continuity_obj1'])[cont]) + \
        # '_' + str(ast.literal_eval(configs['scrape1'])[scrape1]) + \
        # '_' + str(ast.literal_eval(configs['scrape2'])[scrape1]) + \
        # '_' + str(ast.literal_eval(configs['change_mass_mid'])[changemass]) + \
        # '_' + str(ast.literal_eval(configs['change_mat_mid'])[changemat]) + \
        # '_' + str(ast.literal_eval(configs['cube_size'])[cubesize])

        demoname = "stimuli/" + short_long_names[length] + cont_names[cont] 

        cmd =  'python3 /Users/mdelatorre/Developer/tdw/Python/example_controllers/audio_scrapes/' + configs['file_name'] + \
        ' --demotype ' +  str(demoname)  + \
        ' --scrape_length ' +  str(length)  + \
        ' --waiter_time ' +  str(pause_length)  + \
        ' --audiovisual ' + str(ast.literal_eval(configs['audiovisual'])) + \
        ' --mass ' + str(ast.literal_eval(configs['mass'])[mass1]) + \
        ' --secondmass ' + str(ast.literal_eval(configs['secondmass'])[mass2]) + \
        ' --table1mat ' + str(ast.literal_eval(configs['table1mat'])[table]) + \
        ' --table2mat ' + str(ast.literal_eval(configs['table2mat'])[table2]) + \
        ' --object_num ' + str(ast.literal_eval(configs['object_num'])[obj]) + \
        ' --continuity_obj1 ' + str(ast.literal_eval(configs['continuity_obj1'])[cont]) + \
        ' --continuity_obj2 ' + str(ast.literal_eval(configs['continuity_obj2'])[cont2]) + \
        ' --scrape2 ' + str(ast.literal_eval(configs['scrape1'])[scrape1]) + \
        ' --scrape1 ' + str(ast.literal_eval(configs['scrape2'])[scrape1]) + \
        ' --cubemat ' + str(ast.literal_eval(configs['cubemat'])[scrape1]) + \
        ' --cube2mat ' + str(ast.literal_eval(configs['cube2mat'])[scrape1]) + \
        ' --change_mass_mid ' + str(ast.literal_eval(configs['change_mass_mid'])[changemass]) + \
        ' --change_mat_mid ' + str(ast.literal_eval(configs['change_mat_mid'])[changemat]) + \
        ' --cube_size ' + str(ast.literal_eval(configs['cube_size'])[cubesize])

        print(cmd)
        os.system(cmd)
        # time.sleep(5)

