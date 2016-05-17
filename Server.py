import Game
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import uuid


class GameThread(threading.Thread):
    def __init__(self,game):
        self.game = game
        threading.Thread.__init__(self)

    def startGame(self,playerLetter):
        self.game.start(playerLetter)

    def move(self,letter,move):
        self.game.makeMove(self.game.board,letter,move)

class GameHandler():
    def __init__(self):
        self.gameThreads = {}

    def createGame(self):
        id = str(uuid.uuid4())
        #lock
        self.gameThreads[id] = None
        #release lock
        return "0110 GAME CREATED" + id

    def startGame(self,playerID,playerLetter):
        if (self.gameThreads[playerID]) is None:
            return "0290 PLAYER NOT FOUND"
        game = Game(False)
        thread = GameThread(game)
        #lock
        self.gameThreads[playerID] = thread
        #release
        thread.start()
        if game.start(playerLetter):
            return "0210 GAME IS STARTED"
        return "0999 UNKOWN ERROR"

    def getBoard(self,playerID):
        thread = self.gameThreads[playerID]
        thread.game.getBoardCopy(thread.game.board)

    def endGame(self,playerID):
        thread = self.gameThreads[playerID]
        thread.game = None
        #lock
        self.gameThreads.pop(playerID,None)
        #release
        return "0810 GAME IS TERMINATED"

    def move(self,playerID, moveLetter):
        thread = self.gameThreads[playerID]
        if thread.game.isSpaceFree(thread.game.board,moveLetter):
            thread.move(thread.game.playerLetter,moveLetter)
            if thread.game.isWinner(thread.game.board,thread.game.playerLetter):
                return "0380 GAME IS OVER PLAYER HAS BEEN WON"
            else:
                cmove = thread.game.getComputerMove(thread.game.board,thread.game.computerLetter)
                thread.move(thread.game.computerLetter,cmove)
                if (thread.game.isWinner(thread.game.board, thread.game.computerLetter)):
                    return "0390 GAME IS OVER COMPUTER HAS BEEN WON"
        else:
            return "0930 POSITION IS INVALID - FULL"

        return "0310 MOVE HAS BEEN HAPPENED"

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                                requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()
server.register_instance(GameHandler())
server.serve_forever()



