"""Contains routing logic for boggle game"""
# Import neccesary packages and debugger 
from flask import Flask, render_template, session, request, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
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
    
    history = session.get("scores", [])
    session["scores"] = history
    
    return render_template("index.html", board=board, history=history)
    
@app.route("/findword")
def find_word():
    """Check the word submitted and return the result"""
    word = request.args.get("word", "")
    
    return jsonify(result = boggle_game.check_valid_word(session["board"], word))

@app.route("/endgame", methods=["POST"])
def end_game():
    """End the game and display the score from the html file"""
    
    scores = session.get("scores", [])
    scores.append({"time": datetime.now(), "score":request.json.get("score", 0)})
    session["scores"] = scores

    return jsonify(scores)