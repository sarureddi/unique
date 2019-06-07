num1=int(input())
num2=input().split()
num3=[]
num4=''
for i in num2:
    if num2.count(i)>1 and i not in num3:
        num3.append(i)
if len(num3)>0:
    for i in range(len(num3)-1):
        num4+=num3[i]+" "
    print(num4+num3[-1])
else:
    print("unique")
