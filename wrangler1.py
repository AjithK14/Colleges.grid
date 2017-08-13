from pandas import DataFrame
import pandas as pd
import xlsxwriter
file = open('collegeNames.txt', 'r')
rates = open('collegeAcceptanceRate_Locations.txt', 'r')
variable = 0

arr = []
arr2 = []
#writer = pd.ExcelWriter('collegeGrid.xlsx', engine='xlsxwriter')
for line in file.readlines():
    string = str(line)
    #print (string)
    if (len(string) > 3):
        print(string + " " + str(len(string)))
        arr.append(string[:string.find(" (")])
        arr2.append((string[string.find("("):]).replace("(", "").replace(")", ""))
locations = [None] * len(arr)
college_percents = [None] * len(arr) #acceptance rate
for line in rates.readlines():
    if variable == 0:
        temp = str(line)
        name = temp[:temp.find("\t")]
        print(name)
        num = temp[temp.find("\t"):].replace(" ", "")
        print(num)
        try:
            position = arr.index(name)
            college_percents[position] = num
        except ValueError:
            locations.append(None)
            arr2.append(None)
            arr.append(name)
            college_percents.append(num)
        variable += 1
    elif variable == 1:
        light = str(line)
        light = light.rstrip()
        position = arr.index(name)
        locations[position] = light
        variable += 1
    else:
        variable = 0
df = pd.DataFrame({'Colleges': arr, 'Home pages': arr2, 'Locations': locations, 'Acceptance Rate': college_percents})
writer = pd.ExcelWriter('collegeGrid.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheets = writer.sheets['Sheet1']
writer.save()
file.close()
