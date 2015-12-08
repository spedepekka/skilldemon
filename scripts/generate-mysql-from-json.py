#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Generate mysql dump from json file containing names.
#
# Author: Jarno Tuovinen
#
# License: MIT
#

input_filename = "free-names.json"
output_filename = "free-names.sql"

import json

orthodox_name_lines = []
unofficial_name_lines = []

with open(input_filename) as f:    
    data = json.load(f)
    for line in data:
        unofficial_names = line['unofficial_names']
        for name in unofficial_names:
            unofficial_name_lines.append(["{}".format(line['day']), "{}".format(line['month']), name])
        orthodox_names = line['orthodox_names']
        for name in orthodox_names:
            orthodox_name_lines.append(["{}".format(line['day']), "{}".format(line['month']), name])

with open(output_filename, 'wb') as f:    
    f.write("INSERT INTO orthodox_names (day,month,name) VALUES ")
    for line in range(len(orthodox_name_lines)):
        f.write("({},{},'".format(orthodox_name_lines[line][0], orthodox_name_lines[line][1]))
        f.write(orthodox_name_lines[line][2].encode('utf-8'))
        if line != len(orthodox_name_lines)-1:
            f.write("'),\n")
        else:
            f.write("')")
    f.write(";\n")

