#! /usr/bin/env /usr/bin/python

import flask
app = flask.Flask(__name__)

#@app.route('/')
#def index():
#    return "Index Page"

@app.route('/main/')
def main():
    return "Hello world!!!!"


if __name__ == '__main__':
    app.run()
