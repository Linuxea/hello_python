import xlrd


data = xlrd.open_workbook('C:/Users/Linux/Desktop/share/score.xlsx')

table = data.sheets()[0]

# table = data.sheet_by_index(0) #通过索引顺序获取


nrows = table.nrows

for i in range(nrows):
    print("%s" % (table.row_values(i)))
