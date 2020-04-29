def Anagram(s1, s2): 
    s1 = s1.lower()
    s2 = s2.lower()
    if(sorted(s1)== sorted(s2)): 
        print(True)  
    else: 
        print(False)
  
