from flask import Flask, jsonify, request
import os
from src.telemetry import analyze_telemetry

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/upload-page')
def upload_page():
    return '''
    <html>
        <body>
            <h2>Upload CSV</h2>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <input type="submit">
            </form>
        </body>
    </html>
    '''

@app.route('/')
def home():
    return jsonify({"message": "F1 Telemetry Backend Running"})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = analyze_telemetry(filepath)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

