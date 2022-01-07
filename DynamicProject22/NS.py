import copy

##SWAP OPERATOR
'''
Swap Operator (N1): The swap operator selects a pair of jobs πi and πj in the current sequence π of jobs, exchanges their positions
'''


def swap_operator(data):
    swap_result2 = []
    j = 0
    while j < len(data) - 1:
        for i in range(j, len(data) - 1):
            xs = copy.copy(data)
            xs[j], xs[i + 1] = xs[i + 1], xs[j]
            swap_result2.append(xs)
            i += 1
        j += 1
    return swap_result2


##INSERTION OPERATOR
'''
Insertion Operator (N2): For a given incumbent arrangement of jobs, the insertion neighborhood can be obtained by removing a job from its position and inserting it into another position.
'''


def insertion_operator(data):
    insertion_result = []
    j = len(data) - 1
    for i in range(0, len(data)):
        while j in range(0, len(data)):
            if (i != j):
                xi = copy.copy(data)
                a = xi.pop(i)
                xi.insert(j, a)
                insertion_result.append(xi)
                j -= 1
            else:
                j -= 1
        i += 1
        j = len(data) - 1
    return insertion_result


##2-OPT OPERATOR
'''
2-opt Operator (N3): The 2-opt is the most classical heuristic for the traveling salesman problem in which it removes two edges from the tour and reconnects the two paths created.
'''


def twpopt_operator(data):
    twoopt_result = []
    for i in range(0, len(data) - 1):
        for j in range(len(data) - 1, i + 2, -1):
            xs = copy.copy(data)
            xs[i + 1], xs[j - 1] = xs[j - 1], xs[i + 1]

            xs[i + 2:j - 1] = xs[j - 2:i + 1:-1]

            j -= 1
            twoopt_result.append(xs)
        i += 1
    return twoopt_result
