import os


class Display(object):
    def __init__(self):
        fp = os.path.dirname(__file__) + '\\RoomTemplate.txt'
        self.roomTemplate = open(fp).read()

    def displayMap(self, tile, nthRoom, sthRoom, eastRoom, westRoom):
        room = self.roomTemplate
        if tile.north:
            room = room.replace("NNNNNN", "      ")
            room = room.replace("XXnthroomXXX", self.roomNameFormat(nthRoom))
        else:
            room = room.replace("NNNNNN", "______")
            room = room.replace("XXnthroomXXX", " ")
        if tile.south:
            room = room.replace("SSSSSS", "      ")
            room = room.replace("XXsthroomXXX", self.roomNameFormat(sthRoom))
        else:
            room = room.replace("SSSSSS", "______")
            room = room.replace("XXsthroomXXX", " ")
        if tile.east:
            room = room.replace("E", " ")
            room = room.replace("XXeastroomXX", self.roomNameFormat(eastRoom))
        else:
            room = room.replace("E", "|")
            room = room.replace("XXeastroomXX", "            ")
        if tile.west:
            room = room.replace("W", " ")
            room = room.replace("XXwestroomXX", self.roomNameFormat(westRoom))
        else:
            room = room.replace("W", "|")
            room = room.replace("XXwestroomXX", "            ")
        room = room.replace("XXroomnameXX", self.roomNameFormat(tile.name))
        print(room)

    def displayItemCard(self, msg, time):
        print("----------------------------------------")
        print("    The current time is " + str(time) + "pm")
        if msg == "Item":
            print("    You may find an item if you choose.")
        elif isinstance(msg, int):
            print("    You are being attacked by "+ str(msg) + " zombies!.")
        else:
            print("    " + msg)
        print("----------------------------------------")

    def displayActions(self):
        pass

    def displayItems(self, item1, item2):
        print("----------------------------------------")
        print("Items available:")
        print("    1: " + str(item1))
        print("    2: " + str(item2))
        print("----------------------------------------")

    def roomNameFormat(self, name):
        freeSpace = 12 - len(str(name))
        fsRight = round(freeSpace / 2)
        fsLeft = freeSpace - fsRight
        name = fsLeft * " " + name + fsRight * " "
        return name
