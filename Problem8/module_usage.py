import datetime 
import random

current_date_time = datetime.datetime.now()
korean_weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
list_fruit = ['포도', '사과', '오렌지', '바나나', '딸기']

print('현재 날짜와 시간:', current_date_time)
weekday_index = current_date_time.weekday() # 0 (월) ~ 6 (일)
korean_weekday = korean_weekdays[weekday_index]
print(f'포맷된 날짜:{current_date_time.strftime("%Y년 %m월 %d일")} {korean_weekday}')
print('임의의 숫자:',random.randint(1,100))
print(f'임의의 실수: {random.random():.2f}')
print('임의의 리스트 요소:', random.choice(list_fruit))
random.shuffle(list_fruit)
print(list_fruit)