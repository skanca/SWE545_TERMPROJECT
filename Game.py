import random

class Game(object):

    def __init__(self,playerLetter,computerLetter):
        self.win = None
        self.board =[' '] * 10
        self.playerLetter = playerLetter
        self.computerLetter = computerLetter
        self.turn = self.whoGoesFirst()
        self.gameIsPlaying = True

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def isBoardFull(self,board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(self,board, i):
                return False
        return True

    def makeMove(self, board, letter, move):
    ###controlsss......
        board[move] = letter

    def isWinner(self, bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


    def getBoardCopy(self,board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []
        for i in board:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(self, board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'
            # Here is our algorithm for our Tic Tac Toe AI:
            # First, check if we can win in the next move
        for i in range(1, 10):
            copy = self.getBoardCopy(self, board)
            if self.isSpaceFree(self, copy, i):
                self.makeMove(self, copy, computerLetter, i)
                if self.isWinner(self.copy, computerLetter):
                    return i
        # Check if the player could win on their next move, and block them.
        for i in range(1, 10):
            copy = self.getBoardCopy(self, board)
            if self.isSpaceFree(self, copy, i):
                self.makeMove(self, copy, playerLetter, i)
                if self.isWinner(self, copy, playerLetter):
                    return i
        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(self, board, [1, 3, 7, 9])
        if move != None:
            return move
        # Try to take the center, if it is free.
        if self.isSpaceFree(self, board, 5):
            return 5
        # Move on one of the sides.
        return self.chooseRandomMoveFromList(self, board, [2, 4, 6, 8])
