#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]

try:
    my_list = load_from_json_file("add_item.json")
except:
    my_list = []

for arg in args:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
