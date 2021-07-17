stack = []
for i in range(5):
    stack.append(i)

print("Stack :" , stack)
TopNum =  stack.pop()
print("Stack.pop() : " , TopNum)

print("Next Stack : " , stack)
#The stack is updated as it is appended
print('Stack.peek()', stack[-1])
print('New stack : ', stack)