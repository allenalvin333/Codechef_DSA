# https://www.codechef.com/CCSTART2/problems/EXTRICHK

l = sorted(list(map(int,input().split(" "))))
if(l[2]<sum(l[:2])): print(len(set(l)))
else: print(-1)