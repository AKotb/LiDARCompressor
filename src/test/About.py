import sys

from PyQt5.QtWidgets import (QMessageBox)


class About:

    def about(self, MainRunner):
        QMessageBox.about(MainRunner, " About LiDAR Compressor",
                          "<p><b>LiDAR Compressor</b> is an adaptable system for "
                          "compressing LiDAR data.</p>"
                          "<b>LiDAR Compressor</b> Version <b>0.1</b>")


sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook
