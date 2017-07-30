from pandas import DataFrame
import pandas as pd
import xlsxwriter
file = open('collegeNames.txt', 'r')
arr = []
arr2 = []
#writer = pd.ExcelWriter('collegeGrid.xlsx', engine='xlsxwriter')
for line in file.readlines():
    string = str(line)
    print (string)
    if (len(string) > 2):
        arr.append(string[:string.find(" (")])
        arr2.append((string[string.find("("):]).replace("(", "").replace(")", ""))
df = pd.DataFrame({'Colleges': arr, 'Home pages': arr2})
writer = pd.ExcelWriter('collegeGrid.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheets = writer.sheets['Sheet1']
writer.save()
file.close()
