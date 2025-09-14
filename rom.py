from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('ram.html')

@app.route('/upload', methods=['POST'])
def get_data():

    file = request.files['file']

    print("This is what it contains :", request.files)
    print("file :", file)

    if file.filename.endswith('.csv'):
        path = "userfile/" + file.filename
        file.save(path)
        return "We have receive your file"
    
    else:
        return "upload a CSV file only."

if __name__ == '__main__':
    app.run(debug=True) 


import os

@app.route('/upload', methods=['POST'])
def get_data():
    file = request.files['file']

    # make sure folder exists
    upload_folder = "userfile"
    os.makedirs(upload_folder, exist_ok=True)

    path = os.path.join(upload_folder, "industry.csv")
    file.save(path)

    return "File uploaded successfully!"
