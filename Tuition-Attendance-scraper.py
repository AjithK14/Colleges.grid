from pandas import DataFrame
import pandas as pd
import numpy as np
import numpy
def method(arr):
    index = 0;
    ag = arr
    for r in arr:
        if not (str(r).replace(" ","")== ""):
            temp = "$" + str(ag[index])
            ag[index] = temp
        if r is None:
            ag[index] = " "
        index+=1
    return ag
def has(string,arr):
    for x in arr:
        if (str(x).lower() in str(string).lower()):
            return True
    return False
def getNum(string,arr):
    i = 0
    for x in arr:
        if (str(x).lower() in str(string).lower()):
            return i
        i += 1
    return 0
def repl(arr):
    hhh = 0
    for g in arr:
        if g is None or g == "-" or g=="nan":
            arr[hhh] = " "
        hhh += 1
    return arr
def appen(arr,num):
    light = arr
    for i in range(0,num):
        numpy.append(light, [" "])
    return light

writer1 = pd.ExcelFile("publicColleges+tuitions.xlsx")
df = writer1.parse("Sheet1")
arr = df.as_matrix()
index = 0
A = arr[:, 0]
puCOST_IN = arr[:, 1]
puCOST_OUT = arr[:, 2]
puLIVE = repl(arr[:, 3])
for s in A:
    A[index] = A[index].replace("-"," ")
    index += 1
reader1 = pd.ExcelFile("collegeGridLoans.xlsx")
df2 = reader1.parse("Sheet1")
arr2 = df2.as_matrix()
index = 0
B = arr2[:, 0] #big grid college names
writer2 = pd.ExcelFile("privateColleges+tuitions.xlsx")
df3 = writer2.parse("Sheet1")
arr3 = df3.as_matrix()
index = 0
G = arr3[:, 0]
prCOST_IN = arr3[:, 1]
prCOST_OUT = arr3[:, 2]
prLIVE = repl(arr[:, 3])
#Big grid college names: B
#public college names: A
#private college names: G
privateCostsIN = [None] * len(B)
publicCostsIN = [None] * len(B)
privateCostsOUT = [None] * len(B)
publicCostsOUT = [None] * len(B)
privateLive = [None] * len(B)
publicLive = [None] * len(B)
both_live = [None] * len(B)
both_costIN = [None] * len(B)
both_costOUT = [None] * len(B)
pubPriv = [None] * len(B)
print(prLIVE)
for streamline in A:
    if has(streamline,B):
        e = getNum(streamline,B)
        r = getNum(streamline,A)
        pubPriv[e] = "Public"
        publicCostsIN[e] = puCOST_IN[r]
        publicCostsOUT[e] = puCOST_OUT[r]
        both_costOUT[e] = puCOST_OUT[r]
        both_costIN[e] = puCOST_IN[r]
        if r < 701:
            publicLive[e] = puLIVE[r]
            both_live[e] = puLIVE[r]

for streamline in G:
    if has(streamline, B):
        e = getNum(streamline, B)
        r = getNum(streamline, G)
        if 0 <= e and e < len(B) and 0 <= r and r < len(B):
            pubPriv[e] = "Private"
            privateCostsIN[e] = prCOST_IN[r]
            privateCostsOUT[e] = prCOST_OUT[r]
            both_costOUT[e] = prCOST_OUT[r]
            both_costIN[e] = prCOST_IN[r]
            if r < 701:
                privateLive[e] = prLIVE[r]
                both_live[e] = prLIVE[r]
pubPriv = repl(pubPriv)
both_costIN = repl(both_costIN)
both_costOUT = repl(both_costOUT)
both_costIN = method(both_costIN)
both_live = method(both_live)
both_costOUT = method(both_costOUT)
df2['On-Campus Tuition'] = both_costIN
df2['Off-Campus Tuition'] = both_costOUT
df2['Housing'] = both_live
df2.loc[:, 10] = pd.Series(pubPriv, index=df2.index)
df = pd.DataFrame({'Public/Private': pubPriv, 'On-campus Tuition': both_costIN, 'Off-Campus Tuition': both_costOUT, 'Housing': both_live})
writer = pd.ExcelWriter('TEMMMPPPPPP.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheets = writer.sheets['Sheet1']
writer.save()
print(both_costOUT)
print(puCOST_OUT)


