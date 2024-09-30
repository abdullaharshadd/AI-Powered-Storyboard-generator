from flask import Flask, render_template, request
from src.scene_segmentation import segment_text
from src.image_generation import generate_images
import json
# import nltk
# nltk.download('punkt_tab')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.form['description']
    num_scenes = int(request.form['num_scenes'])
    scenes_height = int(request.form["scenes_height"])
    scenes_width = int(request.form["scenes_width"])

    scenes = segment_text(description, num_scenes)
    
    # Strip the whitespace and newlines, then manually convert to a list using string splitting
    scene_list = scenes.strip().strip("[]").split("\n")

    # Remove any extra quotes or spaces
    scene_list = [scene.strip().strip('"') for scene in scene_list if scene.strip()]

    data = {
        "data" : []
    }

    if scenes_height is not None and scenes_width is not None:
        images = generate_images(scene_list, str(scenes_height) + "x" + str(scenes_width))
        data["scenes_width"] = scenes_width
        data["scenes_height"] = scenes_height
    else:
        images = generate_images(scene_list)
        data["scenes_width"] = 400
        data["scenes_height"] = 400

    i = 0
    length = len(scene_list)

    while i < length:
        data["data"].append({
            "scene" : scene_list[i],
            "image" : images[i],
        })
        i += 1

    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
