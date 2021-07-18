import time
import math

def calc(x, code):
    equation = eval(code)
    return equation

def Integral(a, b, N, code, v):


    X = [0]*(N+1)
    Y = [0]*(N+1)
    delta = (b-a)/N
    X[0] = a
    i = 1
    while i < N+1 :
        X[i] = X[i-1] + delta
        i += 1
    sum = 0
    i = 0
    S = 0
    while i < N+1 :
        Y[i] = calc(X[i], code)
        if (i == 0) or (i == N):
            S += Y[i]
        else:
            sum += Y[i]
        i += 1
    if v == 1 :
        answer = (sum + S) * delta
    else:
        answer = ((S/2) + sum) * delta
    return answer

lim = list(map(int, input("Введите пределы интегрирования \n").split()))
a = lim[0]
b = lim[1]
n = int(input("Введите число разбиений отрезка [a;b] (чем больше - тем точнее ответ) \n"))
N = n

code = input("Введите математическое уравнение \n")
start_time = time.time()

ans = Integral(a, b, N, code, 1)
ans2 = Integral(a, b, N, code, 2)
a = str(a)
b = str(b)
print("Приближённое значение интеграла на отрезке от " + a + " до " + b + ", вычесленное методом прямоугольников, равно:")
print(ans)
print("Приближённое значение интеграла на отрезке от " + a + " до " + b + ", вычесленное методом трапеций, равно:")
print(ans2)



