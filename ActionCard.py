class ActionCard(object):
    def __init__(self, item, msgNine, msgTen, msgEleven):
        self.item = item
        self.msgNine = msgNine
        self.msgTen = msgTen
        self.msgEleven = msgEleven

    # Depricated
    def getCards(self, dictCards, location):
        pass

    def sortCards(self, location):
        pass
    # End Depricated

    # New
    def getCardInfo(self):
        return [self.msgNine, self.msgTen, self.msgEleven, self.item]
    # End New
