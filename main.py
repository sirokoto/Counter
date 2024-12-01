cc = 1
file_name = 'list.txt'
try:
    file = open(file_name, 'r')
    for line in file.readlines():
        print(f'{cc:}. {line:^20}')
        cc+=1
except FileNotFoundError:
    raise FileNotFoundError("File not found")