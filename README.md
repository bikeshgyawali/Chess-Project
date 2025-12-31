# Chess Project

This chess project is my version of chess in Python. It is a CLI application built with the intent of learning SWE practices and architecture while focusing on something that would be fun to me.

# What I learnt

Modular Architecture: Enforces a clean separation of concerns between board state, piece logic, and user input.

Object-Oriented Design: Utilizes class inheritance for polymorphic piece behavior and maintainable code.

Move Validation: Implements a unction to ensure all moves comply with (basic) standard chess rules.

State-Aware Game Logic: Accurately detects and handles critical game states, including check and checkmate.

Algebraic Notation Parser: Translates standard chess notation into internal board coordinates for gameplay.

# How to run and test

To run:
Navigate to the source directory:
cd src/py

Run the main script:
python3 main.py

To test:
Navigate to the root directory of the project.
Run the test suite:
python3 -m unittest test/test_chess.py

# Areas to improve
While I'm proud of the current state of the project, there is always room for growth. Looking ahead, I have identified several areas for future improvement:

Implement special chess moves such as Castling, En Passant, and Pawn Promotion.
Develop a graphical user interface (GUI) to provide a more visual and user-friendly experience.
Incorporate features like move history, the ability to undo moves, and game saving/loading.
Introduce optional time controls to allow for different modes of play.


