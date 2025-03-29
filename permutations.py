def permute(nums):
    ans = [] ; sol = []

    def backtrack():
        if len(sol) == len(nums):
            ans.append(sol[:])
            return
        for i in nums:
            if i not in sol:
                sol.append(i)
                backtrack()
                sol.pop()
                
    backtrack()
    return ans 
        

print(permute([1, 2, 3]))  