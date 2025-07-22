e_mail = input('이메일 주소를 입력하세요:')

user,domain = e_mail.split("@")


print(f'사용자명 : {user}')
print(f'도메인 : {domain}')