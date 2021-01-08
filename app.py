# Reference https://www.twilio.com/blog/2016/09/fun-with-markov-chains-python-and-twilio-sms.html

import markovify
import twilio.twiml
from flask import Flask, request, redirect


app = Flask(__name__)

@app.route("/random_message", methods=['GET', 'POST'])
def random_message():
	trump_response = model.make_short_sentence(100)
	return str(trump_response)

if __name__ == "__main__":
    with open("tweets.csv") as f:
        text = f.read()

    model = markovify.Text(text)
    app.run(debug=True)