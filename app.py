from boggle import Boggle
from flask import Flask, render_template
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
    return render_template('gameboard.html')





# 1create start page
# 2is it time to write tests? 
# 3use Jinja to display boggle board on game board page
# 4is it time to write tests? 
# 5save board to session
# 6is it time to write tests? 
# 7create form to enter guess
# 8is it time to write tests? 
# 9use jquery to pull data from guess form
# 10is it time to write tests? 
# 11post guess to server using axios/ajax without refreshing page
# 12is it time to write tests? 
# 13on the server, check that it is a valid word in the dictionary
# 14is it time to write tests? 
# 15check that the word is a valid word on the currnt board (check_valid_word function)
# 16is it time to write tests? 
# 17use jsonify function to respond to ajax request with json of dictionary
# 18is it time to write tests? 
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