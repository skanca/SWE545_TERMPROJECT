from xmlrpclib import ServerProxy

class Client:
    def __init__(self):
        self.playerID = None
        self.board = None
        self.server = ServerProxy("http://localhost:8000")

    def createGame(self):
        self.playerID = self.server.createGame()

    def startGame(self,playerLetter):
        self.server.startGame(self.playerID,playerLetter)

    def makeMove(self,move):
        self.server.move(self.playerID,move)

    def endGame(self):
        self.server.endGame(self.playerID)

    def inputPlayerLetter(self):
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
        letter = input().upper()
        return letter

    def getPlayerMove(self):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split():
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def getBoard(self):
        self.board = self.server.getBoard(self.playerID)

    def drawBoard(board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def parse(self,response):
        return True




client = Client()
response = client.createGame()

if (client.parse(response)):
    while True:
        playerLetter = client.inputPlayerLetter()
        client.startGame(playerLetter)
        gameFinished = False
        while not gameFinished:
            client.drawBoard(client.getBoard())
            playerMove = client.getPlayerMove()
            response = client.makeMove(playerMove)
            if (client.parse(response)) is "FINISH":
                client.drawBoard(client.getBoard())
                gameFinished = True






