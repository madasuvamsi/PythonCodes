__author__ = 'vamsi'
file="E:\\Python\\ipdata.txt"
emp_list=[]
with open(file) as fo:
    for rec in fo:
        if rec.__contains__("IPv6 Address"):
           emp_list.append(rec)
    str_value=emp_list[0]
    print(str_value[str_value.index(":")+1:].lstrip())


