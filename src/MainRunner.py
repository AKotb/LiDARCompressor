import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu, QFileDialog)

from src import LASHandler, About


class MainRunner(QMainWindow):
    CONST_LASTOOLS_PATH = 'D:/Education/Master/Thesis/Sources/LAStools/bin'
    def __init__(self):
        super(MainRunner, self).__init__()
        self.title = 'LiDAR Compressor'
        self.x = 50
        self.y = 100
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.createActions()
        self.createMenus()

    def createActions(self):
        self.openAct = QAction("&Open...", self, shortcut="Ctrl+O", triggered=self.open)
        self.saveAct = QAction("&Save", self, shortcut="Ctrl+S", triggered=self.save)
        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q", triggered=self.close)
        self.histogramAct = QAction("&Histogram", self, enabled=False, triggered=self.histogram)
        self.metadataAct = QAction("&Metadata", self, enabled=False, triggered=self.metadata)
        self.compressLasAct = QAction("&Compress LAS", self, enabled=True, triggered=self.compresslas)
        self.decompressLazAct = QAction("&Decompress LAZ", self, enabled=True, triggered=self.decompresslaz)
        self.aboutAct = QAction("&About", self, triggered=self.about)

    def createMenus(self):
        self.fileMenu = QMenu("&File", self)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.toolsMenu = QMenu("&Tools", self)
        self.toolsMenu.addAction(self.metadataAct)
        self.toolsMenu.addAction(self.histogramAct)
        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction(self.compressLasAct)
        self.toolsMenu.addAction(self.decompressLazAct)

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.toolsMenu)
        self.menuBar().addMenu(self.helpMenu)

    def about(self):
        about = About.About()
        about.about(self)

    def open(self):
        self.inputLASFilePath = QFileDialog.getOpenFileName(self, "Input LAS File", QDir.currentPath())[0]
        lashandler = LASHandler.LASHandler()
        self.loadedLASFile = lashandler.loadLASFile(self, self.inputLASFilePath)

    def save(self):
        generatedLASFilePath = QFileDialog.getSaveFileName(self, "Output LAS File", QDir.currentPath())[0]
        lashandler = LASHandler.LASHandler()
        lashandler.saveLASFile(self.loadedLASFile, generatedLASFilePath)

    def histogram(self):
        lashandler = LASHandler.LASHandler()
        lashandler.generateLASFileHistogram(self, self.loadedLASFile)

    def metadata(self):
        lashandler = LASHandler.LASHandler()
        lashandler.showLASFileMetadata(self, self.loadedLASFile)

    def compresslas(self):
        inputlasfilepath = QFileDialog.getOpenFileName(self, "Input LAS File", QDir.currentPath(), "*.las")[0]
        lashandler = LASHandler.LASHandler()
        data = inputlasfilepath.split('.')
        outputlazfilepath = data[0] + ".laz"
        lashandler.compresslasfile(self.CONST_LASTOOLS_PATH, inputlasfilepath, outputlazfilepath)

    def decompresslaz(self):
        inputlazfilepath = QFileDialog.getOpenFileName(self, "Input LAZ File", QDir.currentPath(), "*.laz")[0]
        lashandler = LASHandler.LASHandler()
        data = inputlazfilepath.split('.')
        outputlasfilepath = data[0] + ".las"
        lashandler.decompresslazfile(self.CONST_LASTOOLS_PATH, inputlazfilepath, outputlasfilepath)


sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainrunner = MainRunner()
    mainrunner.show()
    sys.exit(app.exec_())
