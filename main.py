#adarkatzir 209502293
import math
def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        return "Searching...."
    y= 5
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            return "Searching...."
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
p = lambda x:math.sin(2*math.e**(-2*x))/(2*x**3+5*x**2-6)
start=-1
end=1.2
while(start!=end):
    approx = secant(p, start, start+0.1, 50)
    start=start+0.1
    print(approx)