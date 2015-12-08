#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Fix badly formatted json from finnish-namedays project.
# https://github.com/spedepekka/finnish-namedays
#
# Author: Jarno Tuovinen
#
# License: MIT
#

filename = "free-names.json" # Warning: The file will be overwritten

broken_lines = []
new_lines = []
# Start list
new_lines.append("[\n")
# Read broken lines
with open(filename) as f:    
    broken_lines = f.readlines()

for line in range (len(broken_lines)):
    if line != len(broken_lines)-1:
        # Add comma
        new_lines.append("\t{}".format(broken_lines[line].replace("\n", ",\n")))
    else:
        new_lines.append("\t{}".format(broken_lines[line]))

# End list
new_lines.append("]\n")
with open(filename, 'wb') as f:    
    f.writelines(new_lines)

print "Fixed"

