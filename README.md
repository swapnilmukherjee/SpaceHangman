# Space Hangman 🌌

Welcome to Space Hangman - a galactic twist on the classic game of Hangman! Dive into the universe and test your knowledge of space-themed words.

[Play the game here!](http://swapnilmukherjee.pythonanywhere.com)

[Watch the game demo on YouTube.](https://youtu.be/JxDZO2PMoBQ)

## Game Objective and Rules 🎯

**Objective**: Guess the space-themed word before running out of attempts!

**Rules**:
1. Players are presented with blank spaces representing the letters of a word.
2. Guess a letter by entering it into the input box.
3. If the letter is in the word, it appears in the correct spaces.
4. For each incorrect guess, the number of attempts decreases.
5. Use the "Hint" button if stuck.
6. Win by guessing the word correctly before attempts run out.

## Technologies Used 🛠

- **Python/Flask**: Backend framework to serve the game.
- **HTML/CSS**: For structuring and styling the game interface.
- **JavaScript**: Adds interactivity, enhancing user experience.

## Setup and Deployment ⚙️

1. Clone this repository: `git clone https://github.com/swapnilmukherjee/Space-Hangman.git`
2. Navigate to the project directory: `cd Space-Hangman`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the game: `python app.py`
5. Open a web browser and visit `http://127.0.0.1:5000/` to play.

## Credits and Third-party Assets 🙏

- **Background Video**: Canva
- **Ambient Music**: YouTube NCS
- **Word Definitions API**: Datamuse API 

## Reflection on Design and Development 🌟

Building Space Hangman was a journey filled with learning and discovery. From conceptualizing the game to deploying the final product, every stage posed unique challenges and opportunities.

One of the challenges we faced was ensuring the game maintained a balance between being too easy and too hard. By leveraging a comprehensive space-themed word list and allowing hints, we aimed to keep players engaged and challenged, without causing undue frustration.

A crucial decision was to adopt Flask for the backend, which enabled quick iterations and rapid development. The introduction of JavaScript provided an interactive dimension to the gameplay, making it more dynamic and engaging. Furthermore, integrating an external API for word definitions added a layer of depth to the gameplay, offering players an educational dimension.

In terms of what didn't work, we initially considered adding more interactive elements like disappearing hints, an animated hangman figure, etc., using JavaScript. However, we deferred this enhancement for future iterations due to time constraints and a desire to maintain a straightforward user experience.

Among the lessons learned, the importance of user feedback stood out. Early testers of the game provided invaluable insights, leading to crucial modifications, particularly in the UI design.

In conclusion, Space Hangman is a testament to the power of collaboration, iterative development, and feedback. It serves as a reminder that even simple games can offer profound lessons in software development.

## Contributors 🙌

- [Swapnil Mukherjee](https://github.com/swapnilmukherjee)
- Jayanth Kodur
- Sandya Rani Prasadam
