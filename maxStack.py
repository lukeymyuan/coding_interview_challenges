# https://www.hackerrank.com/challenges/maximum-element/problem

stack = []
N = int(input())
for i in range(N):
    command = input()
    if command[0]=='1':
        stack.append(int(command.split( )[1]))
    elif command[0]=='2':
        stack.pop()
    elif command[0]=='3':
        print(max(stack))
