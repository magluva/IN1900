import numpy as np
import matplotlib.pyplot as plt

def f(u, t):
    beta = 0.0005
    v = 0.1
    S, I, R = u
    return np.array([-beta*S*I, beta*S*I-v*I, v*I])

def rk4(f, u0, T, dt, terminate=None):
    n = int(T/dt)
    t = np.linspace(0, T, n+1)
    u = np.zeros((n+1, len(u0)))
    u[0] = u0
    for k in range(n-1):
        u[k+1] = advance(f, u, k ,t)
        if terminate(u, u0, k):
            print("Terminated!")
            break
    return u[:k+2], t[:k+2]

def advance(f, u, k, t):
    dt = t[k+1]-t[k]
    k1 = dt*f(u[k], t[k])
    k2 = dt*f(u[k]+(1/2)*k1, u[k]+(1/2)*dt)
    k3 = dt*f(u[k]+(1/2)*k2, u[k]+(1/2)*dt)
    k4 = dt*f(u[k]+k3, t[k]+dt)
    _u = u[k]+(k1+2*(k2+k3)+k4)/6
    return _u

def terminate_func(_u, u0, k):
    S, I, R = _u[:,0],_u[:,1], _u[:,2]
    S0, I0, R0 = u0
    tol = 1E-10
    res = abs((S0+I0+R0)-(S[k]+I[k]+R[k]))
    if res > tol:
        return True

S0 = 1500
I0 = 1
R0 = 0
T = 60
dt = 0.5
u0 = np.array([S0, I0, R0])

u, t = rk4(f, u0, T, dt, terminate=terminate_func)
plt.title("SIR")
plt.xlabel("time")
plt.ylabel("people")
plt.plot(t, u[:,0])
plt.plot(t, u[:,1])
plt.plot(t, u[:,2])
plt.legend(["S", "I", "R"])
plt.show()
