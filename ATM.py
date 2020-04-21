ac_bal = 150
am_ded = 0.5
max_time = ac_bal//10
for _ in range(max_time):
    am = int(input())
    if ac_bal < 10.5:
        print("you have very less funds to withdrawl\n Addfunds as soon as you can.")
        break
    elif am % 10 != 0: print("Transaction Error! try again")
    elif am > (ac_bal+0.5): print("Insufficient funds! try to enter lesser amount.")
    else: 
        ac_bal = ac_bal - (am+0.5)
        print(f"thank you! transaction successful.\nYour current balance is {ac_bal}.\nWill you like to make one more transaction")
        one_m = input()
        if one_m == "NO": 
            print("Please take your card, have a good day.")
            break
        else:
            continue
        
