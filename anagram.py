class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Define a list for both strings, if a letter in s and t matches
        #pop out of list, at the end if both list are empty, return true
        #else false

        
        sort1 = sorted(s)
        sort2 = sorted(t)
        return sort1 == sort2


stack = []
print(stack)
stack.append("a")
print(stack)
stack.append("p")
print(stack)
stack.pop(stack.index("c"))
print(stack)
        

        

