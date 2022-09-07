t= int(input())
y=0
y=y+(t%10)*100
t=t//10

y=y+(t%10)*10
t=t//10

y=y+t


print(y*2)