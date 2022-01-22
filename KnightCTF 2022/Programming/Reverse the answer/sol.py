
x = 1
a=0
while x!=544:
  
    calc=(x*(x+1)) + (2 *(x + 1))
    k=str(calc)
    x =x +1
    reversed_calc= k[::-1]
    reversed_calc=int(reversed_calc)
    if reversed_calc % 4 ==0:
       # print(x)
        a=a+reversed_calc
        


print(a)


