__author__ = 'vamsi'
county_list=[]
with open("C:\\Users\\vamsi\\Desktop\\FL_insurance_sample\\FL_insurance_sample.csv") as f:
    for record in f:
        county_list.append(record.split(",")[2])
county_list.pop(0)
unique_county=set(county_list)
print("Total No of Counties in Florida:",len(unique_county))
print(unique_county)
