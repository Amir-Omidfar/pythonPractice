# Enter your code here. Read input from STDIN. Print output to STDOUT
def Wprint( myStr ):
    for j in range(0,len(myStr)):
        if (j%2 == 0):
            print(myStr[j], end='')
    print(" ",end='')
    for j in range(0,len(myStr)):
        if (j%2 == 1):
            print(myStr[j], end='')
    print()
    return


size=input()
size=int(size)
strs=[]
i=0
while (i<size):
    strs.append(input())
    i=i+1


i=0
while(i<size):
    Wprint(strs[i])
    i=i+1




