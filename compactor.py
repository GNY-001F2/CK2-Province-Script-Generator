# usedrgbvalues File compactor
# Copyright (C) 2016 Gundam Astraea Type F2
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
Clean up usedrgbvalues.txt
'''
import argparse
import os
from collections import Counter

cwd = os.getcwd()
_usedrgbvalues = []

if __name__ == "__main__":

    parser = \
        argparse.ArgumentParser(description="Clean up and compact your file"
                                " for used RGB values.",
                                formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-p", "--path", default=os.getcwd(), help="The "
                        "absolute or relative to current directory path "
                        "where your used RGB values file is located.\n"
                        "The default location is your current directory.")
    parser.add_argument("-f", "--filename", default="usedrgbvalues.txt", help=""
                        "The file which contains your list of used RGB values")

    args = parser.parse_args()

    _usedrgbvaluesfilename = args.filename

    try:
        if args.path != cwd:
            os.chdir(args.path)
            cwd = os.getcwd()
    except:
        print("Error changing path due to invalid argument or system error.")
        exit()

    try:
        with open(_usedrgbvaluesfilename, "r", encoding="cp1252") as \
          _usedrgbvaluesfile:
              _usedrgbvalues += _usedrgbvaluesfile
    except:
        print("File does not exist.")
        exit()

    _usedrgbvaluesdict = Counter(_usedrgbvalues)
    _usedrgbvaluesscrubbed = []
    for key in _usedrgbvaluesdict:
        _usedrgbvaluesscrubbed.append(key)

    writefile = open(args.filename[:-4]+"_corrected"+args.filename[-4:], "w",
                     encoding="cp1252")
    writefile.close()
    with open(args.filename[:-4]+"_corrected"+args.filename[-4:], "a",
                   encoding="cp1252") as writefile:
        for rgbvalue in _usedrgbvaluesscrubbed:
            writefile.write(rgbvalue)
