keywords = ['int', 'float']

f = open('sample.txt', 'r')

print(f'{"Name": <15}{"Type": <20} Scope')
print(f'{"-":-<45}')

while True:
    c = f.read(1)
    
    if not c:
        break
    
    temp = ""
    while c != " ":
        temp += c
        c = f.read(1)
    
    if temp in keywords:
        c = f.read(1)
        temp2 = ''
        while c != " " and c != "(" and c != ',' and c != ')' and c != ';':
            temp2 += c
            c = f.read(1)
        
        if c == ' ' or c == ';':
            print(f'{temp2: <15}{temp: <20} Local')
        
        if c == '(':
            print(f'{temp2: <15}{"function": <20} Global')    
        
        if c == ',':
            print(f'{temp2: <15}{temp: <20} function parameter')
        
        if c == ')':
            print(f'{temp2: <15}{temp: <20} function parameter') 
