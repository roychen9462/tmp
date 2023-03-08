#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1], 'r') as infile:
    name_dict = dict()
    text = ""
    for line in infile:
        m = re.search(r"(<.*>)([0-9]+)=(.*)(</.*>)", line)
        tag, error_code, node_name, end_tag = m.group(1), m.group(2), m.group(3), m.group(4)
        if not name_dict.get((error_code, node_name)):
            name_dict[(error_code, node_name)] = 1
        else:
            name_dict[(error_code, node_name)] += 1
            
    duplicat_code = []
    for key, val in name_dict.items():
        if val > 1:
            duplicat_code.append(int(key[0]))
    print(duplicat_code)
    
