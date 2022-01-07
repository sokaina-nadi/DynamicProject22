import copy
import random
import time
import NS as ns


##OBJECTIVE FUNCTION
def minET(data):
    t = 0
    cj = 0  # completion time
    totalET = 0
    for j in range(len(data)):
        pj = data[j][1]
        dj = data[j][2]
        aj = data[j][3]
        bj = data[j][4]

        sj = t  # start time
        cj = sj + pj  # completion time
        t = cj
        earliness = aj * max(0, dj - cj)
        tardiness = bj * max(0, cj - dj)

        totalET = totalET + earliness + tardiness

    return totalET


##NEIGHBOHOOD STRUCTURES
def N1(x):
    return ns.swap_operator(x)  # neighbors by swap operator
def N2(x):
    return ns.insertion_operator(x)  # neighbors by insertion operator
def N3(x):
    return ns.twpopt_operator(x)  # neighbors by 2-opt operator


##SET OF NS
NK = [N3, N1, N2]  # Shaking phase
NL = [N1, N3]  # Local search phase

"""##GETTING DATA
print("Enter the number of jobs to test (10 | 100 | 200 | 500):")
n = input()
data = rf.getData(n)
print(minET(data))"""
##INITIAL SOLUTION AT RANDOM
"""x = copy.copy(data)
random.shuffle(x)
print("solution initiale:", x)
print("minET(x)=", minET(x))"""


##RVNS
# improve the initial solution using RVNS
def RVNS2(data, timelimit):
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N3]  # Local search phase
    x = copy.copy(data)
    random.shuffle(x)
    timeout = time.time() + timelimit
    while time.time() < timeout:
        k = 0
        while k in range(len(NK)):
            # x': generate a sequence x' at random from the k-th neighborhood Nk(x) of x
            x_first = random.choice(NK[k](x))
            if time.time() >= timeout:
                break
            elif minET(x_first) < minET(x):
                x = x_first
                k = 0
            else:
                k += 1
    return x


##VND
# local search using VND
def VND(x):
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N3]  # Local search phase
    l = 0
    while l in range(len(NL)):
        # EXPLORATION OF NEIGHBORHOOD
        neighborhood = NL[l](x)  # create a list of all neighbors in the neighborhood NL[l] of x
        for i in range(len(neighborhood)):
            # x_best: find the best neighbor x' of x in NL(x)
            x_best = neighborhood[i]
            if minET(x_best) < minET(x):
                x = x_best
                l = 0
                i += 1
            else:
                l += 1
                i = 0
    return x


##GVNS
def GVNS2(x_improved, timelimit):
    timeout = time.time() + timelimit
    NK = [N3, N1, N2]  # Shaking phase
    NL = [N1, N3]  # Local search phase
    while time.time() < timeout:
        k = 0
        while k in range(len(NK)):
            # x'(x_first): generate a sequence x' at random from the k-th neighborhood Nk(x) of x
            x_first = random.choice(NK[k](x_improved))
            # x'' (x_seconde): the best neighborhood of x' in NL(x)
            x_second = VND(x_first)
            if time.time() >= timeout:
                break
            elif minET(x_second) < minET(x_improved):
                x_improved = x_second
                k = 0
            else:
                k += 1
    return x_improved, minET(x_improved)



