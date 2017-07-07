from flask import Flask
from flask import request
from pprint import pprint

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    pprint(request.values.to_dict())
    return "DOne with it"

if __name__ == '__main__':
    app.run()
