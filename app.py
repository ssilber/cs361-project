from flask import Flask, jsonify, render_template, request, redirect, url_for

from common import clubs

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        club_submitted = request.form.get("club")
        return redirect(url_for("selected_club", club_submitted=club_submitted))

    return render_template("index.j2", clubs=clubs)


@app.route("/club/<club_submitted>")
def selected_club(club_submitted):

    club_object = None
    for club in clubs:
        if club.name == club_submitted:
            club_object = club
    return render_template("club.j2", club=club_object)


@app.route("/api/clubs")
def api():
    return jsonify(clubs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
