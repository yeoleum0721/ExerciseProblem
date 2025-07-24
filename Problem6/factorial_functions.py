def factorial1(num):
    if num > 0:
        return num*factorial1(num-1)
    else :
        return 1

def factorial2(num):
    total = 1
    for i in range(1,num+1) :
        total = total * i
    return total

print(f'5!(재귀) = {factorial1(5)}')
print(f'5!(반복) = {factorial2(5)}')
print(f'7!(재귀) = {factorial1(7)}')
print(f'7!(반복) = {factorial2(7)}')
