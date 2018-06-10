'''
Created on 09-Nov-2017

@author: srava
'''
#http://pbpython.com/excel-pandas-comp-2.html

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
#from numpy import ma

df = pd.read_csv('rainfall_filtered.csv');
print(df.head(5))
maha = df[df["State"] == "MADHYA MAHARASHTRA"]
guj = df[df["State"] == "GUJARAT REGION"]
mad = df[df["State"] == "EAST MADHYA PRADESH"]
kar = df[df["State"] == "NORTH INTERIOR KARNATAKA"]


print(maha.head(), guj.head(),mad.head(), kar.head())

#mh = maha
#mh = maha[[str("Year"),"q1" , "q2", "q3","q4"]]
#mp = mad[[ str("Year"),"q1" , "q2", "q3","q4"]]
#gj = guj[[ str("Year"),"q1" , "q2", "q3","q4"]]
#ka = kar[[ str("Year"),"q1" , "q2", "q3","q4"]]
#print(mh)

plt.figure(1)
maha.plot(x="Year")
plt.title("maharastra rain fall rate quarterly ")
plt.xlabel("year")
plt.ylabel("Rain fall rate ")
plt.show()

plt.figure(2)
mad.plot(x="Year")
plt.title("Madhya Pradesh rain fall rate quarterly ")
plt.xlabel("year")
plt.ylabel("Rain fall rate ")
plt.show()

plt.figure(3)
guj.plot(x="Year")
plt.title("Gujarat rain fall rate quarterly ")
plt.xlabel("year")
plt.ylabel("Rain fall rate ")
plt.show()

plt.figure(4)
kar.plot(x="Year")
plt.title("Kanataka rain fall rate quarterly ")
plt.xlabel("year")
plt.ylabel("Rain fall rate ")
plt.show()


