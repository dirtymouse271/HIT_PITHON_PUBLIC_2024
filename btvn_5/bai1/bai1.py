Students = {
    "2023600784": 3.59,   
    "2023600785": 1.9,   
    "2023600786": 3.1,   
    "2023600787": 1.57,   
    "2023600788": 2.84,   
    "2023600789": 3.48,   
    }
countt = 0
for i in Students.values():
    if 3.0<= i <= 3.5:
        countt+=1
print(countt)
Students["2023600790"] = 2.89
canXoa = [key for key, value in Students.items() if value < 2.0]
for key in canXoa:
    del Students[key]
print(Students)
