def letterCombinations(digits):
    if not digits:
        return []
    
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    output = []

    def backtrack(index, string):
        if index == len(digits):
            output.append(string)
            return 
        for i in phone_map[digits[index]]:
            backtrack(index + 1, string + i)
        
    backtrack(0, "")
    return output


print(letterCombinations("234"))

