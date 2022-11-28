import queue


def insert_dot(prod, curr_state):
    q = queue.Queue()
    q.put(prod)

    visited = []
    while not q.empty():
        curr_rule = q.get()
        #print(curr_rule)
        curr_rule_split = curr_rule.split('->')
        left = curr_rule_split[0]
        right = curr_rule_split[1]
        dot_right = right.split('.')[1]
        if len(dot_right) > 0:
            char = dot_right[0]
            if ord(char) >= 65 and ord(char) <= 90 and char not in visited:
                visited.append(char)
                temp = rules_map[char]
                for p in temp:
                    q.put(f'{char}->.{p}')
                    curr_state.append(f'{char}->.{p}')

    return curr_state  

def slrparser(rules, exp_rules, rules_map, ss, non_terminals, terminals, terminals_map, non_terminals_map):
    curr_state = [f'X->.S']
    i = 0

    states = {}

    goto_map = {}

    curr_state = insert_dot('X->.S', curr_state)

    states[i] = curr_state

    q = queue.Queue()
    q.put(i)
    
    while not q.empty():
        curr_state_no = q.get()
        visited = {}
        for prod in states[curr_state_no]:
            p_split = prod.split('->')
            left = p_split[0]
            right = p_split[1]
            dot_split = right.split('.')
            dot_left = dot_split[0]
            dot_right = dot_split[1]
            if len(dot_right) > 0:
                new_p = left + '->' + dot_left + dot_right[0] + '.' + dot_right[1:]

                flag = 0

                '''
                if dot_right[0] in visited:
                    states[visited[dot_right[0]]].append(new_p)

                    #find state
                    find_state = states[visited[dot_right[0]]]
                    for st in states:
                        if states[st] == find_state:
                            del states[st]

                    flag = 1
                    i -= 1
                
                else:
                    curr_state = [new_p]
                    visited[dot_right[0]] = i

                    #expand non terminal after dot
                    curr_state = insert_dot(new_p, curr_state)
                    states[i] = curr_state
                    
                    i += 1
                    q.put(i)

                '''    

                for st in states:
                    if states[st][0] == new_p:
                        flag = 1
                        break

                if flag == 0:
                    curr_state = [new_p]
                    visited[dot_right[0]] = i

                    #expand non terminal after dot
                    curr_state = insert_dot(new_p, curr_state)
                    i += 1
                    states[i] = curr_state
                    q.put(i)

                goto_map[prod] = [dot_right[0], i]


    #print('states')
    #print(states)
    #print(goto_map)
    #print(non_terminals)
    #print(terminals)

    #parsing table
    print()
    print('Parsing Table:')
    columns = terminals + non_terminals
    r = len(states)
    c = len(columns)
    
    parsing_table = [[[] for j in range(c)] for i in range(r)]


    print('state', end = '  ')
    for t in columns:
        print(t, end = '   ')

    print()

    for sno in states:
        for prod in states[sno]:
            if prod in goto_map:
                #shift
                goto = goto_map[prod]
                symbol = goto[0]
                j = columns.index(symbol)
                state_no = goto[1]
                if symbol in terminals:
                    parsing_table[sno][j] = f'S{state_no}'
                else:
                    parsing_table[sno][j] = f'{state_no}'
            else:
                #reduce
                if sno == 1:
                    #accept
                    j = columns.index('$')
                    parsing_table[sno][j] = f'accept'     
                else:
                    cols = follow(prod[0], rules_map, follows)
                    for symbol in cols:
                        j = columns.index(symbol)
                        r_no = exp_rules.index(prod[:-1]) + 1
                        parsing_table[sno][j] = f'r{r_no}'
                        
       

    for i in range(r):
        print(i, end='      ')
        for j in range(c):
            if len(parsing_table[i][j]) == 0:
                print('- ',end='  ')
            else:
                print(parsing_table[i][j], end ='  ')
        print()

        

    
    
                

'''
rules=["E->E+T|T",
       "T->T*F|F",
       "F->(E)|id"]

exp_rules =["E->E+T",
            "E->T",
            "T->T*F",
            "T->F",
            "F->(E)",
            "F->id"]
'''


rules=["S->cAd",
       "A->ab|g"]

exp_rules =["S->cAd",
            "A->ab",
            "A->g"]
       

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

non_terminals_map = {}
for i in range(len(non_terminals)):
    non_terminals_map[non_terminals[i]] = i

print(rules)
#print(rules_map)
ss = 'S'

slrparser(rules, exp_rules, rules_map, ss, non_terminals, terminals, terminals_map, non_terminals_map)
