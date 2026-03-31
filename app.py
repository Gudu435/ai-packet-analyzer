from flask import Flask, render_template, request
import os
from analyzer import analyze_pcap

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        print("FILES:", request.files)

        if "pcap" not in request.files:
            result = "No file selected"
        else:
            file = request.files["pcap"]

            if file.filename == "":
                result = "No file selected"
            else:
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)

                result = analyze_pcap(file_path)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
