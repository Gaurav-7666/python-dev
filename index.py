'''import calendar
x=calendar.month(2024,6)
print(x)
import datetime
print(datetime.datetime(2020,4,4,1,26,40) )'''
'''import re  
  
line = "Learn Python through tutorials on javatpoint";  
  
search_object = re.search( r' .*t? (.*t?) (.*t?)', line)  
if search_object:  
    print("search object group : ", search_object.group())  
    print("search object group 1 : ", search_object.group(1))  
    print("search object group 2 : ", search_object.group(2))  
else:  
    print("Nothing found!!")'''
'''import json
x = {
  "Name": "John",
  "Age": 30,
  "Marrige": True,
  "Post": {
    "Title": "Internship",
    "Location": "Bangalore",
    "Exprioncode": "Python",
  }  
}
print(json.dumps(x , indent=4, sort_keys=True))'''
'''from googlesearch import search
query="who is the president of india."
for j in search(query,num_results=2):
    print(j)'''
'''from os import listdir
import random

my_list = [1, 2, 3, 4, 5]
random_sample = random.sample(my_list,1, 3)
print(random_sample)  # Output: [3, 1]'''
'''from googlesearch import search

query = "python tutorial"
for j in search(query, num_results=2):
    print(j)'''
'''from googlesearch import search
qurery = "Taarak Mehta Ka Ooltah Chashmah"
for j in search(qurery, num_results=2):
    print(j)'''
'''import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
mid_row=arr[arr.shape[0]//2]
mid_col=arr[:,arr.shape[1]//2]
mid_ele=arr[arr.shape[0]//2,arr.shape[1]//2]
print(mid_row)
print(mid_col)
print(mid_ele)'''
import numpy
a=rendom.number(5,8,9)
print(a)






