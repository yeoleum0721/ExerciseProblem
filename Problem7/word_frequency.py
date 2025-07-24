def count_func(listoftext):
    word_counts = {}
    for word in listoftext:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

filename = 'wort.txt'
text_to_write = '파이썬 파이썬 파이썬 프로그래밍 프로그래밍 언어 언어 배우기 쉬운 강력한'

with open(filename,'w') as file:
    file.write(text_to_write)

with open(filename,'r') as file :
    text = file.read()
    words=list(text.split())

print(f'단어 빈도 분석 결과:')
counting=count_func(words)
for k,v in counting.items() :
    print(f'{k}:{v}번')