#
# txt2lasPro.py
#
# (c) 2013, martin isenburg - http://rapidlasso.com
#     rapidlasso GmbH - fast tools to catch reality
#
# uses txt2las.exe to turn ASCII text into LAS files
#
# ASCII input:   TXT
# LiDAR output:  LAS/LAZ/BIN/TXT
#
# for licensing see http://lastools.org/LICENSE.txt
#

import arcgisscripting
import os
import subprocess
import sys


def check_output(command, console):
    if console == True:
        process = subprocess.Popen(command)
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)
    output, error = process.communicate()
    returncode = process.poll()
    return returncode, output


### create the geoprocessor object
gp = arcgisscripting.create(9.3)

### report that something is happening
gp.AddMessage("Starting txt2las production ...")

### get number of arguments
argc = len(sys.argv)

### report arguments (for debug)
# gp.AddMessage("Arguments:")
# for i in range(0, argc):
#    gp.AddMessage("[" + str(i) + "]" + sys.argv[i])

### get the path to LAStools
lastools_path = os.path.dirname(os.path.dirname(os.path.dirname(sys.argv[0])))

### make sure the path does not contain spaces
if lastools_path.count(" ") > 0:
    gp.AddMessage("Error. Path to .\\lastools installation contains spaces.")
    gp.AddMessage("This does not work: " + lastools_path)
    gp.AddMessage("This would work:    C:\\software\\lastools")
    sys.exit(1)

### complete the path to where the LAStools executables are
lastools_path = lastools_path + "\\bin"

### check if path exists
if os.path.exists(lastools_path) == False:
    gp.AddMessage("Cannot find .\\lastools\\bin at " + lastools_path)
    sys.exit(1)
else:
    gp.AddMessage("Found " + lastools_path + " ...")

### create the full path to the txt2las executable
txt2las_path = lastools_path + "\\txt2las.exe"

### check if executable exists
if os.path.exists(lastools_path) == False:
    gp.AddMessage("Cannot find txt2las.exe at " + txt2las_path)
    sys.exit(1)
else:
    gp.AddMessage("Found " + txt2las_path + " ...")

### create the command string for txt2las.exe
command = ['"' + txt2las_path + '"']

### maybe use '-verbose' option
if sys.argv[argc - 1] == "true":
    command.append("-v")

### counting up the arguments
c = 1

### add input LiDAR
wildcards = sys.argv[c + 1].split()
for wildcard in wildcards:
    command.append("-i")
    command.append('"' + sys.argv[c] + "\\" + wildcard + '"')
c = c + 2

### maybe use a user-defined parse string
if sys.argv[c] != "xyz":
    command.append("-parse")
    command.append(sys.argv[c])
c = c + 1

### maybe skip a few lines
if sys.argv[c] != "0":
    command.append("-skip")
    command.append(sys.argv[c])
c = c + 1

### set LAS version
if sys.argv[c] != "1.2":
    command.append("-set_version")
    command.append(sys.argv[c])
c = c + 1

### maybe an output format was selected
if sys.argv[c] != "#":
    if sys.argv[c] == "las":
        command.append("-olas")
    elif sys.argv[c] == "laz":
        command.append("-olaz")
    elif sys.argv[c] == "bin":
        command.append("-obin")
    elif sys.argv[c] == "xyz":
        command.append("-otxt")
    elif sys.argv[c] == "xyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("xyzi")
    elif sys.argv[c] == "txyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("txyzi")
c = c + 1

### maybe an output directory was selected
if sys.argv[c] != "#":
    command.append("-odir")
    command.append('"' + sys.argv[c] + '"')
c = c + 1

### maybe an output appendix was selected
if sys.argv[c] != "#":
    command.append("-odix")
    command.append('"' + sys.argv[c] + '"')
c = c + 1

### maybe we should run on multiple cores
if sys.argv[c] != "1":
    command.append("-cores")
    command.append(sys.argv[c])
c = c + 1

### maybe there are additional command-line options
if sys.argv[c] != "#":
    additional_options = sys.argv[c].split()
    for option in additional_options:
        command.append(option)

### report command string
gp.AddMessage("LAStools command line:")
command_length = len(command)
command_string = str(command[0])
command[0] = command[0].strip('"')
for i in range(1, command_length):
    command_string = command_string + " " + str(command[i])
    command[i] = command[i].strip('"')
gp.AddMessage(command_string)

### run command
returncode, output = check_output(command, False)

### report output of txt2las
gp.AddMessage(str(output))

### check return code
if returncode != 0:
    gp.AddMessage("Error. txt2las failed.")
    sys.exit(1)

### report happy end
gp.AddMessage("Success. txt2las done.")
