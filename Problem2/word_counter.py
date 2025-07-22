sentence = input("문장을 입력하세요:")

splited = sentence.split()
print('공백제거 : ', ' '.join(splited))
print(f'단어 개수 : {len(splited)}개' )