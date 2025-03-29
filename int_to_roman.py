def int_to_roman(num):
    hmap = {
                1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
            }

    reversed_keys = sorted(hmap.keys(), reverse=True)
    roman_string = ""
    i = 0
    while num != 0:
        if num >= reversed_keys[i]:
            roman_string += hmap[reversed_keys[i]]
            num = num - reversed_keys[i]
        if num < reversed_keys[i]:
            i = i + 1
    return roman_string

print(int_to_roman(3974))
