def firstUniqChar(s):
   characters = list(dict.fromkeys(s))
   for i in characters:
      if s.count(i) == 1:
        return s.index(i)

print(firstUniqChar("leetcode"))