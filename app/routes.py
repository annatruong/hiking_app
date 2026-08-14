from app import app
from flask import render_template, redirect, session, url_for
from .forms import HikeForm
from calculation import get_hike_estimation


@app.route("/", methods=["GET","POST"])
def home():
    form = HikeForm()
    
    # if user submitted form, get/calculate data and store in session, then redirect to same page
    if form.validate_on_submit():
        session["ascent"] = form.ascent.data
        session["distance"] = form.distance.data
        session["results"] = get_hike_estimation(form.ascent.data,form.distance.data)
        
        return redirect(url_for("home"))
    
    results = session.pop("results", None)
    ascent = session.pop("ascent", None)
    distance = session.pop("distance", None)
    form.ascent.data = ascent
    form.distance.data = distance
    
    return render_template("index.html", 
        form=form, 
        ascent=ascent, 
        distance=distance, 
        results=results)