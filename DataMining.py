__author__ = 'vamsi'

emp_list=[]
with open("C:\\Users\\vamsi\\Desktop\\SalesData.csv") as f:
    for rec in f:
            emp_list.append(rec.strip("\n\r").split(",")[1])
emp_list.pop(0)
print(set(emp_list))



