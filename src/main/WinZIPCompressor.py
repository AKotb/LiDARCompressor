import zipfile
import os
import time
from subprocess import *

class WinZIPCompressor:

    def compressfile(self, pathoffiletocompress, pathofcompressedfile):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\winzipcompress.bat")
        start = time.time()
        p = Popen([batfilepath, pathofcompressedfile, pathoffiletocompress], stdout=PIPE, stderr=PIPE)
        p.communicate()
        p.wait()
        end = time.time()
        compressiontime = end - start
        compressionratio = self.computecompressionratio(pathoffiletocompress, pathofcompressedfile)
        returnedarray = []
        returnedarray.append(compressiontime)
        returnedarray.append(compressionratio)
        return returnedarray

    def decompressfile(self, pathofcompressedfile, pathofextractdirectory):
        batfilepath = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "resources\winzipdecompress.bat")
        start = time.time()
        p = Popen([batfilepath, pathofcompressedfile, pathofextractdirectory], stdout=PIPE, stderr=PIPE)
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