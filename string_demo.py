s1='Physics'
s2='my best subject is mathematics'

print(s1.upper())
print(s2.split()[-1])
print(s2.replace('t','k'))
print(s1.isalnum())
print(s1.isnumeric())
sp=s2.split()
for s in sp:
    print(s.capitalize(),end=' ')
print(s2.count('s'))

print(s2.endswith('s'))
print(s2.index('i'))
print(s2.split())
for i in range(len(s1)-1,-1,-1):
    print(s1[i])
j=len(s1)-1
while j>=0:
    print(s1[j].upper(),end="")
    j-=1