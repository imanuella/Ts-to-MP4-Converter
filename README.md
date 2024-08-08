# Ts-to-MP4-Converter

Convert `.ts` video files to `.mp4` format using FFmpeg.

This Python program allows you to convert `.ts` videos in bulk, including files within subdirectory folders. Additionally, it now supports converting files from URLs, giving you more flexibility in converting your video files.

## Features

- Convert `.ts` video files to `.mp4` format.
- Support for converting files from a local directory or a URL.
- Bulk conversion, including files within subdirectories.
- Utilize GPU acceleration with FFmpeg (using `gpu.py`).

## Usage

1. **Clone the Repository**

    ```
    git clone https://github.com/your_username/Ts-to-MP4-Converter.git
    cd Ts-to-MP4-Converter
    ```

2. **Install Dependencies**

    Ensure you have Python 3 installed along with FFmpeg. You can install FFmpeg from the official website: [ffmpeg.org](https://ffmpeg.org/download.html).

3. **Run the Program**

    ```
    python ts_to_mp4_converter.py
    ```

    Follow the on-screen instructions to choose your input source (local directory or URL) and provide necessary details.

4. **Enjoy Converted Videos**

    Once the conversion process is complete, you'll find your converted `.mp4` files in the specified output directory.

## GPU Acceleration

To utilize GPU acceleration with FFmpeg, change the ffmpeg command inside the `main.py` 

    ffmpeg_command = 'ffmpeg -i "{}" -c:v hevc_nvenc -preset fast -b:v 4000k -c:a aac -b:a 192k "{}"'.format(input_path, output_path)
## Comments

- Ensure that the input video codec (`-c:v`) and output video bitrate (`-b:v`) parameters are suitable for your GPU capabilities and desired output quality.
- Adjust the output audio codec (`-c:a`) and bitrate (`-b:a`) parameters as needed for your specific requirements.

## Demo

- Converting from directory

  <img src="TstoMp4/demo/directory.gif" alt="Demo" width="500"/>

- Converting from URL
  
  <img src="TstoMp4/demo/url.gif" alt="Demo" width="500"/>
