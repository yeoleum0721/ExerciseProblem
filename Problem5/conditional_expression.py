score = 85
grade = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {grade}")

age = 17
message = "성인" if age >= 19 else "미성년자"
print(f'나이 : {age}, 상태 : {message}')


numbers = [1,2,3,10,42]
print(f'숫자들의 최대값: {max(numbers)}')

numbers2 = [-1,5,-6,12,8,23]
plus_numbers =list(filter(lambda x : x>0,numbers2))
print(f'양수들:{plus_numbers}')