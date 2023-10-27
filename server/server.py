from flask import Flask, Response, request , render_template
import logging
import os.path
log_level = logging.ERROR

app = Flask(__name__)
app.config["DEBUG"] = log_level == logging.DEBUG
logging.basicConfig(level = log_level)

@app.route("/")
def idex():
    return render_template("index.html")

@app.route("/<side>")
def side(side = ""):
    if(side == ""):
        return render_template("index.html")
    if(os.path.isfile(f"./templates/{side}.html")):
        return render_template(f"{side}.html")
    resp = Response("Side Not Found", status = 404)
    return resp


@app.route("/zeil", methods=['POST'])
def ziel():
    print(f"Data: {request.data}")
    return request.form


# run api using flask
app.run()