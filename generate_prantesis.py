ans = []
def generate(open, close, n, sol = []):
    if open == close == n:
        final_sol = "".join(sol)
        ans.append(final_sol) 
        return      
    if open < n:
        sol.append("(")
        generate(open + 1, close, n, sol)
        sol.pop()
    if open > close:
        sol.append(")")
        generate(open, close + 1 , n, sol)
        sol.pop()

    return ans

print(generate(0, 0, 2))