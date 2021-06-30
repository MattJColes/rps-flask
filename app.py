# Using gunicorn "gunicorn --bind 0.0.0.0:8080 wsgi:app"
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
PORT = 8080

title = 'Rock, paper, scissors'
computer_choice_options = ['🪨', '📜', '✂️']

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    return render_template('index.html', title = title)

@app.route('/', methods = ['POST'])
def result():
    choice = request.form['choice']
    computer_choice = random.choice(computer_choice_options)
    if choice == computer_choice:
        outcome = "You tied with the computer"
    elif choice == "🪨" and computer_choice == "📜" or choice == "📜" and computer_choice == "✂️" or choice == "✂️" and computer_choice == "🪨":
        outcome = "You lost to the computer"
    else: outcome = "You won over the computer"
    return render_template('result.html', title = title, choice = choice, computer_choice = computer_choice, outcome = outcome)

if __name__ == '__main__':
   app.run(debug = False, host="0.0.0.0", port=PORT)