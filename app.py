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
    print(session['game_board'])
    result = boggle_game.check_valid_word(session['game_board'], guess)
    return jsonify({'result': result})

# 18write tests for /guess route and axios app 
# 19display feedback on guess for user on front end
# 20is it time to write tests? 
# 21create function to track score
# 22is it time to write tests? 
# 23create display for score and update appropriately
# 24is it time to write tests? 
# 25create timer to only allow 60 seconds of play time
# 26is it time to write tests? 
# 27disable future guesses when 60 seconds has passed
# 28is it time to write tests? 
# 29display countdown timer
# 30is it time to write tests? 
# 31send Ajax request to server upon game end with score and increment on number of times played (use request.json)
     # use pdb to set a breakpoint and examine request.json. it's structure is different
# 32is it time to write tests? 
# 33redesign front end to be object oriented
# 34is it time to write tests? 
# 35ensure docstrings for all view functions
# 36is it time to write tests? 
# 37handle duplicate words so that the same word cannot be submitted twice
# 38is it time to write tests? 
# 39refactor anything else you can think of. 
# 40is it time to write tests? 
# 41style application
# 42is it time to write tests? 
# 43create option to determine size of board (will require a form on the start page)
# 44is it time to write tests? 
# 45create a hint feature which will highlight the first couple characters in a valid word that the user hasn't discovered yet
# 46is it time to write tests? 


# January 4, 2024 - 