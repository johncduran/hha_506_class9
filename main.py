import module1 as mod1

output1 = mod1.addition(5,10)
output2 = mod1.subtraction(5,10)

print('Output 1:', output1)
print('Output 2:', output2)

print(f"Output 1:{output1}")
print(f'Output 2:{output2}')

#imported here just these two functions since they were the only ones that we needed.


from module1 import addition, subtraction

output1 = addition(5,10)
output2 = subtraction(5,10)

print('Output 1:', output1)
print('Output 2:', output2)

print(f"Output 1:{output1}")
print(f'Output 2:{output2}')