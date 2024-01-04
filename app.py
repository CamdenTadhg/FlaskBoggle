from boggle import Boggle
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'requin'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()
























# read through boggle.py and do your best to understand it. 
# create necessary routes for start page and game board
# create static folder with css, javascript, and testing files
# create main template with appropriate links for static files
# create start page
# use Jinja to display boggle board on main page
# save board to session
# create form to enter guess
# use jquery to pull data from guess form
# post guess to server using axios/ajax without refreshing page
# on the server, check that it is a valid word in the dictionary
# check that the word is a valid word on the currnt board (check_valid_word function)
# use jsonify function to respond to ajax request with json of dictionary
# display feedback on guess for user on front end
# create function to track score
# create display for score and update appropriately
# create timer to only allow 60 seconds of play time
# disable future guesses when 60 seconds has passed
# display countdown timer
# send Ajax request to server upon game end with score and increment on number of times played (use request.json)
     # use pdb to set a breakpoint and examine request.json. it's structure is different
# redesign front end to be object oriented
# ensure docstrings fora ll view functions
# handle duplicate words so that the same word cannot be submitted twice
# refactor anything else you can think of. 
# style application
# create option to determine size of board (will require a form on the start page)
# create a hint feature which will highlight the first couple characters in a valid word that the user hasn't discovered yet
    #I think this uses the find and find_from functions. 

# January 4, 2024 - 