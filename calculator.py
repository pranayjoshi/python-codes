l = 0
#a calculator program
print("what you want to do")
print("(a)= addition,(b)= subraction")
print("(c)= multiplication, (d)= division, (e) = end")
ans = input()
if ans == "a":
    print("enter two no.")
    b = int(input())
    c = int(input())
    l = b + c
if ans == "b":
    print("enter two no.")
    d = int(input())
    e = int(input())
    l = d - e
if ans == "c":
    print("enter two no.")
    f = int(input())
    g = int(input())
    l = f * g
if ans == "d":
    print("enter two no.")
    h = int(input())
    i = int(input())
    l = h / i
print(l)
if ans == "e":
    print("thank you!")