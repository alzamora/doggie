import os
from model import predict, prepare_image
from flask import Flask, render_template, request
app = Flask(__name__)
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROUTE, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file = request.files.getlist("file")[0]
    filename = file.filename
    destination = "/".join([target, filename])
    print(destination)
    file.save(destination)

    result = predict(destination)
    print(result)
    return render_template("complete.html", prediction=result)


if __name__ == "__main__":
    app.run(port=4555, debug=True)