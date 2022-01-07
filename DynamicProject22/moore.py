### READ FROM A FILE ###
def moore1(lst):
    task_removed=[]
    concurrent_time=0
    S=[]
    a = sorted(lst,key=lambda x: x[2],reverse=False)
    for i in range (0,len(lst)):
            S.append(a[i])
            concurrent_time+=a[i][1]
            if (concurrent_time>  a[i][2]):
                index=max(S,key=lambda item: item[1])
                concurrent_time-=index[1]
                task_removed.append(index)
                S.remove(index)

    for i in range(len(task_removed)):
        task_removed_jobs=task_removed[i][0]
    num=len(task_removed)
    sequence=[]
    for i in range(0,len(S)):
        sequence.append(S[i][0])
    sequence.append(task_removed_jobs)

    return num,sequence


"""start=time()


file = open("P1_n10.txt","r")
lines = file.readlines()
i=1

'''fin = time.time() + 20'''

jobs=[i+1 for i in range(int(lines[0]))]
print(jobs)
print('______________')
print(jobs)
p=[int(i) for i in lines[1].split("\t")]
d=[int(i) for i in lines[2].split("\t")]

#data=list(zip(x,p,d))
data = [[jobs[i],p[i],d[i]] for i in range(len(jobs))]
print(data)

n = len(data)
print(n)
a,b=moore(data)
print('the Maximum lateness will be',a,)
print("the right sequence is:",b)
print("the time of my program is:",time()-start)"""