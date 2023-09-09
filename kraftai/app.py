from flask import Flask, request, jsonify, render_template
from scan_text import ocr, whiteify
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')  


# Rest API
@app.route('/save-image', methods=['POST'])
def save_image():
    try:
        data = request.json
        image_data = data.get('image')

        if image_data:

            image_data = image_data.replace('data:image/png;base64,', '')

            image_path = 'static/drawings/test.png'

            with open(image_path, 'wb') as f:
                import base64
                f.write(base64.b64decode(image_data))
            whiteify(image_path)
            ocr_text = ocr(image_path)
            print(ocr_text)
            return jsonify({"ocr": ocr_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000) 
