import Game

def playGame(playerLetter, computerLetter):
    game= Game(playerLetter,computerLetter)
    while True:
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                # Player’s turn.
#                drawBoard(theBoard)
#                move = getPlayerMove(theBoard)
                game.makeMove(game.board, playerLetter, move)
                if game.isWinner(game.board, playerLetter):
#                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if game.isBoardFull(game.board):
#                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer’s turn.
                move = game.getComputerMove(game.board, computerLetter)
                game.makeMove(game.board, computerLetter, move)
                if game.isWinner(game.board, computerLetter):
#                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if game.isBoardFull(game.board):
#                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'