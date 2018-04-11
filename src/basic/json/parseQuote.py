# coding=utf-8

import json

with open(file=r"C:\Users\Linux\Desktop\temp\quotes2.txt", encoding="utf-8") as file:
    for i in range(199):
        current_line = next(file)
        j_obj = json.loads(current_line)
        print("%12s --  %12s " % (j_obj.get("quote"), j_obj.get("author")))
