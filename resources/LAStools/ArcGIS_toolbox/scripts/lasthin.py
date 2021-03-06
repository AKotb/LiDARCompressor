#
# lasthin.py
#
# (c) 2013, martin isenburg - http://rapidlasso.com
#     rapidlasso GmbH - fast tools to catch reality
#
# uses lasthin.exe to thin LiDAR points by placing a uniform grid over them
# and by keeping only the point with the lowest (or 'highest' or 'random')
# Z coordinate within each grid cell.
#
# LiDAR input:   LAS/LAZ/BIN/TXT/SHP/BIL/ASC/DTM
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
gp.AddMessage("Starting lasthin ...")

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

### create the full path to the lasthin executable
lasthin_path = lastools_path + "\\lasthin.exe"

### check if executable exists
if os.path.exists(lastools_path) == False:
    gp.AddMessage("Cannot find lasthin.exe at " + lasthin_path)
    sys.exit(1)
else:
    gp.AddMessage("Found " + lasthin_path + " ...")

### create the command string for lasthin.exe
command = ['"' + lasthin_path + '"']

### maybe use '-verbose' option
if sys.argv[argc - 1] == "true":
    command.append("-v")

### add input LiDAR
command.append("-i")
command.append('"' + sys.argv[1] + '"')

### maybe a user-specified grid size
if sys.argv[2] != "1":
    command.append("-step")
    command.append(sys.argv[2].replace(",", "."))

### which point should we keep
if sys.argv[3] == "highest":
    command.append("-highest")
elif sys.argv[3] == "random":
    command.append("-random")

### maybe an output format was selected
if sys.argv[4] != "#":
    if sys.argv[4] == "las":
        command.append("-olas")
    elif sys.argv[4] == "laz":
        command.append("-olaz")
    elif sys.argv[4] == "bin":
        command.append("-obin")
    elif sys.argv[4] == "xyz":
        command.append("-otxt")
    elif sys.argv[4] == "xyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("xyzi")
    elif sys.argv[4] == "txyzi":
        command.append("-otxt")
        command.append("-oparse")
        command.append("txyzi")

### maybe an output file name was selected
if sys.argv[5] != "#":
    command.append("-o")
    command.append('"' + sys.argv[5] + '"')

### maybe an output directory was selected
if sys.argv[6] != "#":
    command.append("-odir")
    command.append('"' + sys.argv[6] + '"')

### maybe an output appendix was selected
if sys.argv[7] != "#":
    command.append("-odix")
    command.append('"' + sys.argv[7] + '"')

### maybe there are additional command-line options
if sys.argv[8] != "#":
    additional_options = sys.argv[8].split()
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

### report output of lasthin
gp.AddMessage(str(output))

### check return code
if returncode != 0:
    gp.AddMessage("Error. lasthin failed.")
    sys.exit(1)

### report happy end
gp.AddMessage("Success. lasthin done.")
