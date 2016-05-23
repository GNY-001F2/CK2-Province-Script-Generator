# CK2-Province-Script-Generator

Generates definitions.csv that contains basic mapping information for each 
province.

##Instructions

* You need Python 3. This script was written and tested on Python 3.5.1 but
slightly older versions should work as well.

* DO NOT try to run this script on Python 2. Python 3 and Python 2 are not
compatible with each other.

* You can download the appropriate verison of Python 3 from
https://www.python.org/downloads/
  * If you use an OS with a package manager (most mainstream *nixes) you can
download python3 from there if you do not already have it.

* This program is invoked from a command line interface. I have only tested it
on a linux terminal, but you should be able to run it on a Windows Powershell
(preferred) or Command Prompt without problems, especially with the default.

* This program will create a .csv (default - definitions.csv) to store
mapping information and another file (default - usedrgbvalues.txt) to store used
rgb values

* You can supply a list of already used values as well, by telling the program
the name of that file. The file should be stored in the same directory as your
path.

* Depending on what your default python executable is, on most machines you will
either execute the program as 
  * `python3 psg.py [options]` OR
  * `python psg.py [options]`
  * Default options are supplied. Use `python psg.py -h` to learn what they are
and how to customize their values.

I hope you find this program useful!

This program is licensed under the GPLv2 only.
