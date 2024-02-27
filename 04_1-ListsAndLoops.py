stream = [1.0,2,3.00,4,3.5,7.2,0.1,-8,-2.9]
# stream = [1.0,2,3.00,4,3.5,7.2,0.1,-8,-2.9,"END"]
intList = []
fltList = []

for num in stream:
    if type(num) is int:
        intList.append(num)
    else:
        fltList.append(num)

print(intList)
print(fltList)
