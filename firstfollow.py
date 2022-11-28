#FIRST

rules={ "E":["TY"],
        "Y":["+TY","#"],
        "T":["FZ"],
        "Z":["*FZ","#"],
        "F":['(E)',"i"]}

fir={'E':[], 'Y':[], 'T':[], 'Z':[], 'F':[]}


def first(k,j):
    for i in rules[j]:
        if ord(i[0])<65 or ord(i[0])>90:
            fir[k].append(i[0])
        else:
            first(k,i[0])
            
for i in fir.keys():
    k=i
    first(k,i)
    
print("Firsts of all non terminals are: ")
for i,j in fir.items():
    print(i, " : ", j)

#FOLLOW

fol={'E':set(), 'Y':set(), 'T':set(), 'Z':set(), 'F':set()}

def follow(j):
    
    fol_1 = set()
    
    prods = rules.items()
    if j=='E':
        fol_1 = fol_1 | {'$'}
    for nt,rhs in prods:
        for alt in rhs:
            for char in alt:
                if char==j:
                    following_str = alt[alt.index(char) + 1:]
                    if following_str=='':
                        if nt==j:
                            continue
                        else:
                            fol_1 = fol_1 | follow(nt)
                    else:
                        if ord(following_str)<65 or ord(following_str)>90:
                            fol_2=set(following_str)
                        else:
                            fol_2 = set(fir[following_str])
                        if '#' in fol_2:
                            fol_1 = fol_1 | fol_2-{'#'}
                            fol_1 = fol_1 | follow(nt)
                        else:
                            fol_1 = fol_1| fol_2
    return fol_1

fol['E'] = fol['E'] | {'$'}
for i in fol:
    fol[i] = fol[i] | follow(i)
                
    
print('FOLLOW values of all non terminals are: ')
for i,j in fol.items():
    print(i, " : ", j)
