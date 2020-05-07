from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
@app.route("/<message>")
def index(message):
    sentiment = "postive"
    if TextBlob(message).sentiment.polarity < 0.0:
        sentiment = "negative"

    return app.make_response(f"<h1>{sentiment}</h1>")


#!###############################################
if __name__ == '__main__':
    app.run(debug=True)
