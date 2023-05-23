```python
from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, db_session
from voters import Voter, add_voter, update_voter, delete_voter, get_all_voters
from requests import VoterRequest, add_request, update_request, delete_request, get_all_requests
from map_view import get_voters_in_radius
from auth import login_required

app = Flask(__name__)
app.secret_key = "supersecretkey"
init_db()

@app.route("/")
@login_required
def index():
    return render_template("voters_list.html", voters=get_all_voters())

@app.route("/voters/add", methods=["POST"])
@login_required
def add_voter_route():
    add_voter(request.form)
    flash("Voter added successfully", "success")
    return redirect(url_for("index"))

@app.route("/voters/update", methods=["POST"])
@login_required
def update_voter_route():
    update_voter(request.form)
    flash("Voter updated successfully", "success")
    return redirect(url_for("index"))

@app.route("/voters/delete/<int:voter_id>")
@login_required
def delete_voter_route(voter_id):
    delete_voter(voter_id)
    flash("Voter deleted successfully", "success")
    return redirect(url_for("index"))

@app.route("/requests")
@login_required
def requests_list():
    return render_template("requests_list.html", requests=get_all_requests())

@app.route("/requests/add", methods=["POST"])
@login_required
def add_request_route():
    add_request(request.form)
    flash("Request added successfully", "success")
    return redirect(url_for("requests_list"))

@app.route("/requests/update", methods=["POST"])
@login_required
def update_request_route():
    update_request(request.form)
    flash("Request updated successfully", "success")
    return redirect(url_for("requests_list"))

@app.route("/requests/delete/<int:request_id>")
@login_required
def delete_request_route(request_id):
    delete_request(request_id)
    flash("Request deleted successfully", "success")
    return redirect(url_for("requests_list"))

@app.route("/map")
@login_required
def map_view():
    return render_template("map_view.html", voters=get_all_voters())

@app.route("/map/filter", methods=["POST"])
@login_required
def map_filter():
    location = request.form["location"]
    radius = float(request.form["radius"])
    filtered_voters = get_voters_in_radius(location, radius)
    return render_template("map_view.html", voters=filtered_voters)

if __name__ == "__main__":
    app.run(debug=True)
```