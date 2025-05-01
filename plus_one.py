def plusOne(digits):
    result = []
    num = ""
    for i in digits:
        num += str(i)   
    x = int(num)
    x += 1
    for i in str(x):
        result.append(int(i))
    return result


print(plusOne([1,2,3]))
        