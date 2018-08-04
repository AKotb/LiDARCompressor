import os
import time
import subprocess

class WinRARCompressor:

    def compressfile(self, pathoffiletocompress, pathofcompressedfile):
        start = time.time()
        loc_winrar = r"C:\Program Files\WinRAR\Rar.exe"
        archive_command = r'"{}" a "{}" "{}"'.format(loc_winrar, pathofcompressedfile, pathoffiletocompress)
        subprocess.call(archive_command, shell=True)
        end = time.time()
        compressiontime = end - start
        compressionratio = self.computecompressionratio(pathoffiletocompress, pathofcompressedfile)
        returnedarray = []
        returnedarray.append(compressiontime)
        returnedarray.append(compressionratio)
        return returnedarray

    def decompressfile(self, pathofcompressedfile, pathtoextractfilein):
        start = time.time()
        loc_winrar = r"C:\Program Files\WinRAR\UnRAR.exe"
        extract_command = r'"{}" x "{}" "{}"'.format(loc_winrar, pathofcompressedfile, pathtoextractfilein)
        subprocess.call(extract_command, shell=True);
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