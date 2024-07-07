class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        """
        Personal Notes

        Create a stack, iterate through and check for <{[, if yes, push to stack
        If you find )}], try to find that same character in the stack, if not found
        return false
        """

        stack = []
        for i in s:
            if i == "{" or i == "(" or i == "[":  #Check if Stack is empty or if "[]" is top element in stack
                stack.append(i)

            elif i == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            
            elif i == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            
            elif i == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
        
        if len(stack) == 0: 
            return True
        else:
            return False


input = "{[]}"
input = "[{}]"
print("input: " + input)
print("expected: True")
print("output: " + str(Solution.isValid(input)))