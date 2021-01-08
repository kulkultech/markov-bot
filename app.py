# Reference https://www.twilio.com/blog/2016/09/fun-with-markov-chains-python-and-twilio-sms.html

import markovify
import random
from get_tweets import get_all_tweets, write_tweets_to_csv
from flask import Flask, request, redirect


app = Flask(__name__, static_url_path='', static_folder='templates')

tweets = get_all_tweets()
write_tweets_to_csv(tweets)

with open("tweets.csv") as f:
    text = f.read()
    model = markovify.Text(text)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route("/random_message", methods=['GET', 'POST'])
def random_message():
	trump_response = model.make_short_sentence(100)
	return str(trump_response)


@app.route("/interactive_message", methods=['GET', 'POST'])
def interactive_message():
	trump_response = None

	user_question = request.args.get('inquiry')
	word_list = user_question.split(' ')
	random_word = random.choice(word_list)

	print(word_list)
	print(random_word)

	try:
		trump_response = model.make_sentence_with_start(random_word, strict=False)
	except Exception:
		trump_response = model.make_short_sentence(100)

	return str(trump_response)


if __name__ == "__main__":
    app.run(debug=True)