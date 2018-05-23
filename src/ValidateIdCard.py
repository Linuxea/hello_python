# coding=utf-8
import csv
import logging

logging.basicConfig(filename="idCardError.log", level="DEBUG")

with open(file="idcard.csv") as file:
    go_csv = csv.reader(file, delimiter=",")
    count = 0
    for line in go_csv:
        idCard = ','.join(line)
        year = int(idCard[6:10])
        if year < 1950 or year > 2018:
            count += 1
            logging.error(year)

    logging.info("总共有 %s 条" % count)
