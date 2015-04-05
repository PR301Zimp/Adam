import shelve
import unittest
import os


class FileManager(object):
    def __init__(self):
        self.filepath = os.path.dirname(__file__) + '\\saves'
        self.file = None

    def savedGames(self, filepath):
        """
        savedGames(filepath)

        Reads a shelve file at filepath, stores it to the class
        and returns a dictionary of keys.
        """
        try:
            if self.filepath != filepath:
                self.filepath = filepath
            self.file = shelve.open(self.filepath)
            return self.file.keys()
        except IOError:
            print("Cannot find file at " + filepath)
        except:
            print("An error occured, please try again.")

    def saveGame(self, state, fileName):
        """
        saveGame(state, fileName)

        Takes data from state and stores it in shelve file
        specified in savedGames with key of fileName.
        """
        try:
            self.file[fileName] = state
        except:
            print('No file specified, please load file first.')

    def loadGame(self, fileName):
        """
        loadGame(fileName)

        Checks shelve file set through savedGames for a key of fileName,
        returns information contained within.
        """
        try:
            if fileName in self.file:
                return self.file[fileName]
            else:
                print('No save exists with that name.')
        except:
            print('No file specified, please load file first.')

    def delShelve(self, filePath):
        """
        delShelve(filePath)

        Deletes shelve file at filepath.
        """
        if os.path.exists(filePath + '.bak'):
            os.remove(filePath + '.bak')
        if os.path.exists(filePath + '.dat'):
            os.remove(filePath + '.dat')
        if os.path.exists(filePath + '.dir'):
            os.remove(filePath + '.dir')


class unitTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = os.path.dirname(__file__) + '\\test'
        self.fm = FileManager()
        self.fm.delShelve(self.fp)
        self.fm.savedGames(self.fp)

    def test_savedGames(self):
        self.assertEqual(list(self.fm.file), [])

    def test_saveGame(self):
        self.fm.saveGame('state 1', 'name 1')
        self.fm.saveGame('state 2', 'name 2')
        self.fm.saveGame('state 3', 'name 3')
        dict = self.fm.savedGames(self.fp)
        self.assertEqual(list(dict), ['name 3', 'name 2', 'name 1'])

    def test_loadGame(self):
        self.fm.saveGame('state 1', 'name 1')
        self.fm.saveGame('state 2', 'name 2')
        self.assertEqual(self.fm.loadGame('name 2'), 'state 2')


unittest.main()
