# define all the checks
def check_1(i):
    return True

def check_2(i):
    if i == 1:
        if s["5"] == 1:
            return True
        else: return False
    elif i == 2:
         if s["5"] == 3:
            return True
         else: return False
        
    elif i == 3:
         if s["5"] == 2:
            return True
         else: return False
        
    elif i == 4:
         if s["5"] == 4:
            return True
         else: return False
    
    
def check_3(i):
    if i == 1:
        if s["8"] != s["6"] == s["2"] == s["4"]:
            return True
        else: return False
    elif i == 2:
         if s["6"] != s["8"] == s["2"] == s["4"]:
            return True
         else: return False
        
    elif i == 3:
         if s["2"] != s["8"] == s["6"] == s["4"]:
            return True
         else: return False
        
    elif i == 4:
         if s["4"] != s["8"] == s["2"] == s["6"]:
            return True
         else: return False
            
def check_4(i):
    if i == 1:
        if s["2"] == s["7"]:
            return True
        else: return False
    elif i == 2:
         if s["1"] == s["6"]:
            return True
         else: return False
        
    elif i == 3:
         if s["1"] == s["9"]:
            return True
         else: return False
        
    elif i == 4:
         if s["8"] == s["10"]:
            return True
         else: return False
            
def check_5(i):
    if i == 1:
        if s["8"] == i:
            return True
        else: return False
    elif i == 2:
         if s["4"] == i:
            return True
         else: return False
        
    elif i == 3:
         if s["9"] == i:
            return True
         else: return False
        
    elif i == 4:
         if s["7"] == i:
            return True
         else: return False
            
def check_6(i):
    if i == 1:
        if s["8"] == s["2"] == s["4"]:
            return True
        else: return False
    elif i == 2:
         if s["8"] == s["1"] == s["6"]:
            return True
         else: return False
        
    elif i == 3:
         if s["8"] == s["3"] == s["5"]:
            return True
         else: return False
        
    elif i == 4:
         if s["8"] == s["5"] == s["9"]:
            return True
         else: return False
            
def check_7(i):   
    if counter.index(min(counter)) + 1 == i:
        return True
    else: return False
    
def check_8(i):
    
    if i == 1:
        if s["5"] in [s["1"] - 1, s["1"] + 1]:
            return True
        else: return False
        
    elif i == 2:
         if s["4"] in [s["1"] - 1, s["1"] + 1]:
            return True
         else: return False
        
    elif i == 3:
         if s["7"] in [s["1"] - 1, s["1"] + 1]:
            return True
         else: return False
        
    elif i == 4:
         if s["9"] in [s["1"] - 1, s["1"] + 1]:
            return True
         else: return False

def check_9(i):
    
    switch = s["6"] == s["1"]
    
    if i == 1:
        return s["8"] == s["2"] ^ switch
        
    elif i == 2:
        return s["8"] == s["4"] ^ switch
        
    elif i == 3:
        return s["8"] == s["5"] ^ switch
        
    elif i == 4:
        return s["8"] == s["3"] ^ switch

def check_10(i):   
    if (max(counter) - min(counter)) == i:
        return True
    else: return False
    

if __name__ == "__main__":
    print("Looking for a solution...")
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                    for e in range(1, 5):
                        for f in range(1, 5):
                            for g in range(1, 5):
                                for h in range(1, 5):
                                    for i in range(1, 5):
                                        for j in range(1, 5):
                                            s = {str(i):x for i, x in zip(range(1, 11),
                                                                          [a, b, c, d, e, f, g, h, i, j])}

                                            counter = [sum([i == s[k] for k in s]) for i in range(1, 5)]
                                            if (check_1(s["1"]) and check_2(s["2"]) and check_3(s["3"])
                                                and check_4(s["4"]) and check_5(s["5"]) and check_6(s["6"])
                                                and check_7(s["7"]) and check_8(s["8"]) and check_9(s["9"])
                                                and check_10(s["10"])):

                                                print("Found one solution!\n" + str(s))
    print("Done!")