from flask import Flask, render_template, jsonify
from task_automation import organize_jpg_files
import os


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_FOLDER = os.path.join(
    BASE_DIR,
    "source_folder"
)

DESTINATION_FOLDER = os.path.join(
    BASE_DIR,
    "destination_folder"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run-automation", methods=["POST"])
def run_automation():

    result = organize_jpg_files(
        SOURCE_FOLDER,
        DESTINATION_FOLDER
    )

    return jsonify(result)


@app.route("/folder-status")
def folder_status():

    os.makedirs(SOURCE_FOLDER, exist_ok=True)
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    source_files = os.listdir(SOURCE_FOLDER)
    destination_files = os.listdir(DESTINATION_FOLDER)

    jpg_files = [
        file
        for file in source_files
        if file.lower().endswith((".jpg", ".jpeg"))
    ]

    return jsonify({
        "source_count": len(jpg_files),
        "destination_count": len(destination_files)
    })


if __name__ == "__main__":
    app.run(debug=True)