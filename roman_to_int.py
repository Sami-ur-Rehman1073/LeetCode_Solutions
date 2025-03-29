def roman_to_int(s):
    if s == "":
        return None
    hmap = {
    'I'   :   1,
    'IV'  :   4,
    'V'   :   5,
    'IX'  :   9,
    'X'   :  10,
    'XL'  :  40,
    'L'   :  50,
    'XC'  :  90,
    'C'   :  100,      
    'CD'  :  400,
    'D'   :  500,
    'CM'  :  900,
    'M'   :  1000,   
    }

    int_list = []
    for i in range(len(s)):
        if i != len(s)-1:
            if hmap[s[i]] < hmap[s[i+1]]:
                int_list.append(hmap[s[i]] *  -1)
            else:
                int_list.append(hmap[s[i]])
        else:
            int_list.append(hmap[s[i]])
    integer = sum(int_list)
    return integer

print(roman_to_int("LVIII"))
