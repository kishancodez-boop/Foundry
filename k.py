# import pandas as pd
# df = pd.read_csv("data.csv")
# df = pd.read_excel("file.xlsx")
# import math as m
# print(type(m.nan))
# print((lambda x: x*x)(8))
from functools import reduce
l=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,l)
print(sum)
# f=filter(lambda x:x>2,l)
# print(list(f))