from flask import Flask, jsonify
import time

app = Flask(__name__)


data = {
        "Hello" : 123,
        "hi"    : 345,
        "hey"   : 456 
       }

languages = [   {"language" : "Python"},
            {"language" : "JavaScript"},
            {"language" : "Go"}
        ]

@app.route("/")
def main():
    time.sleep(.75)
    return jsonify(data)

@app.route("/langs")
def langs():
    time.sleep(.5)
    return jsonify(languages)

if __name__ == '__main__':
    app.run("0.0.0.0", 9876)
