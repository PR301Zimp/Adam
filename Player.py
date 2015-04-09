class Player(object):
    def __init__(self):
        self.item1 = None
        self.item2 = None
        self.x = 1
        self.y = 1
        self.health = 6
        self.totem = False
        # New
        self.prevX = None
        self.prevY = None
        # End New

    def getLoc(self):
        return [self.x, self.y]

    # New
    def move(self, newX = 0, newY = 0):
        self.prevX = self.x
        self.x += newX
        self.prevY = self.y
        self.y += newY

    def moveBack(self):
        self.x = self.prevX
        self.prevX = None
        self.y = self.prevY
        self.prevY = None

    def changeHealth(self, amount):
        self.health += amount
    # End New