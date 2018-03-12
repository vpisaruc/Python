a=list(map(int,input('Введите массив в одну строку: ').split()))
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]%2==0 and a[j+1]%2!=0:
            a[j],a[j+1]=a[j+1],a[j]

print(a)
