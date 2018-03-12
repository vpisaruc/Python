#Бутолин Александр
#Защита строки

s=input('Введите строку: ')
s=s.split()
for i in range (len(s)):
    s[i]=list(s[i])
max=s[0]

for i in range (1,len(s)):
    if len(max)<len(s[i]):
        max=s[i]

for i in range (len(s)):
    if len(s[i])<len(max):
        for j in range (len(max)-len(s[i])):
            s[i].append(' ')

for i in range (len(s[0])):
    for j in range (len(s)):
        print(s[j][i],end=' ')
    print()
