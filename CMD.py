from cmd import Cmd

class CMD(Cmd):
    def __init__(self):
        pass

    def do_move(self, direction):
        if direction == "up":
            self.game.movePlayer(0, 1)
        elif direction == "down":
            self.game.movePlayer(0, -1)
        elif direction == "left":
            self.game.movePlayer(-1, 0)
        elif direction == "right":
            self.game.movePlayer(1, 0)
        else:
            print("No valid direction given.")

    def do_rotateTile(self, rotation):
        pass

    def do_placeTile(self):
        pass

    def do_drawCard(self):
        pass

    def do_run(self):
        pass

    def do_fight(self):
        pass

    def do_save(self, fileName):
        self.game.save(fileName)

    def do_load(self, fileName):
        self.game.load(fileName)

    def do_quit(self):
        return True

    def validateCommands(self):
        pass

    # New
    def loadFile(filePath):
        self.game.loadFile(filePath)
    # End New
