#!/usr/bin/env python3
# Required ffmpeg

import os
import shlex

# Prompt the user to enter the input directory path
input_dir = input("Enter the input directory path: ")

# Remove leading and trailing quotation marks if present
input_dir = input_dir.strip('"')

# Verify if the entered path exists
if not os.path.exists(input_dir):
    print("Error: Input directory does not exist.")
    exit()

output_dir = os.path.join(input_dir, "output")  # Output directory will be created inside the input directory

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

count = 0

for root, _, files in os.walk(input_dir):
    for file in files:
        if file.lower().endswith('.ts'):
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_path, input_dir)
            output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + ".mp4")
            
            # Create output directory if it doesn't exist
            output_dir_path = os.path.dirname(output_path)
            if not os.path.exists(output_dir_path):
                try:
                    os.makedirs(output_dir_path)
                except OSError as e:
                    print("Error creating directory:", e)
                    continue
            
            if os.path.isfile(output_path):
                print('Already converted: "{}"'.format(input_path))
                continue
            
            ffmpeg_command = 'ffmpeg -i "{}" -c:v hevc_nvenc -preset fast -b:v 4000k -c:a aac -b:a 192k "{}"'.format(input_path, output_path)
            exit_code = os.system(ffmpeg_command)
            
            if exit_code == 0:
                count += 1
                print('Converted: "{}"'.format(input_path))
            else:
                print('Failed to convert: "{}"'.format(input_path))

print('Done. Total number of files converted:', count)
input("Press ENTER to exit...")