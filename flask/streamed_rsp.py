from flask import Flask, Response, request

app = Flask(__name__)

def reader():
    with open("sample.csv", "r", encoding="latin1") as fobj:
        for line in fobj:
            yield line

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return Response(reader())
    elif request.method == "POST":
        ## Read the data from the input stream as below
        #print(request.input_stream.readline())
        #print(request.input_stream.readline())
        #print(request.input_stream.readline())
        #request.input_stream.close()
        return Response("Got the state")


if __name__ == '__main__':
    app.run(threaded=True)

# How to upload the huge file data background
"""
def fgn():
    yield "hello".encode()
    yield "hi\ntherea you are\n got it".encode()

## Here data could be any iteerator/generator

rsppost = requests.post("http://127.0.0.1:5000/", data=fgn(), stream=True)
"""
