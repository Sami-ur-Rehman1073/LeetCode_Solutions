def myAtoi(s):

    final_int = ""

    for i in s:
        if i.isdigit():
            final_int += i            
            continue
        if i == " " and final_int == "":
            continue
        if i == " " and final_int != "":
            break
        if i == "-" and final_int == "":
            final_int += i
            continue
        if i == "-" and final_int != "":
            break
        if i == "+" and final_int != "":
            break
        if i == "+" and final_int == "":
            final_int += i
            continue
        if not i.isdigit() and i != "-":
            break

    if final_int == "" or final_int == "-" or final_int == "+":
        return 0 

    if final_int == "":
        return 0  
    
    if int(final_int) < (- 2) ** 31: 
        return (- 2) ** 31
    
    if int(final_int) > (2 ** 31) - 1: 
        return (2 ** 31) - 1

    return int(final_int)

print(myAtoi("   +0 123"))   