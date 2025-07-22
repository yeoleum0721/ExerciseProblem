words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
long_word = ''
short_word= words[0]

for word in words :
    if len(long_word)<len(word) :
        long_word = word

for word in words :
    if len(short_word)>len(word) :
        short_word = word

print(f'단어목록 : {words}')
print(f'가장 긴 단어:{long_word}({len(long_word)}글자)')
print(f'가장 짧은 단어:{short_word}({len(short_word)}글자)')
