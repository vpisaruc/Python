# Бутолин ИУ7-12
print('Введите массив X: ')
X=list(map(int,input().split()))
r=int(input('Введите число которое вы хотите вставлять: '))
max=X[0]
s=0
for i in range (len(X)):
    if X[i] > max:
        max = X[i]
for i in range (len(X)):
    if X[i] == max:
        s+=1
i = 0
while i != len(X):
    if X[i] == max:
        X.insert(i,r)
        i+=1
    i+=1
print('Расширенный массив: ')
for i in range(len(X)):
    print(X[i],end=' ')
