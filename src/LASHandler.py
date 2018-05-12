import os
from subprocess import *

import matplotlib.pyplot as plt
from laspy.file import File

from src import MetadataViewer


class LASHandler:

    def loadLASFile(self, LASFilePath):
        inFile = File(LASFilePath, mode='r')
        return inFile

    def saveLASFile(self, loadedLASFile, generatedLASFilePath):
        I = loadedLASFile.Classification == 2
        generatedLASFile = File(generatedLASFilePath, mode='w', header=loadedLASFile.header)
        generatedLASFile.points = loadedLASFile.points[I]
        generatedLASFile.close()

    def generateLASFileHistogram(self, MainRunner, loadedLASFile):
        plt.hist(loadedLASFile.intensity)
        plt.title('Histogram of the Intensity Dimension')
        plt.show()
        MainRunner.histogramAct.setEnabled(False)

    def showLASFileMetadata(self,MainRunner, loadedLASFile):
        MainRunner.metadataviewer = MetadataViewer.MetadataViewer(loadedLASFile)

    def compresslasfile(self, lastoolspath, inputlasfilepath, outputlazfilepath):
        cwd = os.getcwd()
        batfilepath = os.path.join(cwd, "resources\compresslas.bat")
        print(batfilepath)
        p = Popen([batfilepath, lastoolspath, inputlasfilepath, outputlazfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        self.computecompressionratio(inputlasfilepath, outputlazfilepath)

    def decompresslazfile(self, lastoolspath, inputlazfilepath, outputlasfilepath):
        cwd = os.getcwd()
        batfilepath = os.path.join(cwd, "resources\decompresslaz.bat")
        print(batfilepath)
        p = Popen([batfilepath, lastoolspath, inputlazfilepath, outputlasfilepath], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()

    def computecompressionratio(self, originalfile, compressedfile):
        originalfilesize = float(os.path.getsize(originalfile))
        compressedfilesize = float(os.path.getsize(compressedfile))
        compressionratio = float(compressedfilesize / originalfilesize) * 100
        print(compressionratio)
