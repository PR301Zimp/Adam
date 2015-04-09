Unbreakable = -1

class Item(object):
    def __init__(self, name, damage = 0, message = "", uses = Unbreakable):
        self.name = name
        self.damage = damage
        self.message = message
        self.uses = uses
