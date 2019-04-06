a = int(input("enter the first no."))
b = int(input("enter the second no."))
c = int(input("enter the third no."))
d = int(input("enter the fourth no."))
e = int(input("enter the fifth no."))
if a >= b and c and d and e:
    print(f"{a} is the largest no.")
if b >= a and c and d and e:
    print(f"{b} is the largest no.")
if c >= b and a and d and e:
    print(f"{c} is the largest no.")
if d >= b and c and a and e:
    print(f"{d} is the largest no.")
if e >= b and c and d and a:
    print(f"{e} is the largest no.")
