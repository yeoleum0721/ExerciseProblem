num = int(input('몇 단을 출력할까요?'))

print(f'{num}단 구구단')
for i in range(10):
    print(f'{num} x {i} = {num*i}')