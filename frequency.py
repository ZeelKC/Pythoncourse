#frequency of letter
'''ex:  Mississippi
m=1 ; i=4 ; s=4 ; p=2
'''
import operator
def most_frequent():

  w=input("Enter the word or sentence:\n")
  d = dict()
  i=0
  for i in w:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1 
  return d

f=most_frequent()
s_f = dict( sorted(f.items(), key=operator.itemgetter(1),reverse=True))
print(s_f)


