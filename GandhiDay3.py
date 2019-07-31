# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:31:07 2019

@author: STEM
"""

import math
dir(math)

dark = 5
milk = 6
white = 8
cadbury1 = "milk chocolate"
cadbury2 = "dark chocolate"
cadbury3 = "white chocolate"
print("The chocolate box contains",dark,cadbury2,",",milk,cadbury1,",and",white, 
      cadbury3)

chocolate1={"cadburymilk":5}
chocolate2={"cadburydark":8}
chocolate3={"cadburywhite":3}
print(chocolate1,chocolate2,chocolate3)

chocolatebox={"cadburymilk":5,"cadburydark":8,"cadburywhite":3}

person1={"steve":32}
person2={"lia":28}
person3={"vin":45}
person4={"katie":38}
people=[person1,person2,person3,person4]
people

people2={"steve":32,"lia":28,"vin":45,"katie":38}
studentgender={"steve":"M","lia":"F","vin":"M","katie":"F"}
studentlist=[["steve",32,"M"],["lia",28,"F"],["vin",45,"M"],["katie",38,"F"]]
studentlist


people2={"steve":32,"lia":28,"vin":45,"katie":38}
studentgender={"steve":"M","lia":"F","vin":"M","katie":"F"}
finallist = [people2,studentgender]
finallist

import pandas
dir(pandas)

studentdf=pandas.DataFrame(studentlist, columns=("name","age","gender"))
studentdf


#reference columns from dataframes
studentdf["name"]
studentdf["age"]

chocolatelist=[["milk",5],["dark",8],["white",3]]
chocolatelist
chocodf=pandas.DataFrame(chocolatelist,columns=("chocolate","quantity"))
chocodf

#reference columns from dataframes
chocodf["chocolate"]
chocodf["quantity"]

#create a dataframe of studentinfo
studentlist=[["steve",32,"M"],["lia",28,"F"],["vin",45,"M"],["katie",38,"F"]]
import pandas
studentlistdf=pandas.DataFrame(studentlist,columns=("name","age","gender"))

studentdf2=pandas.DataFrame(studentlist,columns=("name","age","gender"),
                            index=["1","2","3","4"])
studentdf2

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

studentbar=go.Bar(x=studentdf2["name"],y=studentdf2["age"])
plot([studentbar])


chocolatelist=[["milk",5],["dark",8],["white",3]]
chocodf=pandas.DataFrame(chocolatelist,columns=("chocolate","quantity"))
import plotly
from plotly.offline import plot
import plotly.graph_objs as go
chocolategraph=go.Bar(x=chocodf["chocolate"],y=chocodf["quantity"])
plot([chocolategraph])





































