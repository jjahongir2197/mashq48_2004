from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = ""

    if request.method == "POST":

        text = request.form.get("text")

        result = len(text)

    return render_template("index.html", result=result)

app.run(debug=True)
