#Chess-Functional-OOP
Minimalist chess implementation built on a hybrid functional/OOP architecture.

Core Architecture
State The system uses OOP to manage the board state. An 8x8 2D array stores piece objects, mapping Rank 1 to index 0 and File A to index 0.

Logic Input parsing is handled through functional programming. Pure functions translate algebraic notation into grid coordinates using hash maps for constant-time lookup.
