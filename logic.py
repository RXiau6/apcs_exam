a = input().split()
op_and = False
op_or = False
op_xor = False
#convert to int
a = list(map(int,a))

#convert to boolean
for i in range(len(a)):
    if (a[i]>0):
        a[i]=True
    else:
        a[i]=False

#judge
if (a[0] & a[1] == a[2]):
    op_and = True
    print ("AND")
if (a[0] | a[1] == a[2]):
    op_or = True
    print ("OR")
if (a[0] ^ a[1] == a[2]):
    op_xor = True
    print ("XOR")

if (op_xor | op_or | op_and == 0):
    print ("IMPOSSIBLE")