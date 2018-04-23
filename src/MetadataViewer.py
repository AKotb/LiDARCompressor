import sys
from laspy.file import File
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout)
from PyQt5.QtCore import pyqtSlot


class MetadataViewer(QWidget):

    def __init__(self, loadedLASFile):
        super(MetadataViewer, self).__init__()
        self.loadedLASFile = loadedLASFile
        self.title = 'Metadata Viewer'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()

    def createTable(self, ):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(32)
        self.tableWidget.setColumnCount(2)
        headerformat = self.loadedLASFile.header.header_format
        rowcounter = 0
        print(self.loadedLASFile.header)
        for spec in headerformat:
            self.tableWidget.setItem(rowcounter, 0, QTableWidgetItem(spec.name))
            #self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(self.loadedLASFile.header.scale))
            rowcounter +=1
        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())