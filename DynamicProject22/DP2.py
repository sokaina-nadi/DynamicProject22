import itertools
import time
#step1 condition initial:
E={}
T={}
test={}
time={}
sequence={}
def dynamic_problem2(jobs,pi,di,alpha,beta):
    for x in range(0, len(jobs)):
        test[(x,)]=alpha[x]*max(0,di[x]-pi[x])+beta[x]*max(0,pi[x]-di[x])
    for x in range (0,len(jobs)):
        time[(x,)]=pi[x]
    for x in range (0,len(jobs)):
        sequence[(x,)]=str(jobs[x])
    for i in range(1,len(jobs)):
        for j in itertools.combinations(jobs, i + 1):
            tuplet=j
            min = 123456
            for k in range(i+1):

                a=tuplet[k]
                temp=list(tuplet).copy()
                temp.remove(a)
                temp=tuple(temp)
                h = test[temp] +alpha[a]*max(0,di[a]-time[temp]-pi[a])+beta[a]*max(0,time[temp]+pi[a]-di[a])
                if (h < min):
                    min = h
                    sequence[j] = sequence[temp] + ',' + str(a)
                test[j] = min
                time[j] = time[temp] + pi[a]
        last_sequence = sequence[j]
        number_of_latness = test[j]
    return last_sequence,number_of_latness

#Get Data
'''print("Enter the number of jobs to test (10 | 100 | 200 | 500):")
n = input()
file = open("Problem_2/DATA/P2_n"+n+".txt", "r")
lines = file.readlines()
jobs=[i for i in range(int(lines[0]))]
p=[int(i) for i in lines[1].split("\t")]
d=[int(i) for i in lines[2].split("\t")]
alpha=[int(i) for i in lines[3].split("\t")]
beta=[int(i) for i in lines[4].split("\t")]

last_sequence,number_of_latness=dynamic_problem2(jobs,p,d,alpha,beta)
print('the Maximum lateness will be',number_of_latness)
print("the right sequence is:",last_sequence)'''