
def multiply(num1, num2):
    arrays = []
    a = []
    zero_count = 0
    for i in range(len(num2)-1, -1, -1):
        carry = 0
        for j in range(len(num1)-1, -1, -1):
            ans = int(num2[i]) *int(num1[j]) + carry
            if ans > 9:
                if j == 0:
                    a.append(ans % 10)
                    a.append(ans // 10)
                else:
                    carry = ans // 10
                    a.append(ans % 10)
            else:
                carry = 0
                a.append(ans)
        arrays.append(a[::-1])
        zero_count += 1
        a = [0] * zero_count

    resultant_arrs = []
    for i in range(len(arrays)):
        if len(arrays[i]) != len(arrays[len(arrays) - 1]):
            zero_count = len(arrays[len(arrays) - 1]) - len(arrays[i])
            zeros = [0] * zero_count
            y = zeros + arrays[i]
            resultant_arrs.append(y)
        else:
            resultant_arrs.append(arrays[i])
    
    total_sum = 0
    for i in resultant_arrs:
        num = ""
        for j in i:
            num += str(j)
        total_sum += int(num)
    return str(total_sum)


print(multiply("4", "4"))