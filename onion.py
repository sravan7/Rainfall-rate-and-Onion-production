'''
Created on 08-Nov-2017

@author: srava
'''
#http://pbpython.com/excel-pandas-comp-2.html
#http://pbpython.com/excel-pandas-comp.html
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('onion.csv')
print( df.tail(5))
hyd = df[df["Centre_Name"]=="HYDERABAD"]

#chn = df[df["Centre_Name"]=="CHENNAI"]
hyd["Date"] = pd.to_datetime(hyd["Date"] )

#chn["Date"] = pd.to_datetime(chn["Date"])

#print("dth 2000", hyd[hyd['Date'] >= '01-01-2000'].head() )

hyd = hyd[(hyd["Date"] >= "01-01-1998") & (hyd["Date"] <= "12-31-2015")]
#chn = chn[(chn["Date"] >= "01-01-2000") & (chn["Date"] <= "03-30-2015")]
#print("hyderabd", hyd)

k = 1997
yearNo = []
q1 = []
q2 = []
q3 = []
q4 = []
for i in range(0,17) :
    k =k+1
    yearNo.append(k) 
    temp = (str(k)+"-"+"01"+"-"+"01" , str(k)+"-"+"03"+"-"+"30")
    q1.append(temp)
    q2.append(( str(k)+"-"+"04"+"-"+"01" , str(k)+"-"+"06"+"-"+"30" ) )
    q3.append(  (str(k)+"-"+"07"+"-"+"01" , str(k)+"-"+"09"+"-"+"30" ) )
    q4.append(( str(k)+"-"+"10"+"-"+"01" , str(k)+"-"+"12"+"-"+"30" ))
print(yearNo)   
q1m = []
q2m = []
q3m = []
q4m = []
print(q1)

g = hyd[(hyd["Date"] >= "1998-01-01") & (hyd["Date"] <= "1998-03-30")]["Price"]
print(hyd.head(5))
q = hyd[(hyd["Date"] >= "1998-04-01") & (hyd["Date"] <= "1998-06-30")]["Price"]


print(hyd.head(5))
#print(g.head(5))
print("g count", g.count())
print("q count", q.count())
print("2nd quarterv mean",g.max(), g.min(), g.mode() , g.count(), g.mean() )

print("q s", q.max(), q.min(), q.mode() , q.count(), q.mean())
    


for year in range(0,17) :
    #print(q1[year])
    #c = hyd[(hyd["Date"] >= q1[year][0] ) | (hyd["Date"] <= q1[year][1]) ]
    print(q1[year][0])
    print(q1[year][1])
    
    q1m.append(int( hyd[(hyd["Date"] >= q1[year][0] ) & (hyd["Date"] <= q1[year][1]) ]["Price"].mean() ) ) 
    
    #print("inside looop", hyd[(hyd["Date"] >= q1[year][0] ) | (hyd["Date"] <= q1[year][1]) ]["Price"].mean() )
    q2m.append( int( hyd[(hyd["Date"] >= q2[year][0] ) & (hyd["Date"] <= q2[year][1]) ]["Price"].mean()) )
    q3m.append( int( hyd[(hyd["Date"] >= q3[year][0] ) & (hyd["Date"] <= q3[year][1]) ]["Price"].mean() ))
    q4m.append(int( hyd[(hyd["Date"] >= q4[year][0] ) & (hyd["Date"] <= q4[year][1]) ]["Price"].mean() )) 
    #print(c)
print(q1m)
print(q2m)
print(q3m)
print(q4m)
file = open("mean.csv", "w")
file.write("year"+"," + "quarter1"+","+"quarter2"+","+"quarter3"+","+"quarter4"+ '\n')
for i in range(0,17) :
    #print(yearNo[i])
    #print(q1m[i])
    file.write( str(yearNo[i]) +","+str(q1m[i]) + ","+str(q2m[i]) + ","+str(q3m[i]) + ","+str(q4m[i]) + "," +'\n')

file.close()
data = pd.read_csv("mean.csv")

data.plot()
plt.title("quarterly price of Onions from 1998 - 2014")
plt.xlabel("year")
plt.ylabel("Price ")
plt.show() 