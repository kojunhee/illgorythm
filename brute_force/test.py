n=int(input())
untilnow=[]
for i in range(n):
    num,strike,ball=input().split()
    untilnow.append([int(num),int(strike),int(ball)])
numlist=[]
for i in range(111,1000):
    numlist.append(i)
newlist={}
for i in numlist:
    newlist[i]=0
for i in numlist:
    for j in untilnow:
        strike_c=0
        ball_c=0
        if str(int((i-i%100)/100)) in str(j[0]):
            if (i-i%100==j[0]-j[0]%100):
                strike_c+=1
            else:
                ball_c+=1
        if str(int((i%100-i%10)/10)) in str(j[0]):
            if (i%100-i%10==(j[0]%100)-j[0]%10):
                strike_c+=1
            else:
                ball_c+=1
        if str(i%10) in str(j[0]):
            if(i%10==j[0]%10):
                strike_c+=1
            else:
                ball_c+=1
        if strike_c==j[1] and ball_c==j[2]:
            newlist[i]+=1
answer=0
for i in newlist.keys():
    if(newlist[i]==len(untilnow)):
        answer+=1
print(answer)
