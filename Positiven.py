#positive no. in given range
n=int(input('Enter range of list: '))
print('Enter the numbers')
x=[0 for i in range(n)]
for i in range(n):
    x[i]=int(input())
xp=[0 for i in range(n)]
xn=[0 for i in range(n)]
j=0
for i in range(n):

    if x[i]>0:
        xp[j]=x[i]
        j=j+1

print('Positive numbers are:\n')
for i in range(n):
  
    if xp[i]==0:
        break
    print(' ',xp[i], end=' ')
