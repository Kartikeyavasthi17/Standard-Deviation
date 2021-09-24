import csv
import math

with open("data3.csv",newline='') as f:
    r_data=csv.reader(f)
    file_data=list(r_data)
    data=file_data[0]    

def mean(data):
    n=len(data)
    total=0

    for x in data:
        total+=int(x)

    mean=total/n

    return mean

squared_list=[]
for number in data:
    a=int(number)-(mean(data))
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum+=int(i)
    
result=sum/(len(data)-1)
std_daviation=math.sqrt(result)
print(std_daviation)  