Date : Dec 28 2025

Just starting the project, for today my main goal would be to just have a board in place. My short term goal is to have a chess board working. Structure it in a way that Player 1 moves, switches to Player 2. And then for the long term have the choice to play against an engine. 

Okay, so by now I have a board with pieces in place. A game loop that tracks move names. I feel like the hard part is done, I think i just need a way to find out if a move is legal or not. 

Date : Dec 29 2025

Yesterday I started work on the input translator. But it only translates the final position, but not the type of piece it is, if it is capturing a piece or not, etc.
So today I will research on the algebraic notation (I think that is what its called) and implement a solution for it.

I encountered an issue where the grid systems were inverted in the translator.py file and board.py. It was simple fix but took a while to figure out.

I worked on a rudimentary move function for the board. It is not a good solution yet, but i just want to see it work for now.

As the project is getting larger and larger I am finding it harder to maintain. The logic feels hard to follow through even though I am trying my best to use OOP principles and functional programming principles. Wonder how much worse it would be if I did not use those.

I also am starting working on the validation of piece moves right now, dont think it will be finished by today though.