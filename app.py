from flask import Flask, render_template, request, send_file, url_for
import os
from rembg import remove
from PIL import Image

app = Flask(__name__)

# Ensure the 'static' folder exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            input_path = os.path.join('static', 'uploaded.png')
            output_path = os.path.join('static', 'output.png')
            file.save(input_path)
            # Remove the background
            input_image = Image.open(input_path)
            output_image = remove(input_image)
            output_image.save(output_path)
            return render_template('results.html', 
                                   original_image=url_for('static', filename='uploaded.png'), 
                                   output_image=url_for('static', filename='output.png'))
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_file('static/output.png', as_attachment=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
