from flask import Flask, render_template, request, redirect, url_for, session
import random
import requests

app = Flask(__name__)
app.secret_key = 'GiveUsFullMarksPleaseeeeeeee'  # A secret key is required for the session to work

words = [
    "astronomy", "universe", "galaxy", "meteor", "telescope", "satellite", "star", "planet",
    "orbit", "comet", "asteroid", "cosmos", "blackhole", "nebula", "constellation", "eclipse",
    "gravity", "moon", "sun", "mars", "venus", "jupiter", "saturn", "neptune", "uranus",
    "mercury", "pluto", "milkyway", "interstellar", "solarsystem", "lightyear", "spaceship",
    "quasar", "pulsar", "supernova", "cosmic", "vacuum", "extraterrestrial", "astronaut",
    "observatory", "spectrum", "radiation", "magnetism", "parallax", "lunar", "solar",
    "equinox", "solstice", "luminosity", "magnitude", "orbit", "trajectory", "celestial",
    "zenith", "nadir", "spacecraft", "shuttle", "cosmology", "exoplanet", "aliens", "wormhole",
    "gamma", "ray", "flare", "spiral", "ellipse", "galactic", "helium", "hydrogen", "nucleus",
    "electron", "proton", "neutron", "darkmatter", "darkenergy", "dwarf", "giant", "ejecta",
    "tidal", "binary", "singularity", "photosphere", "corona", "chromosphere", "rotation",
    "revolution", "apogee", "perigee", "spacestation", "oort", "kuiper", "hubble", "spectroscope"
]

max_attempts = 6

def start_new_game():
    session['current_word'] = random.choice(words)
    session['guessed_word'] = "_ " * len(session['current_word'])
    session['attempts_left'] = max_attempts
    session['hint'] = None

def fetch_meaning(word):
    url = f"https://api.datamuse.com/words?sp={word}&md=d"
    response = requests.get(url)
    json_response = response.json()
    if json_response and 'defs' in json_response[0]:
        return json_response[0]['defs'][0].split("\t")[1]
    return None

@app.route("/")
def index():
    # If the game hasn't started yet, initialize it
    if 'current_word' not in session:
        start_new_game()
    return render_template("index.html", guessed_word=session['guessed_word'], attempts_left=session['attempts_left'], hint=session['hint'])

@app.route("/guess", methods=["POST"])
def guess():
    guessed_letter = request.form["guess"].strip().lower()
    # Check if the user actually entered a letter
    if not guessed_letter or len(guessed_letter) != 1:
        return redirect(url_for("index"))

    new_guessed_word = []
    for idx, letter in enumerate(session['current_word']):
        if letter == guessed_letter or session['guessed_word'][idx*2] != "_":
            new_guessed_word.append(letter)
        else:
            new_guessed_word.append("_")
    session['guessed_word'] = " ".join(new_guessed_word)

    # If the guessed letter is not in the current word, decrement attempts
    if guessed_letter not in session['current_word']:
        session['attempts_left'] -= 1

    # Check game status
    if "_" not in session['guessed_word']:
        return render_template("win.html", word=session['current_word'])
    elif session['attempts_left'] == 0:
        return render_template("lose.html", word=session['current_word'])

    return redirect(url_for("index"))

@app.route("/hint", methods=["POST"])
def get_hint():
    session['hint'] = fetch_meaning(session['current_word'])
    return redirect(url_for("index"))

@app.route("/play_again", methods=["POST"])
def play_again():
    start_new_game()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
