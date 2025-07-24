from math import pi

def area_circle(radius):
    return pi * radius**2

def area_rec(width,length):
    return width*length

def factorial(num):
    if num > 0:
        return num*factorial(num-1)
    else :
        return 1

def G_com_divisor(num1,num2):
    big_num = 0
    if num1<=0 & num2<=0:
        print('실행할 수 없습니다')
        return 0
    else:
        if num1>=num2:
            big_num = num1
        else:
            big_num = num2

        Greatest = 0
        for number in range(1,big_num+1):
            if num1%number==0 &num2%number==0:
                Greatest = number

