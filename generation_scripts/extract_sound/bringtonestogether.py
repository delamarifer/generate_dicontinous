import subprocess

## define your paths
path1 = 'output_stimuli/original_sounds/'
path2 = 'output_stimuli/new_tones/'

## where to place the merged data
merged_path = 'output_stimuli/all_sounds/'

## write an rsync commands to merge the directories
rsync_cmd = 'rsync' + ' -avzh ' + path1 + ' ' + path2 + ' ' + merged_path

## run the rsync command
subprocess.run(rsync_cmd, shell=True)
