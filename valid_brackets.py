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

def isValid(s):
    stack = Stack()
    for i in s:
        if i not in [")", "}", "]"]:
            stack.push(i)
        if i == ")":
            if stack.is_empty() is True:
                return False
            other_pair = stack.pop()
            if other_pair != "(":
                return False
        if i == "}":
            if stack.is_empty() is True:
                return False
            other_pair = stack.pop()
            if other_pair != "{":
                return False
        if i == "]":
            if stack.is_empty() is True:
                return False
            other_pair = stack.pop()
            if other_pair != "[":
                return False
    return True

print(isValid("([])"))
