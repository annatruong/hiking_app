from flask import Flask, render_template
from config import Config
from forms import HikeForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/", methods=["GET","POST"])
def home():
    form = HikeForm()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)