counter: int = 1
file_name: str = 'list.txt'
try:
    file = open(file_name, 'r')
    for line in file.readlines():
        print(f'{counter}. {line}', end='')
        counter+=1
except Exception as e:
    #raise FileNotFoundError("File not found")
    print(f"Error: {e}")
