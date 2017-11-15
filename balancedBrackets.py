import sys

def bracketsMatched(b1, b2):
    if (b1 == '(' and b2 == ')'):
        return True
    elif (b1 == '[' and b2 == ']'):
        return True
    elif (b1 == '{' and b2 == '}'):
        return True
    else:
        return False

def isBalanced(s):
    brackets = []
    for char in s:
        if char=='(' or char =='[' or char =='{':
            brackets.append(char)
        if char==')' or char ==']' or char =='}':
            if(len(brackets) == 0):
                return "NO"
            if not bracketsMatched(brackets.pop(), char):
                return "NO"
    if(len(brackets) == 0):
        return "YES"
    else:
        return "NO"
         

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        print(result)
