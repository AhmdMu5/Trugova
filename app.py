from flask import Flask, render_template, request
from predict import load, predict

app = Flask (__name__)

load()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction = predict(text)
    return render_template('index.html', text=text, result=prediction)

if __name__ == "__main__":
    app.run(debug=True)