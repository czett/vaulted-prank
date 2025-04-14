from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("sharing.html")

if __name__ == "__main__":
    app.run(debug=True, port=5050)

#dSCB69#0|H%=