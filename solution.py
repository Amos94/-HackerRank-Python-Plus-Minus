n = int(input())

arr = list(map(int, input().split()))
pos=0
neg=0
zero=0
for i in arr:
 if i>0:
  pos=pos+1
 elif i<0:
  neg=neg+1
 else:
  zero=zero+1
print("%.6f" % (pos/n))
print("%.6f" %(neg/n))

print("%.6f" %(zero/n))
