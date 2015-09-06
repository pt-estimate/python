import numpy as np

def matrix_factorization(R, K, steps=5000, alpha=0.0002, beta=0.02):
    N, M = R.shape
    P = np.random.rand(N,K)
    Q = np.random.rand(M,K)
    Q = Q.T
    for step in range(steps):
        for i in range(N):
            for j in range(M):
                if R[i][j] > 0:
                    e_ij = R[i][j] - np.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * e_ij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * e_ij * P[i][k] - beta * Q[k][j])
        eR = np.dot(P,Q)
        e = 0
        for i in range(N):
            for j in range(M):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * (pow(P[i][k],2) + pow(Q[k][j],2))
        if e < 0.001:
            break
    return P, Q.T