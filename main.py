cc = 1
print()
while True:
    lines = map(str, input().splitlines())
    for line in lines:
        print(f'{cc}. {line}', end='\n')
        cc+=1
