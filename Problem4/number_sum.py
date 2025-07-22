total =0

while 1 :
    num = int(input('숫자를 입력하세요 (0을 입력하면 종료):'))
    if num == 0 :
        break;
    total +=num

print('입력된 숫자들의 합:', total)
