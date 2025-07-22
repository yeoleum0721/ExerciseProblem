multiple_3 = [i for i in range(1,101) if i%3 ==0]

total = 0
num = len(multiple_3)

for a in multiple_3 :
    total +=a
print('1부터 100까지 3의 배수:', multiple_3)
print(f'3의 배수의 합: {total}')
print(f'3의 배수의 개수: {num}')