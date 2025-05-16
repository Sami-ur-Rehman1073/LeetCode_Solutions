class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
    
def backspaceCompare(s, t):
    stack_s = Stack()
    stack_t = Stack()

    for i in s:
        if i == "#" and not stack_s.is_empty():
            stack_s.pop()
        if i != "#":
            stack_s.push(i)

    for i in t:
        if i == "#"and not stack_t.is_empty():
            stack_t.pop()
        if i != "#":
            stack_t.push(i)
    
    s = "" ; t = ""
    while (not stack_s.is_empty()) or (not stack_t.is_empty()):
        if not stack_s.is_empty():
            s += stack_s.pop()
        if not stack_t.is_empty():
            t += stack_t.pop()
    
    return s[::-1] == t[::-1]
        



print(backspaceCompare("ab#c", "ad#c"))
    