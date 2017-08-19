import requests
from bs4 import BeautifulSoup
import pdb
import pandas as pd

#print(requests.get("http://www.stateuniversity.com/rank/tot_enroll_rank/1").text)
with open("collegeGridEdited.xlsx","rb") as file:
	df=pd.read_excel(file)
df["2015 Enrollment"]=""
for page in range(1,26):
	print(page)
	soup=BeautifulSoup(requests.get("http://www.stateuniversity.com/rank/tot_enroll_rank/"+str(page)).text,'html.parser')
	lis=soup.find("table",class_="datatable").tbody.contents
	for elem in lis:
		#print(elem.name)
		if elem.name!=None:
			#pdb.set_trace()
			name=[i for i in elem.contents if i.name!=None][2].a.string
			size=[i for i in elem.contents if i.name!=None][3].string
			df.loc[df["Colleges"]==name,"2015 Enrollment"]=size
df.to_excel("collegeGridSizes.xlsx")
"""
Username:sh0012
Password:9MrGWDG8MbC
"""


	
	

