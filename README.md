# AI-Powered Storyboard Generator

## Objective
The goal of this project is to develop a prototype storyboard generator that creates a visual storyboard based on a text description. Users can specify the number of scenes or shots, and the tool will generate corresponding images and text descriptions for each scene.

## Features
- **Input Handling**: Users can input a short story or scene description and specify the number of scenes they want to generate.
- **Scene Segmentation**: The tool uses natural language processing (NLP) to segment the input text into a coherent number of scenes.
- **Image Generation**: A pre-trained image generation model (e.g., DALL-E) creates images based on the segmented scene descriptions.
- **Storyboard Creation**: Generates a storyboard in PDF or HTML format, containing the images and corresponding text descriptions.
- **User Interface**: A command-line interface (CLI) or basic web interface allows users to input their story and see the resulting storyboard.
- **Error Handling**: Includes error handling for invalid inputs, API failures, and other edge cases.
- **Customization**: Allows customization of image size, layout, and more through a configuration file or command-line arguments.

## Requirements
- Python 3.x
- NLP model (e.g., spaCy)
- Pre-trained image generation model (e.g., DALL-E API or a similar alternative)
- Flask (if using the web interface)

## Installation
### Create Enviroment
```
python3 -m venv venv
```

### Activate Environment
```
source venv/bin/activate
```

### Install dependencies
```
pip3 install -r requirements.txt
```

### Downloading the model
```
python3 -m spacy download en_core_web_sm
```

### Running the project
```
python3 app.py
```

## Usage Guide
* Input: Enter a story or scene description when prompted or via the web interface.
* Specify Number of Scenes: Choose how many scenes the storyboard should have.
* View Storyboard: Once generated, view the resulting storyboard as a PDF or HTML,        containing images for each scene with accompanying text.

## Configuration
* API Keys: Add any necessary API keys (e.g., for image generation) in a .env file.
* Customization Options: Provide image size, through the web interface while generating the story scenes.

## Error Handling
The tool includes error handling for:
* Invalid user inputs (e.g., non-text entries or an unreasonable number of scenes).
* API call failures (e.g., image generation service issues).
* File operation errors (e.g., inability to save the storyboard).

## Deliverables
* Python source code for the storyboard generator
* requirements.txt file listing all dependencies
* README.md with setup instructions, usage guide, and assumptions
* Sample output storyboards demonstrating the tool's capabilities
* (Optional) A simple web interface for the tool

## Generated Stories
You can go to `/generated-stories` to see example generated stories.