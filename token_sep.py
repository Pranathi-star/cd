keyword = ['break','case','char','const','countinue','deafult','do','int','else','enum','extern','float','for',
'goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['printf','scanf','main']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-','=','*=']
specialchars = ['@','#','$','_','!',',',':',';','\n','\t','{','}','(',')','[',']']
keywords_count = 0
operators_count = 0
strings_count = 0
constants_count = 0
special_chars_count = 0
identifiers_count = 0
f = open('lexical.txt', 'r')
while True:
  c = f.read(1)
  if not c:
    break
  if c.isdigit():
    temp = ''
    while c.isdigit() or c == '.':
      temp += c
      c = f.read(1)
    constants_count += 1
    print('constant:',temp)
  if c == '"':
    temp = ''
    c= f.read(1)
    while c != '"':
      temp += c
      c = f.read(1)
    strings_count += 1
    print('string:', temp)
  if ord(c) >= 97 and ord(c) <= 122:
    temp = c
    c = f.read(1)
    while ord(c) >= 97 and ord(c) <= 122:
      temp += c
      c = f.read(1)
    if temp in keyword:
      keywords_count += 1
      print('keyword:', temp)
    elif temp in built_in_functions:
      pass
    else:
      identifiers_count += 1
      print('identifier', temp)
  if c in operators:
    temp = ''
    while c in operators:
      temp += c
      c = f.read(1)
    operators_count += 1
    print('operator:',temp)
  if c in specialchars:
    special_chars_count += 1
    if c == '\n':
      print('Special Character: \\n')
    elif c== '\t':
      print('Special Character: \\t')
    else:
      print('Special Character:',c)
f.close()
print('Keywords:',keywords_count)
print('Operators:',operators_count)
print('Constants:',constants_count)
print('Identifiers:',identifiers_count)
print('Strings:',strings_count)
print('Special Characters:',special_chars_count)
