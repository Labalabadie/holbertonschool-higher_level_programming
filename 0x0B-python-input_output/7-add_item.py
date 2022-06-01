#!/usr/bin/python3
"""Script, adds all args to a py list, then saves to file"""

import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []
list(my_list)
try:
    my_list = load_from_json_file("add_item.json")
except Exception:
    save_to_json_file(sys.argv[1:], "add_item.json")

my_list.append(sys.argv[1:])
save_to_json_file(my_list, "add_item.json")
