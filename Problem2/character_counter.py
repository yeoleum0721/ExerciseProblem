str = input('문자열을 입력하세요:')
find_chr = input('찾을 문자를 입력하세요: ')

num = 0
for i in range(len(str)) :
    if str[i] == find_chr :
        num+=1
    

print(f"문자 '{find_chr}'이 {num}번 나타납니다.")