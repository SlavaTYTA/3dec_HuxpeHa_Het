x=1
y=1
z=0
p=int(input('write p (2<p<=10)'))
print(p,'ичная таблица умножения')
for x in range(1,p-1):
    for y in range(1,p-1):
        z=(x*y//p)*10+(x*y)%p
        print(z)
