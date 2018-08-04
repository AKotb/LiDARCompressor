import os
import time
import subprocess


class ZIP7Compressor:

    def compressfile(self, pathoffiletocompress, pathofcompressedfile):
        start = time.time()
        loc_7z = r"C:\Program Files\7-Zip\7z.exe"
        archive_command = r'"{}" a "{}" "{}"'.format(loc_7z, pathofcompressedfile, pathoffiletocompress)
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
        loc_7z = r"C:\Program Files\7-Zip\7z.exe"
        extract_command = r'"{}" x "{}" -o"{}"'.format(loc_7z, pathofcompressedfile, pathtoextractfilein)
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