import pandas as pd
import yfinance as yf
import datetime
import talib

# x=[3,4,5,6]
# var=pd.Series(x,index=['a','s','d','f'],dtype='float')
# print(var)
# print(type(var))
# print(var[2])

# dic={'name':['python','c','c++','java'],'por':[12,13,14,15],'rank':[1,4,3,2]}
# var1=pd.Series(dic)
# print(var1)
# s1=pd.Series(12,index=[1,2,3,4,5,6,7])
# s2=pd.Series(12,index=[1,2,3,4])
# print(s1+s2)

# l=[1,2,3,4,5,6]
# var=pd.DataFrame(l)
# print(var)
# print(type(var))
# d={'a':[1,2,3,4,5],"s":[1,2,3,4,5]}
# print(pd.DataFrame(d))
# var1=pd.DataFrame(d,columns=['a'])
# print(type(var1))
# print(var1)
# e={'a':[1,2,3,4,5],"s":[1,2,3,4,5],'d':[1,2,3,4,5],1:[1,2,3,4,5]}
# var2=pd.DataFrame(e,columns=['a',1],index=['a','s','d','f','g'])
# print(type(var2))
# print(var2)
# print(var1['a'][3])


# startdate=datetime.datetime(2020,1,1)
# enddate=datetime.datetime(2023,1,1)
# data=yf.download('AAPL',start=startdate,end=enddate)
# data.drop('Adj Close',axis=1,inplace=True)
# print(data)
# data1=data['Close']
# print(data1)

# var=pd.DataFrame({'a':[1,2,3,4],'b':[5,6,7,8]})
# var['c']=var['a']+var['b']
# print(var)
# var1=pd.DataFrame({'a':[10,20,30,40],'b':[15,16,17,18]})
# var1['python']=var1['a']<=20
# var1['c++']=var1['b']>15
# var1['java'] = (var1['python'] == True) & (var1['c++'] == True)
# print(var1)

#delete and insert data in dataframe
#insert
# var=pd.DataFrame({'a':[1,2,3,4,5],'b':[9,8,7,6,5]})
# var.insert(1,'py',var['a'])
# var.insert(1,'cpp',[11,12,13,14,15])
# var['python_12']=var['a'][:3]
# print(var)

#delete
# var=pd.DataFrame({'a':[1,2,3,4,5],'b':[9,8,7,6,5],'c':[11,12,13,14,15]})
# print(var.pop('b'))
# print(var)

# del var['a']
# print(var)

#dropna/fillna
# startdate=datetime.datetime(2020,1,1)
# enddate=datetime.datetime(2023,1,1)
# data=yf.download('AAPL',start=startdate,end=enddate)
# data.drop('Adj Close',axis=1,inplace=True)
# data['Rsi']=talib.RSI(data['Close'],timeperiod=14)
# print(data.dropna()) #this doesn't contain the NaN function
# #here in the dropna function axis=1-column and axis=0 works for rows
# print(data.dropna(axis=1))
# data.dropna(how='any') #here we can pass any/all any deletes the value if one exist all deletes if all value exist.
# data.dropna(subset=['Rsi']) #this changes and deletes the value of the rsi column not the volume and other columns
# print(data)
# data1=yf.download('GOOGL',start=startdate,end=enddate)
# data1.drop('Adj Close',axis=1,inplace=True)
# data1['Rsi']=talib.RSI(data1['Close'],timeperiod=14)
# data1['Ema20']=talib.EMA(data1['Close'],timeperiod=20)
# print(data1.fillna('0'))
# print(data1)
# print(data1.fillna({'Rsi':50,'Ema20':0}))#perfectly working

#merge concat join append

# var1=pd.DataFrame({'a':[1,2,3,4],'b':[11,12,13,14]})
# var2=pd.DataFrame({'a':[1,2,3,4],'c':[21,22,23,24]})
# print(pd.merge(var2,var1,on='a'))
# print(pd.merge(var2,var1,how='inner'))
# print(pd.merge(var2,var1,how='left'))
# print(pd.merge(var2,var1,how='right'))
# print(pd.merge(var2,var1,how='outer'))

# sr1=pd.Series([1,2,3,4])
# sr2=pd.Series([11,21,31,41])
# print(pd.concat([sr1,sr2]))
# print(pd.concat([var1,var2],axis=1))

