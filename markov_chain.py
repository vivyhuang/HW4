import numpy as np

def markov_chain(n, N):
    #random n-vector with entries equal to sum of 1
    p = np.random.rand(n)
    sum_of_p = np.sum(p)
    p = p/sum_of_p
    
    #random nxn matrix with the sum of each row equal to 1
    P = np.random.rand(n,n)
    sum_of_rows = np.sum(P, axis = 1)
    P = np.divide(P.T,sum_of_rows).T
    
    #computes the transition for N steps
    PT = p*(P**N)
    return PT

#calls on the markov_chain function
markov_chain(n = 5, N = 50)
    
    