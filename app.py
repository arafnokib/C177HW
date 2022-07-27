from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 56,
        "category": "Sports",
        "word": "Soccer"
    },
    {
        "inputs": 7,
        "category": "American State",
        "word": "Ilinois"
    },

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
