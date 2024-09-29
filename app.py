from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    description = request.form['description']
    num_scenes = int(request.form['num_scenes'])

    scenes = [f"Scene {i+1}: {description}" for i in range(num_scenes)]
    return render_template('results.html', scenes=scenes)

if __name__ == '__main__':
    app.run(debug=True)
