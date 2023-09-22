# Text-to-Video VSL Generator
The Text-to-Video VSL Generator is a Python application that allows users to input text and generate a video with a voiceover reading the text while displaying it in the video. It's a versatile tool that can be used for various purposes, including creating Video Sales Letters (VSLs) and educational content.

## Table of Contents
* Installation
* Usage
* Configuration Options
* Examples
* Contributing
* License
* Acknowledgments
* Contact Information
-----

## Installation

To set up the project locally, follow these steps:

1. Clone the repository to your local machine:

`git clone https://github.com/yourusername/text-to-video-VSL.git`

2. Change to the project directory:

`cd text-to-video-VSL Install the required Python packages using pip:`

`pip install -r requirements.txt`
3. Make sure you have the '**ImageMagick**' binary installed. You can download it from '[**ImageMagick**]('https://imagemagick.org/script/download.php')'.

4. Run the application:

`python app.py`

Now your Text-to-Video VSL Generator is up and running locally.
___
## Usage
To use the Text-to-Video VSL Generator, make a POST request to the /generate-video endpoint with the following parameters:

* '**text:**' The input text you want to include in the video.
* '**voice (optional):**' The voice language for the voiceover (default is English).
* '**font_color (optional):**' The font color for the text (default is white).
* '**background_color (optional):**' The background color of the text (default is black).
* '**background_opacity (optional):**' The background opacity (default is 1.0, no transparency).
* '**font_size (optional):**' The font size (default is 70).
* '**text_speed (optional):**' The text speed (default is 0.5).
* '**background_image_path (optional):**' Path to a background image (optional).

The generator will create a video with the specified text, voiceover, and visual settings.

## Configuration Options
You can customize the appearance and behavior of the generated videos by adjusting the following configuration options:

* '**voice:**' Specify the voice language for the voiceover.
* '**font_color:**' Choose the font color for the text.
* '**background_color:**' Set the background color for the text.
* '**background_opacity:**' Adjust the background opacity (0.0 for fully transparent, 1.0 for opaque).
* '**font_size:**' Change the font size.
* '**text_speed:**' Adjust the speed at which the text is displayed.
* '**background_image_path:**' Add a background image to the video.

## Examples
Here are some usage examples of the Text-to-Video VSL Generator:

Basic Usage: Generate a video with default settings:

`{
    "text": "This is a basic example of the Text-to-Video VSL Generator."
}`
Customized Appearance: Customize font color and background color:

`{
    "text": "This video has a custom font and background color.",
    "font_color": "blue",
    "background_color": "yellow"
}`
Background Image: Add a background image to the video:

`{
    "text": "This video has a custom background image.",
    "background_image_path": "path/to/background/image.jpg"
}`
## Contributing
If you would like to contribute to this project, please follow these guidelines:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Commit your changes with clear and concise messages.
Push your branch to your fork and submit a pull request to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.
_____
## Frontend
* Next.js
* Axios
* React

## Backend
* Python
* Acknowledgments
* MoviePy
* gTTS (Google Text-to-Speech)
* FFMPEG

----
## Contact Information
If you have any questions or suggestions, feel free to contact me
