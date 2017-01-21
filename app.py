from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app
#default home page
@app.route("/")
def hello():
    return render_template("hello.html")

#floor map updates
@app.route("/nofire")
def nofire():
    return render_template("nofire.html")

@app.route("/nopeople")
def nopeople():
    return render_template("nopeople.html")

@app.route("/oneperson")
def oneperson():
    return render_template("oneperson.html")

@app.route("/twopeople")
def twopeople():
    return render_template("twopeople.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
