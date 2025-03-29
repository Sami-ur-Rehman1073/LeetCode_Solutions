class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]


def decode(s):
    stack = Stack()
    num = ""
    
    for i in range(len(s)):
        x = s[i]
        string = ""
        
        if x.isdigit():  
            num += x
            if not s[i + 1].isdigit():
                stack.push(int(num))
                num = ""
        elif not x.isdigit():  
            if s[i] == "]":
                while True:
                    j = stack.pop()
                    if j == "[":
                        break
                    if j != "]":
                        string += j
                integer = stack.pop()
                for _ in range(integer):
                    stack.push(string)
            if s[i] != "]":
                stack.push(s[i])

    def output(stack):
        y = ""
        while not stack.is_empty():
            y += stack.pop()
        return y[::-1]  

    return output(stack)


print(decode("3[a2[c]]"))  
