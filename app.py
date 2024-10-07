from flask import Flask, render_template, request
from src.scene_segmentation import segment_text
from src.image_generation import generate_images
from src.input_handling import validate_story_and_scenes
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/generated-stories")
def generated_stories():
    return render_template('generated-stories.html');

@app.route('/generate', methods=['POST'])
def generate():
    try:
        description = request.form['description']
        num_scenes = int(request.form['num_scenes'])
        scene_size = request.form['scene_size']
        print(scene_size)

        can_be = validate_story_and_scenes(description, num_scenes)

        if can_be == 'False':
            return render_template('results.html', alert="Error: Story cannot be divided into the requested number of scenes.", data={"data": []}), 400

        # Try segmenting the text into scenes
        scenes = segment_text(description, num_scenes)
        if scenes is None:
            return render_template('results.html', alert="Error: Unable to segment the text into scenes.", data={"data": []}), 500

        # Strip the whitespace and newlines, then manually convert to a list using string splitting
        scene_list = scenes.strip().strip("[]").split("\n")

        # Remove any extra quotes or spaces
        scene_list = [scene.strip().strip('"') for scene in scene_list if scene.strip()]

        data = {
            "data": []
        }

        # Try generating images for the scenes
        images = generate_images(scene_list, scene_size)

        if not images:
            return render_template('results.html', alert="Error: Image generation failed.", data={"data": []}), 500

        # Populate the data with the scenes and their corresponding images
        for i, scene in enumerate(scene_list):
            data["data"].append({
                "scene": scene,
                "image": images[i] if images[i] else "Image generation error"
            })

        return render_template('results.html', data=data)
    
    except Exception as e:
        print(f"Error in /generate: {str(e)}")
        return render_template('results.html', alert=f"An error occurred: {str(e)}", data={"data": []}), 500

if __name__ == '__main__':
    app.run(debug=True)
