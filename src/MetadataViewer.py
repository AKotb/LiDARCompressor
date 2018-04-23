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
        header = self.loadedLASFile.header
        headerformat = header.header_format
        rowcounter = 0
        for spec in headerformat:
            self.tableWidget.setItem(rowcounter, 0, QTableWidgetItem(spec.name))
            if (spec.name == 'file_sig'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.file_signature))
            if (spec.name == 'file_source_id'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.filesource_id))
            if (spec.name == 'global_encoding'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.global_encoding))
            if (spec.name == 'proj_id_1'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.project_id))
            if (spec.name == 'proj_id_2'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.project_id))
            if (spec.name == 'proj_id_3'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.project_id))
            if (spec.name == 'proj_id_4'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.project_id))
            if (spec.name == 'version_major'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.major_version))
            if (spec.name == 'version_minor'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.minor_version))
            if (spec.name == 'system_id'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.system_id))
            if (spec.name == 'software_id'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.software_id))
            if (spec.name == 'created_day'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem('{:%m/%d/%Y}'.format(header.date)))
            if (spec.name == 'created_year'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem('{:%m/%d/%Y}'.format(header.date)))
            if (spec.name == 'header_size'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.header_size))
            if (spec.name == 'data_offset'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.data_offset))
            if (spec.name == 'num_variable_len_recs'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.records_count))
            if (spec.name == 'data_format_id'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.dataformat_id))
            if (spec.name == 'data_record_length'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.data_record_length))
            if (spec.name == 'point_records_count'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.point_records_count))
            if (spec.name == 'point_return_count'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.point_return_count[0]))
            if (spec.name == 'x_scale'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.scale[0]))
            if (spec.name == 'y_scale'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.scale[1]))
            if (spec.name == 'z_scale'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.scale[2]))
            if (spec.name == 'x_offset'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.offset[0]))
            if (spec.name == 'y_offset'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.offset[1]))
            if (spec.name == 'z_offset'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.offset[2]))
            if (spec.name == 'x_max'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.max[0]))
            if (spec.name == 'x_min'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.min[0]))
            if (spec.name == 'y_max'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.max[1]))
            if (spec.name == 'y_min'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.min[1]))
            if (spec.name == 'z_max'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.max[2]))
            if (spec.name == 'z_min'):
                print(spec.name)
                self.tableWidget.setItem(rowcounter, 1, QTableWidgetItem(header.min[2]))
            rowcounter +=1
        self.tableWidget.move(0, 0)
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())