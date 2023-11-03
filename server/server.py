from flask import Flask, Response, request , render_template
import logging
import os.path
log_level = logging.ERROR

app = Flask(__name__)
app.config["DEBUG"] = log_level == logging.DEBUG
logging.basicConfig(level = log_level)

def StripHtmlOff(instring):
    if(".html" in instring):
        return str(instring).split(".")[0]
    return str(instring)

@app.route("/")
def idex():
    return render_template("index.html")

@app.route("/<side>")
def side(side = ""):
    side = StripHtmlOff(side)
    print(f"Requested Side: {side}")
    if(side == ""):
        return render_template("index.html")
    if(os.path.isfile(f"./templates/{side}.html")):
        print("Sucseeded")
        return render_template(f"{side}.html")
    print("Failed")
    resp = Response("Side Not Found", status = 404)
    return resp


@app.route("/zeil", methods=['POST'])
def ziel():
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    return render_template("THX.html",**locals())


# run api using flask
app.run()