grades={'김철수': 85 ,'이영희': 92, '박민수': 78, '최수진': 95}



for student,grade in grades.items() :
    print(f'{student} : {grade}점')

total = 0
for i in grades.values() :
    total += i

print(f'평균 점수 : {total/len(grades.values())}')