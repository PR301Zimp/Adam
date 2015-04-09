from FileManager import FileManager
from Player import Player
from Display import Display
from CMD import CMD
from Item import Item
from ActionCard import ActionCard
from Display import Display
import Tile
import random


class Game(object):
    def __init__(self):
        self.allMyIndoorTiles = {}
        self.allMyOutdoorTiles = {}
        self.time = 9  # Need to change to correct time
        self.actionCards = []
        self.actionCardsCurrent = []
        self.map = []
        # New
        self.allMyItems = {}
        self.fm = FileManager()
        self.player = Player()
        self.cmd = CMD(self)
        self.display = Display()
        self.saves = None
        # End New

    # New
    def loadFile(self, filePath):
        self.saves = self.fm.savedGames(filePath)
    # End New

    def save(self, fileName):
        state = {}  # What goes into state
        state["indoor"] = self.allMyIndoorTiles
        state["outdoor"] = self.allMyOutdoorTiles
        state["time"] = self.time
        state["allActionCards"] = self.actionCards
        state["currentActionCards"] = self.actionCardsCurrent
        state["map"] = self.map
        state["player"] = self.player
        self.fm.saveGame(state, fileName)

    def load(self, fileName):
        state = self.fm.loadGame(fileName)  # What goes into state
        # Assign values in state to __init__ variables
        self.allMyIndoorTiles = state["indoor"]
        self.allMyOutdoorTiles = state["outdoor"]
        self.time = state["time"]
        self.actionCards = state["allActionCards"]
        self.actionCardsCurrent = state["currentActionCards"]
        self.map = state["map"]
        self.player = state["player"]

    def drawCard(self):
        if not self.actionCardsCurrent:
            self.time += 1
            self.shuffleActionCards()
        intRandom = random.randrange(0, len(self.actionCardsCurrent))
        card = self.actionCardsCurrent[intRandom]
##        self.actionCardsCurrent.remove(intRandom)
        return card

    def addCard(self, actionCard):
        self.actionCards.append(actionCard)

    def newGame(self):
        pass

    def continueGame(self):
        pass

    def addTile(self, tile):
        pass

    def combat(self):
        pass

    def movePlayer(self, Xmovement, Ymovement):
        self.player.move(Xmovement, Ymovement)

    def waitHeal(self):
        # Move time and remove action card
        Game.drawCard()
        self.player.changeHealth(3)

    def runAway(self):
        self.player.moveBack()
        self.player.changeHealth(-1)

    def searchTotem(self):
        pass

    def buryTotem(self):
        pass

    def suicide(self):
        pass

    # New
    def createItem(self, name, damage, message, uses):
        self.allMyItems[name] = Item(name, damage, message, uses)

    def getItem(self, itemName):
        return self.allMyItems[itemName]

    def createActionCard(self, itemName, msgNine, msgTen, msgEleven):
        item = Game.getItem(self, itemName)
        Game.addCard(self, ActionCard(item, msgNine, msgTen, msgEleven))

    def shuffleActionCards(self):
        self.actionCardsCurrent = self.actionCards
        for i in range(2):
            del self.actionCardsCurrent[random.randrange(0, 8 - i)]

    def createTile(self, tileType, name, north=False, south=False, east=False, west=False, message=""):
        if tileType == "out":
            tile = Tile.OutdoorTile(name, north, south, east, west, message)
            self.allMyOutdoorTiles[name] = tile
        elif tileType == "in":
            tile = Tile.IndoorTile(name, north, south, east, west, message)
            self.allMyIndoorTiles[name] = tile

    def displayTile(self, tile, nthRoom="None", sthRoom="None", eastRoom="None", westRoom="None"):
        self.display.displayMap(tile, nthRoom, sthRoom, eastRoom, westRoom)

    def displayItems(self):
        self.display.displayItems(self.player.item1, self.player.item2)

    def takeTurn(self):
        card = self.drawCard()
        if self.time == 9:
            msg = card.msgNine
        elif time == 10:
            msg = card.msgTen
        else:
            msg = card.msgEleven
        self.display.displayItemCard(msg, self.time)
    # End New


def startGameWithData():
    g = Game()

    g.createItem('Oil', 0, "", 1)
    g.createItem('Gasoline', 0, "", 1)
    g.createItem('Board with Nails', 1, "", -1)
    g.createItem('Machete', 3, "", -1)
    g.createItem('Grisly Femur', 1, "", -1)
    g.createItem('Golf Club', 1, "", -1)
    g.createItem('Chainsaw', 4, "", 2)
    g.createItem('Can of Soda', 0, "", 1)
    g.createItem('Candle', 0, "", 1)

    g.createActionCard('Oil', 'You try hard not to wet yourself', 'Item', 6)
    g.createActionCard('Gasoline', 4, 'You sense your impending doom', 'Item')
    g.createActionCard('Board with Nails', 'Item', 4, 'Something icky in your mouth')
    g.createActionCard('Machete', 4, 'A bat poops in your eye', 6)
    g.createActionCard('Grisly Femur', 'Item', 5, 'Your sould is not wanted here')
    g.createActionCard('Golf Club', 'Slip on nasty goo', 4, 'The smell of blood is in the air')
    g.createActionCard('Chainsaw', 3, 'you hear terrible screams', 5)
    g.createActionCard('Can of Soda', 'Candy bar in your pocket', 'Item', 4)
    g.createActionCard('Candle', 'Your body shivers involuntarily', 'You feel a spark of hope', 4)

    g.shuffleActionCards()

    g.createTile("in", 'Bathroom', True, False, False, False, "")
    g.createTile("in", 'Kitchen', True, True, False, True, '+1 health if end move here')
    g.createTile("in", 'Storage', True, False, False, False, 'may search for an item here')
    g.createTile("in", 'Evil Temple', False, True, False, True, 'can search for the totem here')
    g.createTile("in", 'Family Room', True, True, False, True, "")
    g.createTile("in", 'Dining Room', True, True, True, True, "")
    g.createTile("in", 'Bedroom', True, False, False, True, "")
    g.createTile("in", 'Foyer', True, False, False, False, "")

    g.createTile("out", 'Garden', False, True, True, True, '+1 Health of end turn here')
    g.createTile("out", 'Sitting Area', False, True, True, True, "")
    g.createTile("out", 'Yard01', False, True, True, True, "")
    g.createTile("out", 'Graveyard', False, True, True, False, 'Can bury the totem here')
    g.createTile("out", 'Garage', False, False, True, True, "")
    g.createTile("out", 'Patio', True, True, True, False, "")
    g.createTile("out", 'Yard02', False, True, True, True, "")
    g.createTile("out", 'Yard03', False, True, True, True, "")

    return g

if __name__ == '__main__':
    game = startGameWithData()
    game.displayTile(game.allMyIndoorTiles["Dining Room"])
    game.displayItems()
    game.takeTurn()
    # game.cmd.cmdloop()
