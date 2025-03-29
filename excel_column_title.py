def convertToTitle(columnNumber):
     
    result = ""

    while columnNumber > 0:
        columnNumber -= 1
        remainder = columnNumber % 26
        result += chr(remainder+ ord("A"))
        columnNumber = columnNumber // 26

    return result[::-1]

    
print(convertToTitle(28))
