students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]
score_dict={}

for student,score in zip(students, scores) :
    print(f'{student}:{score}점')

score_dict=dict(zip(students,scores))


print('점수별 학생 딕셔너리:', score_dict)