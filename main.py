from flask import Flask, jsonify, render_template

app = Flask(__name__)

#@app.route('/')
#def home():
#    return "Welcome to the Website"

@app.route('/about')
def about():
    return """<h1>About Us</h1><br>
              <h2>The mental activity of forming ideas, opinions, beliefs, and the resulting mental construct themselves</h2>
              <h3>Thank you visting my website.</h3>"""

@app.route('/data')
def data():
    user_data = {"Name": "Darshika",
                 "Age": "19",
                 "hobbies": "Badminton"}
    return jsonify(user_data)

#@app.route('/index')
#def home_page():
#    Name = "darshika"
#    return render_template('index.html', Name=Name)

#@app.route('/', methods=['GET'])
#def home():
#    return "Hello World!"

@app.route('/', methods=['GET'])
def form():
    return render_template("form.html")

@app.route('/form', methods=['GET'])
def welcome():
    return "We have received your information."

    

if __name__ == '__main__':
    app.run(debug=True) 
