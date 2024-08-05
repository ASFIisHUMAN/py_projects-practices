fus=[0]
first_num=int(input("Enter the first number: "))
fus.append(first_num)
range_num=int(input("Enter the range: "))
for i in range(1,range_num-1):
     l=len(fus)
     fus.append(int(fus[l-1])+int(fus[l-2]))
print(fus)