from flask import Flask, render_template, request, redirect
from config import Config
from forms import HikeForm
from calculation import get_hike_estimation


app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=["GET","POST"])
def home():
    form = HikeForm()
    if form.validate_on_submit():
        results = get_hike_estimation(form.ascent.data,form.distance.data)

        return render_template("index.html", form=form, ascent=form.ascent.data, distance=form.distance.data, results=results)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)