def palindrome(inp):
    inp.lower()
    if inp == inp[::-1]:
        print("True")
    else:
        print("False")
