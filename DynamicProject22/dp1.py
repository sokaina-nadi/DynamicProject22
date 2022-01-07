import itertools
combin = []
test={}
time={}
sequence={}


def U(d,p,lst, currentTime):
    if (p[lst] + currentTime) > d[lst]:
        return 1
    else:
        return 0
def dynamic_function(jobs,p,d):

    for x in range (0,len(jobs)):
        test[(x,)]=U(d,p,x,0)
    for x in range (0,len(jobs)):
        time[(x,)]=d[x]
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
                h = test[temp] + U(d,p,a, time[temp])
                if (h < min):
                    min = h
                    sequence[j]=sequence[temp]+','+str(a)

                test[j] = min
                time[j]=time[temp]+p[a]

    last_sequence=sequence[j]
    number_of_latness=test[j]
    last_sequence=last_sequence.split(",")



    return last_sequence,number_of_latness
# file = open("P1_n10.txt","r")
# lines = file.readlines()
# jobs=[i for i in range(int(lines[0]))]
# print(jobs)
# p=[int(i) for i in lines[1].split("\t")]
# print(p)
# d=[int(i) for i in lines[2].split("\t")]
# print(d)

# last_sequence,number_of_latness=dynamic_function(jobs,p,d)
# print('the Maximum lateness will be',number_of_latness)
# print("the right sequence is:",last_sequence)
