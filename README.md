# Chess-Project

Core Components
Game State Management The system represents the chessboard as an 8x8 two-dimensional vector. Individual pieces are instantiated as objects inheriting from a base piece class. This structure maintains the physical locations and properties of all entities on the board.

Turn Control The execution flow is managed by a central game loop that alternates between players. It tracks active turns and maintains a comprehensive history of all moves performed during the session.

Input Processing A dedicated utility module handles the translation of algebraic chess notation into grid-based coordinates. This component utilizes hash mapping to convert file characters into integer indices and extracts rank information through string manipulation.

Implementation Details
Board Indexing The board is indexed using a [row][col] format. In this configuration, the first index represents the rank (vertical position) and the second index represents the file (horizontal position).

Data Structures

2D List: Primary grid for piece placement and board representation.

Class Inheritance: Hierarchical structure for piece types.

Hash Maps: Used for coordinate translation within the functional processing layer.

List: Move history tracking.

Future Development
The project is prepared for the integration of movement execution and piece-specific validation logic. The separation of the parser from the core board logic allows for independent testing of coordinate math before integration with the move execution methods.
