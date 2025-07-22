numbers = [10,20,30,40,50]

total = 0
for i in numbers :
    total += i

print(f'숫자들 : {numbers}')
print(f'합계 : {total}')
print(f'평균 : {total/len(numbers):.1f}')
