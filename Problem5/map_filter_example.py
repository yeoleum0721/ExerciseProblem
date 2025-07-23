numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(x):
    return x * x

squared_numbers = list(map(square,numbers))
filtered_numbers = list(filter(lambda x : x > 5,numbers))

filtered_squared_numbers = list(map(square,filtered_numbers))

print()
print('원본 숫자: ', numbers)
print('모든 수의 제곱:', squared_numbers)
print('5보다 큰 수들: ' , filtered_numbers)
print('5보다 큰 수들의 제곱:', filtered_squared_numbers)

