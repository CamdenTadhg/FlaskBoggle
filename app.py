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

@app.route('/gameover', methods = ['POST'])
def update_stats():
    """update game play stats in the session"""
    data = request.get_json()
    current_score = data['score']
    high_score = session.get('high_score', 0)
    if current_score > high_score:
        session['high_score'] = current_score
    session['games_played'] = session.get('games_played', 0) + 1
    print('************************')
    print('High score is ', session['high_score'])
    print('Games played is ', session['games_played'])
    return jsonify({'result': 'score logged'})


# 11 deal with what happens if you hit submit without entering a word
# 10 write tests for all javascript functions
# 9 refactor anything else you can think of. 
# 8 style application including different size screens
# 7 create option to determine size of board (will require a form on the start page and a change to the boggle.py file)
# 5 write tests for new functionality
# 4 create a hint feature which will highlight the first couple characters in a valid word that the user hasn't discovered yet
# 3 write tests for new functionality
# 2 run all tests
# 1 remove console.log, print, and other testing features


# January 4, 2024 - 