from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api

import base64
import random

from scan_text import ocr, whiteify

app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/play")
def play():
    return render_template("game.html")


class SaveImage(Resource):
    def post(self):
        data = request.json
        image_data = data.get("image")
        if image_data:
            image_data = image_data.replace("data:image/png;base64,", "")
            image_path = "static/drawings/test.png"
            with open(image_path, "wb") as f:
                f.write(base64.b64decode(image_data))
            return jsonify({"ocr": "success"})


class GetOCR(Resource):
    def post(self):
        image_path = "static/drawings/test.png"
        whiteify(image_path)
        ocr_text = ocr(image_path)
        print(ocr_text)
        return jsonify({"ocr": ocr_text})


class GiveWord(Resource):
    def post(self):
        path = "static/data/words.txt"
        with open(path, "r") as f:
            words = f.readlines()
        rand_sent = random.sample(words, 1)[0].strip()
        return jsonify({"sentence": rand_sent})


api.add_resource(SaveImage, "/save-image")
api.add_resource(GetOCR, "/get-ocr")
api.add_resource(GiveWord, "/give-word")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
