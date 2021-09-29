x=list (input ('Введите номер билета '))
y=int(len(x)//2)
z=sum(list(map(int,x[:y:])))
c=x[::-1]
q=sum(list(map(int,c[:y:])))
res=q==z
print(res)

