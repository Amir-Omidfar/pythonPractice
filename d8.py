# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phonebook={}
for i in range(0,n):
    name,phonebook[name] = input().split()


while True:
    try:
        key=input()
    except EOFError:
        break
    if key in phonebook:
        print(key+"="+phonebook[key])
    else:
        print("Not found")





