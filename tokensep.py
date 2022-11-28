with open("sample.txt", 'r') as f:
    text = f.read()
print("The text is:\n")
print(text)
lines = 1; tabs = 0; spaces = 0; characters = 0; punc = 0
for ch in text:
    if ch == '\n':
        lines += 1
    elif ch == '\t':
        tabs += 1
    elif ch == ' ':
        spaces += 1
    elif ch == ',' or ch == '.' or ch == '?' or ch == '!':
        punc += 1
    characters += 1
print("\nCount:\nCharacters: %d, lines: %d, spaces: %d\ntabs: %d, punctuation: %d" % 
(characters, lines, spaces, tabs, punc))
