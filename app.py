from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🥾 HIKING APP 🥾</h1><br><p>Gradient • Climb • Difficulty Rating</p><br><p>How steep is your adventure?</p>"


if __name__ == "__main__":
    app.run()