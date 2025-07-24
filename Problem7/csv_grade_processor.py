student_grades = {'김철수': 85,'이영희':92  ,'박민수': 78, '최수진': 95}

filename = 'grades.csv'
total=0
count=0

with open(filename, 'w') as file :
    for student,grade in student_grades.items() :
        line=f'{student}:{grade}점'
        file.write(line+'\n')
        total += grade
        count+=1
    file.write(f'전체평균 : {total/count}점')

print('성적 분석 결과 :')
with open(filename,'r') as file:
    print(file.read())