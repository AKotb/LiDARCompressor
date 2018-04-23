from laspy.file import File
import matplotlib.pyplot as plt
from src import MetadataViewer

class LASHandler:

    def loadLASFile(self, MainRunner, LASFilePath):
        inFile = File(LASFilePath, mode='r')
        MainRunner.histogramAct.setEnabled(True)
        MainRunner.metadataAct.setEnabled(True)
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