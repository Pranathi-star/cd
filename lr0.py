def findlr0(lhs, rhs, lr0):
    for i in range(len(rhs)+1):
        x = lhs + '->' + rhs[:i] + '.' + rhs[i:]
        lr0.append(x)
n=int(input("Enter the number of productions:"))
arr=[]
for i in range(n):
    arr.append(str(input()))
lr0 = []
for i in range(len(arr)):
    ip = arr[i]
    lhs, rhs = ip.split("->")
    productions = list(rhs.split("|"))
    for prod in productions:
        findlr0(lhs, prod, lr0)
print("LR(0) items for given production: ")
for i in range(len(lr0)):
    print(i,"->",lr0[i])
