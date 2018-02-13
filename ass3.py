import re
import pandas as pd

import numpy as np
import preprocessing

file = open("C:\\Users\\Family Members\\Downloads\\wine.data","r")

for line in file :
	values = re.split(', |\n| ',line)

dataFrame = pd.io.parsers.read_csv('C:\\Users\\Family Members\\Downloads\\wine.data',header=None, usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12])

dataFrame.columns = [ 'Feature1', 'Feature2', 'Feature3', 'Feature4', 'Feature5','Feature6','Feature7','Feature8','Feature9','Feature10','Feature11','Feature12','Feature13']

print(dataFrame)


#Print maxes for each column
print ("================MAX==================")
print ("Feature 1: ",dataFrame['Feature1'].max())
print ("Feature 2: ",dataFrame['Feature2'].max())
print ("Feature 3: ",dataFrame['Feature3'].max())
print ("Feature 4: ",dataFrame['Feature4'].max())
print ("Feature 5: ",dataFrame['Feature5'].max())
print ("Feature 6: ",dataFrame['Feature6'].max())
print ("Feature 7: ",dataFrame['Feature7'].max())
print ("Feature 8: ",dataFrame['Feature8'].max())
print ("Feature 9: ",dataFrame['Feature9'].max())
print ("Feature 10: ",dataFrame['Feature10'].max())
print ("Feature 11: ",dataFrame['Feature11'].max())

print ("Feature 12: ",dataFrame['Feature12'].max())
print ("Feature 13: ",dataFrame['Feature13'].max())



#Print mins for each column

print ("=============MIN======================")
print ("Feature 1: ",dataFrame['Feature1'].min())
print ("Feature 2: ",dataFrame['Feature2'].min())
print ("Feature 3: ",dataFrame['Feature3'].min())
print ("Feature 4: ",dataFrame['Feature4'].min())
print ("Feature 5: ",dataFrame['Feature5'].min())
print ("Feature 6: ",dataFrame['Feature6'].min())
print ("Feature 7: ",dataFrame['Feature7'].min())
print ("Feature 8: ",dataFrame['Feature8'].min())
print ("Feature 9: ",dataFrame['Feature9'].min())
print ("Feature 10: ",dataFrame['Feature10'].min())
print ("Feature 11: ",dataFrame['Feature11'].min())

print ("Feature 12: ",dataFrame['Feature12'].min())
print ("Feature 13: ",dataFrame['Feature13'].min())


print ("===============STD=====================")

print ("Feature 1: ",dataFrame.loc[:,"Feature1"].std())

print ("Feature 2: ",dataFrame.loc[:,"Feature2"].std())

print ("Feature 3: ",dataFrame.loc[:,"Feature3"].std())

print ("Feature 4: ",dataFrame.loc[:,"Feature4"].std())

print ("Feature 5: ",dataFrame.loc[:,"Feature5"].std())
print ("Feature 6: ",dataFrame.loc[:,"Feature6"].std())

print ("Feature 7: ",dataFrame.loc[:,"Feature7"].std())

print ("Feature 8: ",dataFrame.loc[:,"Feature8"].std())

print ("Feature 9: ",dataFrame.loc[:,"Feature9"].std())

print ("Feature 10: ",dataFrame.loc[:,"Feature10"].std())

print ("Feature 11: ",dataFrame.loc[:,"Feature11"].std())

print ("Feature 12: ",dataFrame.loc[:,"Feature12"].std())

print ("Feature 13: ",dataFrame.loc[:,"Feature13"].std())


print ("=====================PERFORMING LAMBDA FUNCTIONS====================")



dataFrame['Feature1'] = dataFrame['Feature1'].apply(lambda x: x *9)

dataFrame['Feature2'] = dataFrame['Feature2'].apply(lambda x: x *9)

dataFrame['Feature3'] = dataFrame['Feature3'].apply(lambda x: x *9)

dataFrame['Feature4'] = dataFrame['Feature4'].apply(lambda x: x *9)

dataFrame['Feature5'] = dataFrame['Feature5'].apply(lambda x: x *9)

dataFrame['Feature6'] = dataFrame['Feature6'].apply(lambda x: x *9)

dataFrame['Feature7'] = dataFrame['Feature7'].apply(lambda x: x *9)

dataFrame['Feature8'] = dataFrame['Feature8'].apply(lambda x: x *9)

dataFrame['Feature9'] = dataFrame['Feature9'].apply(lambda x: x *9)

dataFrame['Feature10'] = dataFrame['Feature10'].apply(lambda x: x *9)

dataFrame['Feature11'] = dataFrame['Feature11'].apply(lambda x: x *9)

dataFrame['Feature12'] = dataFrame['Feature12'].apply(lambda x: x *9)

dataFrame['Feature13'] = dataFrame['Feature13'].apply(lambda x: x *9)



print("=====================ADJUSTED LAMBDA FUNCTIONed DATAFRAME========================")
print(dataFrame)
