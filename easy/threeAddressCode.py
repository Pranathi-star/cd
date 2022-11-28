Operators = ['+', '-', '*', '/', '(', ')', '^']

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3}

def printCode(st, output, no):
    a = st.pop()
    c1 = output.pop()
    c2 = output.pop()
    print(f't{no[0]} = {c2} {a} {c1}')
    newVar = f't{no[0]}'
    no[0] += 1
    output.append(newVar)
 
def threeAddressCode(exp):
    st = []
    output = []
    no = [1]

    for char in exp:
        
        if char not in Operators:
            output.append(char)

        elif char == '(':
            st.append('(')

        elif char == ')':
            while st and st[-1]!= '(':
                printCode(st, output, no)

            st.pop()

        else: 
            while len(st) > 0 and st[-1]!='(' and Priority[char] <= Priority[st[-1]]:
                printCode(st, output, no)

            st.append(char)

    while len(st) > 0:
        printCode(st, output, no)

exp = "a+b*(c^d-e)^(f+g*h)-i"

print(exp)
print()
print('Three Address Code:')
threeAddressCode(exp)
