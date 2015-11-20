#!/usr/bin/python

# Display I/O memory map in Linux 2.4+
# Copyright (C) 2015 Davide Madrisan <davide.madrisan.gmail.com>

import os
import sys

__author__ = "Davide Madrisan"
__copyright__ = "Copyright 2015 Davide Madrisan"
__license__ = "GPLv3"
__version__ = "1"
__email__ = "davide.madrisan.gmail.com"
__status__ = "stable"

def die(exitcode, message):
    "Print an error message and exit with code 'errorcode'"
    sys.stderr.write('pyoocs: Fatal error: %s\n' % message)
    sys.exit(exitcode)

def readfile(filename):
    "Returns a list containing the lines of 'filename'"
    if not os.path.isfile(filename):
        die(1, 'No such file: ' + filename)

    fd = open(filename, 'r')
    try:
       content = fd.readlines()
    except:
       die(1, 'Error opening the file ' + filename)
    return content

def toMb(number):
    "Convert 'number' bytes to the equivalent number of Mb"
    return int(number, 16) / 1024 / 1024

def main():
    data = readfile('/proc/iomem')
    for line in data:
        (range, takenby) = line.split(':', 1)
        (b, e) = range.strip().split('-', 1)
        sys.stdout.write('%d to %d bytes (%d to %d Mb) - %s\n' % (
            int(b, 16), int(e, 16), toMb(b), toMb(e), takenby.strip()))

if __name__ == '__main__':
    exitcode = 0
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')
    sys.exit(exitcode)
