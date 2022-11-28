gram = {
	"E":["2E2","3E3","4"]
}
start = "E"
inp = "2324232$"

grammar = {
    "S":["S+S","S*S","i"]
    
}
start = "S"
inp = "i+i*i$"


stack = "$"
print(f'{"Stack": <15}{"Input Buffer": <15} Parsing Action')
print(f'{"-":-<50}')

while True:
    action = True
    
    i = 0
    while i < len(grammar[start]):
        if grammar[start][i] in stack:
            stack = stack.replace(grammar[start][i], start)
            print(f'{stack: <15}{inp: <15} Reduce S->{grammar[start][i]}')
            i =- 1
            action = False
                
        i += 1
             
    if len(inp) > 1:
    	stack += inp[0]
    	inp = inp[1:]
    	print(f'{stack: <15}{inp: <15} Shift')
    	action = False

    if inp == "$" and stack == "$"+start:
    	print(f'{stack: <15}{inp: <15} Accepted')
    	break

    if action:
    	print(f'{stack: <15}{inp: <15} Rejected')
    	break
