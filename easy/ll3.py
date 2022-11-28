def first(left, rules_map):
    if ord(left) >= 65 and ord(left) <= 90:
        ans = []
        right = rules_map[left]
        flag = 0
        for p in right:
            if ord(p[0]) >= 65 and ord(p[0]) <= 90:
                temp = first(p[0], rules_map)
                if 'e' in temp:
                    ind = 0
                    flag = 1
                    while 'e' in temp:
                        temp.remove('e')
                        ind += 1
                        if ind < len(p):
                            temp += first(p[ind], rules_map)
                ans += temp 
                
            else:
                ans.append(p[0])
        
        if flag == 1:
            ans.append('e')          
       
        return list(dict.fromkeys(ans))  
    
    else:
        return [left]

def follow_helper(left, ind, p, follows, rules_map):
    if ind == len(p):
        if left in follows:
            temp = follows[left]
        else:
            temp = follow(left, rules_map, follows)
    else:
        temp = first(p[ind], rules_map)
    
    return temp
    
def follow(symbol, rules_map, follows):
    ans = []
    
    for left, right in rules_map.items():
        for p in right:
            ind = p.find(symbol)
            if ind != -1:
                if ind == len(p)-1:
                    if left in follows:
                        temp = follows[left]
                    else:
                        if symbol != left:
                            temp = follow(left, rules_map, follows)
                else:
                    temp = first(p[ind+1], rules_map)
                
                if 'e' in temp:
                    ind += 1
                    while 'e' in temp:
                        temp.remove('e')
                        ind += 1
                        if ind <= len(p):
                            temp += follow_helper(left, ind, p, follows, rules_map)
                        
                ans += temp    
                    
    return list(dict.fromkeys(ans))
           
def ll1parser(rules, rules_map, ss, non_terminals, terminals, terminals_map):
    firsts = {}
    for left in rules_map:
        ans = first(left, rules_map)
        print(f'FIRST({left}) = {ans}')
        firsts[left] = ans
        
    print()    
        
    follows = {}    
    for left in rules_map:
        ans = follow(left, rules_map, follows)
        if left == ss:
            ans = ['$'] + ans
        print(f'FOLLOW({left}) = {ans}')  
        follows[left] = ans
        
    print()
    print('Parsing Table:')
    print()
    
    #print(non_terminals)
    #print(terminals)
    #print(terminals_map)
    
    m = len(non_terminals)
    n = len(terminals)
    
    parsing_table = [[[] for j in range(n)] for i in range(m)]

    print('',end='     ')
    for t in terminals:
        print(t, end = '       ')

    print()    
    
    for i in range(len(non_terminals)):
        left = non_terminals[i]
        for p in rules_map[left]:
            ind = 0
            
            if p[0] != 'e':
                ts = first(p[0], rules_map)
            else:
                ts = follows[left]
            
            for t in ts:
                if t == 'e':
                    ind += 1
                    if ind < len(p):
                        ts += first(p[ind], rules_map)
                    continue
                j = terminals_map[t]
                parsing_table[i][j].append(f'{left}->{p}')
            
            if ind == len(p):
                ts = follows[left]
                for t in ts:
                    j = terminals_map[t]
                    parsing_table[i][j].append(f'{left}->{p}')
    
    #print(parsing_table)   
    
    for i in range(m):
        print(non_terminals[i], end='  ')
        for j in range(n):
            print(parsing_table[i][j], end =' ')
        print()    

rules=["S->ACB|Cbb|Ba",
       "A->da|BC",
       "B->g|e",
       "C->h|e"]
       
rules2 = ["E->TL",
          "L->+TL|e",
          "T->FM",
          "M->*FM|e",
          "F->(E)|i"]    

rules_map = {}
non_terminals = []
terminals = []

for rule in rules:
    temp = rule.split('->')
    left = temp[0]
    non_terminals.append(left)
    right = temp[1]
    parts = right.split('|')
    
    for p in parts:
        for s in p:
            if (ord(s) >= 65 and ord(s) <= 90) or s == 'e':
                pass
            else:
                if s not in terminals:
                    terminals.append(s)
                    
    rules_map[left] = parts

terminals.append('$')    

terminals_map = {}
for i in range(len(terminals)):
    terminals_map[terminals[i]] = i

print(rules)   
ss = 'S'
ll1parser(rules, rules_map, ss, non_terminals, terminals, terminals_map)
