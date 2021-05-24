import csv
import math
with open("data.csv", newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
totaldata=0

data=file_data[0]
for i in data:
    totaldata+=int(i)
num_data=len(data)    
mean=totaldata/num_data
#print(num_data)  
#print(mean)
square_list=[]
for num in data:
    a=int(num)-mean 
    a=a**2
    square_list.append(a)
sum=0
for n in square_list:
    sum+=n
result=sum/(len(data)-1)
SD=math.sqrt(result)
print(SD)

