import xlwt


file = xlwt.Workbook()


table = file.add_sheet('linuxea')

table.write(0,0,'老子成功写入')

file.save('C:/Users/Linux/Desktop/share/demo.xlsx')