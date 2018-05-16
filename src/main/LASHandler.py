import os
import sys
import time
from subprocess import *

import matplotlib.pyplot as plt
from laspy.file import File

from src.test import MetadataViewer


class LASHandler:

    def loadLASFile(self, LASFilePath):
        inFile = File(LASFilePath, mode='r')
        return inFile

    def generateLASFileHistogram(self, loadedLASFile):
        plt.hist(loadedLASFile.intensity)
        plt.title('Histogram of the Intensity Dimension')
        plt.show()

    def showLASFileMetadata(self, MainRunner, loadedLASFile):
        MainRunner.metadataviewer = MetadataViewer.MetadataViewer(loadedLASFile)

    def viewfileinfo(self, lastoolspath, inputlasfilepath):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\lidarfileinfo.bat")
        p = Popen([batfilepath, lastoolspath, inputlasfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()

    def compresslasfile(self, lastoolspath, inputlasfilepath, outputlazfilepath):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\compresslas.bat")
        start = time.time()
        p = Popen([batfilepath, lastoolspath, inputlasfilepath, outputlazfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        end = time.time()
        compressiontime = end - start
        compressionratio = self.computecompressionratio(inputlasfilepath, outputlazfilepath)
        returnedarray = []
        returnedarray.append(compressiontime)
        returnedarray.append(compressionratio)
        return returnedarray

    def decompresslazfile(self, lastoolspath, inputlazfilepath, outputlasfilepath):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\decompresslaz.bat")
        start = time.time()
        p = Popen([batfilepath, lastoolspath, inputlazfilepath, outputlasfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        end = time.time()
        decompressiontime = end - start
        returnedarray = []
        returnedarray.append(decompressiontime)
        return returnedarray

    def compressasciifile(self, lastoolspath, inputasciifilepath, outputcompressedfilepath):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\compressascii.bat")
        start = time.time()
        p = Popen([batfilepath, lastoolspath, inputasciifilepath, outputcompressedfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        end = time.time()
        compressiontime = end - start
        compressionratio = self.computecompressionratio(inputasciifilepath, outputcompressedfilepath)
        returnedarray = []
        returnedarray.append(compressiontime)
        returnedarray.append(compressionratio)
        return returnedarray

    def decompressasciifile(self, lastoolspath, inputcompressedfilepath, outputasciifilepath):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\decompressascii.bat")
        start = time.time()
        p = Popen([batfilepath, lastoolspath, inputcompressedfilepath, outputasciifilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        end = time.time()
        decompressiontime = end - start
        returnedarray = []
        returnedarray.append(decompressiontime)
        return returnedarray

    def computecompressionratio(self, originalfile, compressedfile):
        originalfilesize = float(os.path.getsize(originalfile))
        compressedfilesize = float(os.path.getsize(compressedfile))
        compressionratio = float(compressedfilesize / originalfilesize) * 100
        return compressionratio


sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook
