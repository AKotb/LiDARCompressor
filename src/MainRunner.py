import sys
from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QMenu, QFileDialog)
from PyQt5.QtCore import QDir
from src import LASHandler, About, MetadataViewer


class MainRunner(QMainWindow):
    def __init__(self):
        super(MainRunner, self).__init__()
        self.title = 'LiDAR Compressor'
        self.x = 50
        self.y = 100
        self.width = 400
        self.height = 50
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

        self.helpMenu = QMenu("&Help", self)
        self.helpMenu.addAction(self.aboutAct)

        self.menuBar().addMenu(self.fileMenu)
        self.menuBar().addMenu(self.toolsMenu)
        self.menuBar().addMenu(self.helpMenu)

    def about(self):
        about = About.About()
        about.about(self)

    def open(self):
        inputLASFilePath = QFileDialog.getOpenFileName(self, "Input LAS File", QDir.currentPath())[0]
        lashandler = LASHandler.LASHandler()
        self.loadedLASFile = lashandler.loadLASFile(self, inputLASFilePath)

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
