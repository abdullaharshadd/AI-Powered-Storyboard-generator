from flask import Flask, render_template, request
from src.scene_segmentation import segment_text
from src.image_generation import generate_images
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        description = request.form['description']
        num_scenes = int(request.form['num_scenes'])
        scenes_height = int(request.form["scenes_height"])
        scenes_width = int(request.form["scenes_width"])

        # Try segmenting the text into scenes
        scenes = segment_text(description, num_scenes)
        if scenes is None:
            return "Error: Unable to segment the text into scenes.", 500

        # Strip the whitespace and newlines, then manually convert to a list using string splitting
        scene_list = scenes.strip().strip("[]").split("\n")

        # Remove any extra quotes or spaces
        scene_list = [scene.strip().strip('"') for scene in scene_list if scene.strip()]

        data = {
            "data": []
        }

        # Try generating images for the scenes
        if scenes_height is not None and scenes_width is not None:
            images = generate_images(scene_list, str(scenes_height) + "x" + str(scenes_width))
            data["scenes_width"] = scenes_width
            data["scenes_height"] = scenes_height
        else:
            images = generate_images(scene_list)
            data["scenes_width"] = 400
            data["scenes_height"] = 400

        if not images:
            return "Error: Image generation failed.", 500

        # Populate the data with the scenes and their corresponding images
        for i, scene in enumerate(scene_list):
            data["data"].append({
                "scene": scene,
                "image": images[i] if images[i] else "Image generation error"
            })

        return render_template('results.html', data=data)
    
    except Exception as e:
        print(f"Error in /generate: {str(e)}")
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
