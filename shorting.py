get_list=input("Enter the values split by space :")
a=list(map(int, get_list.split()))
b=[]
def shortf():
    
    for i in range(len(a)):
      b.append(min(a))
      a.remove(min(a))
    
    print(b)
def spe():
    cg=[]
    lg=[]
    
    for item in b:
      if not cg or item == cg[-1]:
          cg.append(item)
      else:
          lg.append(cg)
          cg = [item]
    
    # Append the last group
    if cg:
      lg.append(cg)
    print("splited by quantity:")
    for l in lg:
      print(l)
      
shortf()
ask=input("do you want to split by quantity? (y/n):")
if ask=="y":
  spe()