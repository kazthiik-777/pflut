from flask import Flask

app = Flask(name)

@app.route("/")
def home():
    return "Hello, Flask!"

if name == "main":
    app.run(debug=True)