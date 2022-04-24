from flask import Flask, render_template, request, redirect

from common import clubs

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.j2", clubs=clubs)


@app.route("/club/", methods=["POST", "GET"])
def selected_club():
    if request.method == "POST":
        club_submitted = request.form.get("club")
        club_object = None
        for club in clubs:
            if club.name == club_submitted:
                club_object = club
        return render_template("club.j2", club=club_object)

    if request.method == "GET":
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
