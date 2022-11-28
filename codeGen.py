Operators = ['+', '-', '*', '/', '(', ')', '^']

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

assembly_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}

def printCode(st, output, no, tac, d):
    a = st.pop()
    c1 = output.pop()
    c2 = output.pop()

    if f'{c2}{a}{c1}' in d:
        output.append(d[f'{c2}{a}{c1}' ])
    else:
        tac.append(f't{no[0]}={c2}{a}{c1}')
        d[f'{c2}{a}{c1}'] = f't{no[0]}'
        newVar = f't{no[0]}'
        no[0] += 1
        output.append(newVar)
 
def threeAddressCode(exp):
    st = []
    output = []
    no = [1]
    tac = []
    d = {}

    for char in exp:
        
        if char not in Operators:
            output.append(char)

        elif char == '(':
            st.append('(')

        elif char == ')':
            while st and st[-1]!= '(':
                printCode(st, output, no, tac, d)

            st.pop()

        else: 
            while len(st) > 0 and st[-1]!='(' and Priority[char] <= Priority[st[-1]]:
                printCode(st, output, no, tac, d)

            st.append(char)

    while len(st) > 0:
        printCode(st, output, no, tac, d)

    return tac

def codeGen(tac):
    reg_map = {}
    reg_map2 = {}
    reg_no = 0
    
    for k in range(len(tac)):
        temp =tac[k].split('=')
        left = temp[0]
        right = temp[1]
        i = 0
        op1 = ''
        while(right[i] not in assembly_map):
            op1 += right[i]
            i += 1

        if op1 in reg_map:
            op1 = reg_map[op1]
            pass
        else:
            print(f'MOV {op1}, R{reg_no}')
            reg_map[op1] = f'R{reg_no}'
            reg_map2[f'R{reg_no}'] = op1
            reg_no += 1

        op = right[i]
        i += 1
        
        op2 = right[i:]

        if op2 in reg_map:
            op2 = reg_map[op2]

        if op1 not in reg_map:
            print(f'{assembly_map[op]} {op2}, {op1}')
        else:
            print(f'{assembly_map[op]} {op2}, {reg_map[op1]}')

        
        if op1 in reg_map2:
            temp = reg_map2[op1]
            reg_map2[op1] = left
            reg_map[left] = op1
            del reg_map[temp]
        else:   
            temp = reg_map2[f'{reg_map[op1]}']
            reg_map2[f'{reg_map[op1]}'] = left
            reg_map[left] = f'{reg_map[op1]}'
            del reg_map[temp]

        #last three address code
        if k == len(tac)-1:
            print(f'MOV {op1}, {left}')   
    
exp = "d=(a-b)+(a-c)+(a-c)"
print(exp)
print()

#Three Address Code 
print('Three Address Code:')
temp =exp.split('=')
left = temp[0]
right = temp[1]
tac = threeAddressCode(right)
last = tac[-1].split('=')
last[0] = left
last = '='.join(last)
tac.pop()
tac.append(last)
for i in tac:
    print(i)
print()

#Code Generation
print('Code Generation:')
codeGen(tac)
