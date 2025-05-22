from flask import Flask, render_template, request
import requests


app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submittodoitem", methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post("http://127.0.0.1:9000//submittodoitem", json=form_data)
    return "Data submission successful"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)
