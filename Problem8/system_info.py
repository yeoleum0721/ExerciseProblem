import os
import sys

print(f'현재 작업 디렉토리: {os.getcwd()}')
print(f'Python 버전: {sys.version}')
print(f'운영체제 :{sys.platform}')
print(f'환경 변수 PATH 일부:{os.environ.get('PATH')[:23]}')


directory_path = '/Users/username/documents'
file_name = 'report.txt'
file_extension = '.txt'

full_file_path = os.path.join(directory_path, file_name)
file_exists = os.path.exists(full_file_path)
print(f' - 디렉토리:{directory_path}')
print(f' - 파일명 : {file_name}')
print(f' - 확장자 : {file_extension}')
print(f'파일 존재 여부 : {file_exists}')