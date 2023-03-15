"""Contains routing logic for boggle game"""
# Import neccesary packages and debugger 
from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


# Set file as application file, turn debugger on
app = Flask(__name__)

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'BoggleGameKey'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def render_board():
    """Render the index.html template and display the board"""
    board = boggle_game.make_board()
    # Add board to session
    session["board"] = board 
    
    # history = session.get("scores", [])
    # session["scores"] = history
    
    return render_template("index.html", board=board)
    