def prime_checker(num):
    if num<2 :
        return False
    for i in range(2,num) :
        if num%i == 0 :
            return False
        else :
            return True
        

num = int(input('숫자를 입력하세요:'))

if prime_checker(num) :
    print(f'{num}은 소수입니다')
else :
    print(f'{num}은 소수가 아닙니다')