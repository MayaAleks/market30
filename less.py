import functools

file = open('tx.txt', 'r')
#print(file)
#print(file.read())

s=0
n=0
for i in file:
    s+=int(i)
    n+=1
    print(s)
    print(n)
file.close()
file1=open('tx1.txt','w')
if n !=0:
    file1.write(str(s/n))
file1.close()







