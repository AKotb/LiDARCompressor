# import time
# import libarchive.public
# import libarchive.constants
# from src.main import LASHandler
#
#
# class Operation7ZIP:
#
#     def compressfile(self, inputfilepath, outputfilepath):
#         start = time.time()
#         libarchive.public.create_file(outputfilepath, libarchive.constants.ARCHIVE_FORMAT_7ZIP,[inputfilepath])
#         end = time.time()
#         compressiontime = end - start
#         compressionratio = LASHandler.computecompressionratio(inputfilepath, outputfilepath)
#         returnedarray = []
#         returnedarray.append(compressiontime)
#         returnedarray.append(compressionratio)
#         return returnedarray


