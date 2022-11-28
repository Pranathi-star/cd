operators = ['+', '-', '*', '/']

def printMap(d):
    for i in d:
        print(f'{i[0]} = {i[1]}')
    print()    
    
def codeOptimization(statements):
    d = []
    n = len(statements)
    copy = []
    
    for s in statements:
        temp = s.split('=')
        left = temp[0]
        right= temp[1]
        d.append([left, right])

    print('Statements:')
    printMap(d)
    #common subexpression
    for i in range(n-1):
        left, right = d[i][0], d[i][1]
        
        op1 = ''
        k = 0
        while k < len(right) and right[k] not in operators:
            op1 += right[k]
            k += 1
        if k == len(right):
            copy.append(i)
            continue
        op2 = right[k+1:] 
            
        flag = 0
        
        for j in range(i+1, n):
            left2, right2 = d[j][0], d[j][1]
            if right2 == right:
                if flag == 0:
                    d[j][1] = left

            if op1 == left2 or op2 == left2:
                flag = 1

    print('Step1: eliminating common subexpressions')
    printMap(d)
    
    #copy propagation
    for i in copy:
        left, right = d[i][0], d[i][1]
        for j in range(i+1, n):
            left2, right2 = d[j][0], d[j][1]
            temp = right2.replace(left, right)
            d[j][1] = temp

    print('Step2: copy propagation')
    printMap(d)

    #deadcode elimination
    ans = []
    for i in range(n):
        if i in copy:
            flag = 0
            left, right = d[i][0], d[i][1]
            for j in range(i+1, n):
                left2, right2 = d[j][0], d[j][1]
                if left in right2:
                    flag = 1
                    break
                
            if flag == 1:
                ans.append(d[i])
                
        else:
            ans.append(d[i])

    print('Step3: eliminating deadcode')
    printMap(ans)        

statements = [
    'x=e',
    'a=b+c',
    'b=a-d',
    'c=b+c',
    'd=a-d',
    'f=x*d'
]

codeOptimization(statements)
