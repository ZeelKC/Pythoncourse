#fiboncci series
# 0 1 1 2 3 5 8 13 21 34 55 89 .....
n=int(input('Enter a number: '))
s=0
s1=1
for i in range (n):
    print(s)
    x=s1+s
    s=s1
    s1=x

print('Done!')   
