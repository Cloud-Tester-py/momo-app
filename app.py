from flask import Flask
# from textblob import TextBlob

app = Flask(__name__)


@app.route('/')
# @app.route('/<msg>')
def indix(): 
    # sentiment = "positive"
    # if TextBlob(msg).sentiment.polarity < 0.0:
    #     sentiment ="negative"
    # # return app.make_response(f"<h1> {sentiment} </h1>")
    return "deployed to Heroku"







#!###############################################
if __name__ == '__main__':
    app.run(debug=True)