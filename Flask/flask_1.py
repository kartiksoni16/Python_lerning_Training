from flask import Flask

app = Flask(__name__)  # Initialize Flask app

@app.route('/iser')  # Define route for home page
def home():
    return "Hello, Welcome to Flask!"  # Response


@app.route('/Ks')  # Define route for home page
def m():
    return "Hi,. I am Sony kartik"


if __name__ == '__main__':
    app.run(debug=True) 