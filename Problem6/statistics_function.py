import statistics as sta

def statistics(numbers) :
    average = sta.mean(numbers)
    max_numbers = max(numbers)
    min_numbers = min(numbers)
    std_numbers =sta.pstdev(numbers)

    print(f'숫자들:{numbers}')
    print(f'평균:{average}')
    print(f'최댓값:{max_numbers}')
    print(f'최솟값:{min_numbers}')
    print(f'표준편차:{std_numbers:.2f}')

statistics([10, 20, 30, 40, 50])