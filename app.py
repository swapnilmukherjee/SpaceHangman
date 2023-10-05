from flask import Flask, render_template, request, redirect, url_for
import random
import requests

app = Flask(__name__)

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

current_word = ""
guessed_word = ""
max_attempts = 6
attempts_left = max_attempts
hint = None

def start_new_game():
    global current_word, guessed_word, attempts_left, hint
    current_word = random.choice(words)
    guessed_word = "_ " * len(current_word)
    attempts_left = max_attempts
    hint = None

def fetch_meaning(word):
    url = f"https://api.datamuse.com/words?sp={word}&md=d"
    response = requests.get(url)
    json_response = response.json()
    if json_response and 'defs' in json_response[0]:
        return json_response[0]['defs'][0].split("\t")[1]
    return None

@app.route("/")
def index():
    global hint
    return render_template("index.html", guessed_word=guessed_word, attempts_left=attempts_left, hint=hint)

@app.route("/guess", methods=["POST"])
def guess():
    global guessed_word, attempts_left, hint
    hint = None  # Clear the hint after a guess is made

    if request.method == "POST":
        guessed_letter = request.form["guess"].strip().lower()

        # Check if the user actually entered a letter
        if not guessed_letter or len(guessed_letter) != 1:
            return redirect(url_for("index"))

        # Build a new version of guessed_word with the guessed letter filled in
        new_guessed_word = []
        for idx, letter in enumerate(current_word):
            if letter == guessed_letter or guessed_word[idx*2] != "_":
                new_guessed_word.append(letter)
            else:
                new_guessed_word.append("_")
        guessed_word = " ".join(new_guessed_word)

        # If the guessed letter is not in the current word, decrement attempts
        if guessed_letter not in current_word:
            attempts_left -= 1

        # Check game status
        if "_" not in guessed_word:
            return render_template("win.html", word=current_word)
        elif attempts_left == 0:
            return render_template("lose.html", word=current_word)

    return redirect(url_for("index"))

@app.route("/hint", methods=["POST"])
def get_hint():
    global hint
    hint = fetch_meaning(current_word)
    return redirect(url_for("index"))

@app.route("/play_again", methods=["POST"])
def play_again():
    start_new_game()
    return redirect(url_for("index"))

if __name__ == "__main__":
    start_new_game()
    app.run(debug=True)