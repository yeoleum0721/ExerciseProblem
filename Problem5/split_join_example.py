mystr = 'Python is awesome programming language'
split_mystr = mystr.split()
join_mystr_hypen = '-'.join(split_mystr)
upper_split_mystr = [word.upper() for word in split_mystr]
join_mystr_blink = ' '.join(upper_split_mystr)


print('원본 문자열: ', mystr)
print('분리된 단어들:',split_mystr)
print('하이픈으로 연결:',join_mystr_hypen)
print('대문자로 변환 후 공백으로 연결:', join_mystr_blink)