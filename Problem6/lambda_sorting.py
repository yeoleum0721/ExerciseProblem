info_studernt = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

print('학생 정보 : ', info_studernt)
print('이름순 정렬:', sorted(info_studernt, key = lambda x : x[0]))
print('점수순 정렬:',sorted(info_studernt, key = lambda x : x[1]))
print('점수 내림차순:',sorted(info_studernt, key = lambda x : x[0],reverse=True))

