#!/usr/bin/env python3
# Required ffmpeg

import os
import shlex
import urllib.request
import tempfile


# Function to download file from URL
def download_file(url):
    temp_dir = tempfile.mkdtemp()
    file_name = os.path.basename(url)
    file_path = os.path.join(temp_dir, file_name)
    try:
        urllib.request.urlretrieve(url, file_path)
        return file_path
    except Exception as e:
        print("Error downloading file:", e)
        return None


# Function to convert a file using FFmpeg
def convert_file(input_path, output_path):
    # Create output directory if it doesn't exist
    output_dir_path = os.path.dirname(output_path)
    if not os.path.exists(output_dir_path):
        try:
            os.makedirs(output_dir_path)
        except OSError as e:
            print("Error creating directory:", e)
            return

    if os.path.isfile(output_path):
        print('Already converted: "{}"'.format(input_path))
        return

    ffmpeg_command = 'ffmpeg -i "{}" "{}"'.format(input_path, output_path)
    exit_code = os.system(ffmpeg_command)

    if exit_code == 0:
        print('Converted: "{}"'.format(input_path))
        return True
    else:
        print('Failed to convert: "{}"'.format(input_path))
        return False


# Prompt the user to choose the input source
source_choice = input("Choose input source (1 - Directory, 2 - URL): ")

if source_choice == '1':
    # Prompt the user to enter the input directory path
    input_dir = input("Enter the input directory path: ")

    # Remove leading and trailing quotation marks if present
    input_dir = input_dir.strip('"')

    # Verify if the entered path exists
    if not os.path.exists(input_dir):
        print("Error: Input directory does not exist.")
        exit()

    # Proceed with the directory conversion process
    output_dir = os.path.join(input_dir, "output")  # Output directory will be created inside the input directory
elif source_choice == '2':
    # Prompt the user to enter the URL
    url = input("Enter the URL of the file to convert: ")
    input_file = download_file(url)
    if input_file is None:
        print("Error: Failed to download the file from the URL.")
        exit()
    # Prompt the user to enter the output directory path
    output_dir = input("Enter the output directory path: ")
    # Remove leading and trailing quotation marks if present
    output_dir = output_dir.strip('"')
else:
    print("Invalid choice.")
    exit()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

count = 0

if source_choice == '1':
    # Directory conversion process
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.ts'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + ".mp4")
                if convert_file(input_path, output_path):
                    count += 1
elif source_choice == '2':
    # Single file conversion process
    file_name = os.path.basename(input_file)
    output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".mp4")
    if convert_file(input_file, output_path):
        count += 1

print('Done. Total number of files converted:', count)

input("Press ENTER to exit...")
