'''
원본 리스트: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
짝수들: [2, 4, 6, 8, 10]
짝수의 제곱: [4, 16, 36, 64, 100]

'''

numbers = [a for a in range(1,11)]
even_numbers = [b for b in numbers if b%2==0]
squared_even_numbers = [c**2 for c in even_numbers]

print('원본 리스트:', numbers)
print('짝수들', even_numbers)
print('짝수의 제곱:', squared_even_numbers)
