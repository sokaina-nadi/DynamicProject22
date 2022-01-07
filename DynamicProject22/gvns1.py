import copy
import random
import time
import NS as ns

##OBJECTIVE FUNCTION
def f(data):
    t = 0
    u = 0
    for j in range(0,len(data)):
        s_j = t
        f_j = s_j + data[j][1]
        t = f_j

        if f_j>data[j][2]:
            u += 1
        else:
            u += 0
    return u

##NEIGHBOHOOD STRUCTURES
def N1(x):
    return ns.swap_operator(x)      # neighbors by swap operator
def N2(x):
    return ns.insertion_operator(x) # neighbors by insertion operator
def N3(x):
    return ns.twpopt_operator(x)    # neighbors by 2-opt operator

##SET OF NS
NK=[N3,N1,N2] #Shaking phase
NL=[N1,N2,N3] #Local search phase

"""##GETTING DATA
print("Enter the number of jobs to test (10 | 50 | 200 | 500):")
n = input()
data=rf.getData(n)
print(f(data))"""
##INITIAL SOLUTION AT RANDOM
"""x = copy.copy(data)
random.shuffle(x)"""
"""print("solution initiale:",x)
print("f(x)=",f(x))"""
def initialSolution(data):
    x = copy.copy(data)
    return random.shuffle(x)

##RVNS
#improve the initial solution using RVNS
def RVNS(data,timelimit):
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N2, N3]  # Local search phase
    x = copy.copy(data)
    random.shuffle(x)
    timeout = time.time()+timelimit
    while time.time() < timeout:
        k=0
        while k in range(len(NK)):
            # x': generate a sequence x' at random from the k-th neighborhood Nk(x) of x
            x_first = random.choice(NK[k](x))
            if time.time()>=timeout:
                break
            elif f(x_first)<f(x):
                x = x_first
                k = 0
            else:
                k+=1
    return x



##VND
#local search using VND
def VND(x):
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N2, N3]  # Local search phase
    l=0
    while l in range(len(NL)):
            #EXPLORATION OF NEIGHBORHOOD
            neighborhood = NL[l](x) #create a list of all neighbors in the neighborhood NL[l] of x
            for i in range(len(neighborhood)):
                # x_best: find the best neighbor x' of x in NL(x)
                x_best = neighborhood[i]
                if f(x_best)<f(x):
                    x = x_best
                    l = 0
                    i+=1
                else:
                    l+=1
                    i=0
    return x

##GVNS
def GVNS(x_improved,timelimit):
    timeout = time.time()+timelimit
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N2, N3]  # Local search phase
    while time.time() < timeout:
        k=0
        while k in range(len(NK)):
            # x'(x_first): generate a sequence x' at random from the k-th neighborhood Nk(x) of x
            x_first = random.choice(NK[k](x_improved))
            # x'' (x_seconde): the best neighborhood of x' in NL(x)
            x_second= VND(x_first)
            if time.time()>=timeout:
                break
            elif f(x_second)<f(x_improved):
                    x_improved = x_second
                    k = 0
            else:
                    k+=1
    return x_improved,f(x_improved)



###MAIN
"""print("________RVNS________")
x_improved = RVNS(x,30)
print("x initial improved by RVNS:",x_improved)
print("f(x_improved)=",f(x_improved))
'''
print("________VND________")
x_second= VND(x_improved)
print("Best x found by VND:",x_second)
print("f(x_second)=",f(x_second))
'''
print("________GVNS________")
x_optimal = GVNS(x_improved,120)
print("La solution optimale:",x_optimal)"""
