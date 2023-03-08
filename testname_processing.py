#!/usr/bin/env python3

import re
import sys

with open(sys.argv[1]) as infile:
    name_dict = dict()
    text = ""
    for line in infile:
        m = re.search(r"(<.*>)(.*)(</.*>)", line)
        tag, name, end_tag = m.group(1), m.group(2), m.group(3)
        if not name_dict.get(name):
            name_dict[name] = 1
        else:
            name_dict[name] += 1
            name = f"{name}_{name_dict[name]}"
            
        print(f"#### {tag}{name}{end_tag}")
    
