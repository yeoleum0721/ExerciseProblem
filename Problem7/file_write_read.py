filename = 'text_file.txt'

lines_to_write = [
        "안녕하세요",
        "파이썬 파일 처리를 연습하고 있습니다",
        "오늘은 좋은 날씨입니다"
    ]

with open(filename, 'w') as file :
        for line in lines_to_write:
            file.write(line + '\n')

print('파일에 저장할 내용 :')
for line in lines_to_write:
            print(line)

print()

with open(filename, 'r') as file :
    read_content = file.read()
    print('파일에서 읽어온 내용')
    print(read_content)