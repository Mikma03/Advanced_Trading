from flask import Flask, render_template, request, jsonify
import subprocess
import json
from utils import clear_data_json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/execute", methods=["POST"])
def execute():
    input_data = request.json["input_data"]

    # Execute the zsh script and provide input data
    process = subprocess.Popen(
        ["zsh", "process_records.zsh"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
    )
    stdout, _ = process.communicate(json.dumps(input_data) + "\n")
    process.wait()

    # Return the output captured from the zsh script
    return jsonify({"status": "success", "output": stdout})

@app.route('/clear', methods=['POST'])
def clear():
    clear_data_json()
    return "Data cleared", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
