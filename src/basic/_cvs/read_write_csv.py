# coding=utf-8
import csv

with open(file="go.csv") as file:
    go_csv = csv.reader(file, delimiter=",")
    for line in go_csv:
        print(','.join(line))

    with open(file="copy.csv", mode="w") as file:
        write_ = csv.writer(file, delimiter="=")
        write_.writerow(list(x * x for x in range(10)))
        write_.writerow(list(str(x) + "..." for x in range(10)))
