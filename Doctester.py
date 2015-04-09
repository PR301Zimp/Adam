import doctest
import os

class Doctester(object):
    def __init__(self, filePath = os.path.dirname(__file__) + '\\broadTestData.txt'):
        self.dt = doctest
        self.filePath = filePath

    def setFilePath(filePath):
        self.filePath = filePath

    def runTest(self):
        self.dt.testfile(self.filePath)


dt = Doctester()
dt.runTest()