from boggle import Boggle
from flask import Flask, render_template, session, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'requin'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def display_start():
    """Return a start page for Boggle game"""
    return render_template('start.html')

@app.route('/boggle')
def play_boggle():
    """Return a page showing a boggle game board"""
    game_board = boggle_game.make_board()
    session['game_board'] = game_board
    return render_template('gameboard.html', game_board = game_board)

@app.route('/guess', methods = ['POST'])
def check_guess():
    """check if the submitted guess is valid"""
    data = request.get_json()
    guess = data['guess']
    result = boggle_game.check_valid_word(session['game_board'], guess)
    return jsonify({'result': result})

# create display for score and update appropriately
     #current stuck on why my update score function isn't being called properly
# create timer to only allow 60 seconds of play time
# disable future guesses when 60 seconds has passed
# display countdown timer
# send Ajax request to server upon game end with score and increment on number of times played (use request.json)
     # use pdb to set a breakpoint and examine request.json. it's structure is different
# redesign front end to be object oriented
# ensure docstrings for all view functions
# handle duplicate words so that the same word cannot be submitted twice
# refactor anything else you can think of. 
# style application including different size screens
# create option to determine size of board (will require a form on the start page)
# create a hint feature which will highlight the first couple characters in a valid word that the user hasn't discovered yet
# WRITE TESTS!!
# run all tests again
# remove console.log and other testing features


# January 4, 2024 - 