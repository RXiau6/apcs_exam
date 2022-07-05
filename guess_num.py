num = list(map(int,input().split()))
num.sort(reverse=True)
max_num = 0
for i in num:
    # print (i,":")
    # print ("now max num is ",max_num,", and counting ",i," and has ",num.count(i))
    if (num.count(i)>max_num):
        max_num = num.count(i)
        # print ("max num is ",max_num)
# print (num,max(num))
# print (num.count(max_num),end=" ")
print (max_num,end=" ")
num = list(dict.fromkeys(num))
for i in num :
    print (i,end=" ")