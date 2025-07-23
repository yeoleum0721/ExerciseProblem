x,y=(10,20)
a,b,c = [1,2,3]

def add_all_numbers(*args):

    total = 0
    for num in args:
        total += num
    return total

print(f'좌표 : x ={x}, y={y}')
print(f'리스트 언패킹 : a = {a}, b={b},c={c}')
print(f'가변 인수의 합: {add_all_numbers(10,20,30)}')

def print_keyword_arguments(**kwargs):
    output_parts = []
    for key, value in kwargs.items():
        output_parts.append(f"{key}={value}")

    print(f"키워드 인수들: {', '.join(output_parts)}")

# 함수 호출 시 키워드 인자들을 전달
print_keyword_arguments(name="김철수", age=25, city="서울")