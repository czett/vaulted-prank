from flask import Flask, request, render_template, redirect, session, send_from_directory
import funcs

app = Flask(__name__)
app.secret_key = "gvjkfblkejgboidhvg"

@app.route("/")
def start():
    downloaded = False
    if session.get("name"):
        name = session["name"]
        if session.get("downloaded"):
            downloaded = session["downloaded"]
        else:
            downloaded = False
    else:
        name = None

    names = funcs.get_all_available_names()

    return render_template("sharing.html", downloaded=downloaded, names=names, name=name)

@app.route("/unlock", methods=["POST"])
def unlock():
    name = request.form["name"]
    session["name"] = name
    session["downloaded"] = False

    funcs.set_downloaded_true(name)

    return redirect("/")

@app.route("/wipe")
def wipe():
    session.clear()

    return redirect("/")

@app.route("/download")
def download():
    return send_from_directory(
        directory="static",
        path="shotsizes.pdf",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True, port=5050, host="0.0.0.0")