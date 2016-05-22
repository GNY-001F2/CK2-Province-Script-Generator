# CK2 Culture Script Generator
# Copyright (C) 2016 Gundam Astraea Type F2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import argparse
import os

cwd = os.getcwd()
_reserved_rgb_values = [[0, 0, 0], [255, 255, 255]]
_usedrgbvalues = []

class psg:

    __reservedvalues = [] # list containing reserved RGB values not to be
                          # applied to provinces

    def __init__(self, provincefile, delimiter, target):
        self.__provincefile = provincefile
        self.__delimiter = delimiter
        self.__target = target
        self.__startvalue = startvalue
        self.__provincelist = []
        

    def generate_province_list(self):
        try:
            with open(self.__provincefile, "r") as provincefile:
                if __delimiter:
                    for line in provincefile:
                        __provincelist.extend(line.split(__delimiter))
                else:
                    __provincelist.extend(provincefile.read().split())

        except:
            print("The province file that you specified does not exist...")
            exit()

    def write_provinces_to_file(self):
        try:
            import random
            rgb = [0, 0, 0]
            rgbstring = str(rgb[0])+";"+str(rgb[1])+";"+str(rgb[2])+";"
            while(rgb in _reserved_rgb_values or rgbstring in _usedrgbvalues):
                rgb = [random.randrange(0, 255), random.randrange(0, 255),
                       random.randrange(0, 255)]
                rgbstring = str(rgb[0])+";"+str(rgb[1])+";"+str(rgb[2])+";"
            with open(self.__target, "a") as targetfile:
                i = self.__startvalue
                for province in self.__provincelist:
                    targetfile.write(str(i))
            (int(v) for v in args.rgb.split(";") if v and 0 <= int(v) <= 255)
        if ((r, g, b) in _reserved_rgb_values):
            # Not entirely sure which ones are reserved. I'm waiting for the 
            # forum people to tell me.
            print("RGB value cannot be \""+str(r)+";"+str(g)+";"+str(b)+";\". "
                  "It is reserved by the game.")
            exit()
    except:
        print("Your rgb input is invalid. It must (0-255);(0-255);(0-255), "
              "excluding any reserved values.")
        exit()


def check_values(args):
    if cwd != args.path:
        try:
            os.chdir(args.path)
            cwd = os.getcwd()
        except:
            print("ERROR: Invalid path specified.")
            exit()

    if args.target[:4] != ".csv"
        print("ERROR: Target name must be a .csv.")
        exit()
    try:
        with open(args.usedrgbvalues, "r") as _usedrgbvaluesfile:
            _usedrgbvalues += _usedrgbvaluesfile.read().split()
    except FileNotFoundError:
        _usedrgbvaluesfile = open(args.usedrgbvalues, "a")
        _usedrgbvaluesfile.close()
    except:
        print("Something went seriously wrong when opening "
                  "usedrgbvalues.csv")
        exit()
    if args.startvalue < 1:
        print("Starting province number cannot be less than 1.")
        exit()

    return args

if __name__ == "__main__":
    parser = \
        argparse.ArgumentParser(description="Generate definitions.csv for your"
                                "CK2 map.",
                                formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-p", "--path", default=os.getcwd(), help="The "
                        "absolute or relative to current directory path "
                        "where all your music is located; default is your "
                        "current working directory.")
    parser.add_argument("-f", "--provincefile", default="provinces.txt",
                        help="The name of the file contaiing your list of "
                        "provinces.")
    parser.add_argument("-d", "--delimiter", default=None, help="If set, the "
                        "delimiter to use to split all the names in every "
                        "line. Useful if you have many names.\nThe default is "
                        "None, which means the standard whitespace is used.")
    parser.add_argument("-t", "--target", default="definitions.csv", help=""
                        "Contains the province names, province number and "
                        "associated RGB values. By default it is named "
                        "definitions.csv, but it might be useful to rename "
                        "if working on different parts of the map to avoid "
                        "conflicts. Target name must end in .csv.\n"
                        "WARNING: Use --startvalue to avoid conflicts with "
                        "province numbers.\n"
                        "WARNING: Make sure that your usedbgrvalues.txt "
                        "is up to date and contains the values used in any "
                        "other partial province files for your map.")
    parser.add_argument("--startvalue", default=1, type=int, help="Integer "
                        "value that tells the script from to where to start "
                        "numbering provinces;  default is 1.")
    parser.add_argument("--usedrgbvalues", type=str,
                        default="usedrgbvalues.txt", help="File that contains "
                        "all the RGB values that have already been used up; "
                        "default is usedrgbvalues.txt.\n"
                        "If the file does not exist it will be created.")

    args = parser.parse_args();

    args = check_values(args);

    psg.obj = (args.provincefile, args.delimiter, args.target, args.startvalue)
    obj.generate_province_list()
    obj.write_provinces_to_file()
