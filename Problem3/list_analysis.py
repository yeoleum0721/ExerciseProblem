numbers = [15, 3, 27, 8, 19, 12, 31]

a =list(set(numbers))

print(f'최댓값: {a[len(numbers)-1]}')
print(f'최솟값: {a[0]}')
print(f'두 번째로 큰 값: {a[len(a)-2]}')
