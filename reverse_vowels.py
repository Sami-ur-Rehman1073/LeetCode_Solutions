def reverseVowels(s):
    str_list = list(s)
    vowels = ["a", "e", "i", "o", "u"]
    low = 0 ; high = len(str_list) - 1
    while low < high:
        while low < high and str_list[low].lower() not in vowels:
            low += 1
        while low < high and str_list[high].lower() not in vowels:
            high -= 1
        str_list[low], str_list[high] = str_list[high], str_list[low]
        low += 1
        high -= 1

    return "".join(str_list)
    



print(reverseVowels("leetcode"))