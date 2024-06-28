import numpy as np
import matplotlib.pyplot as plt
import os

# 保存先のディレクトリを指定
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

'''-----------------------------------
連立方程式解法
-----------------------------------'''
#掃き出し法(ガウス・ジョルダン法)
def GaussJordan_method(solve_list, print_info=True):
    if print_info:
        print("与えられたリスト:",*solve_list, sep='\n')
    N = len(solve_list)

    result_list = [row[:] for row in solve_list]

    for i in range(0, N, 1):
        pivot = result_list[i][i]
        #print("\n", "pivot:", pivot, "\n")
        for j in range(i, N+1, 1):
            result_list[i][j] = result_list[i][j] / pivot

        #print(*result_list, sep='\n')
        #print('\n')

        for k in range(0,N,1):
            if (k-i) != 0:
                aik = result_list[k][i]
                #print("\n","aik:", aik, "\n")
                for j in range(i, N+1, 1):
                    result_list[k][j] = result_list[k][j] - aik*result_list[i][j]
        
            #print(*result_list, sep='\n')
            #print("\n")

    if print_info:
        print("解:")
        variables = {}
        for i in range(N):
            variables[f'x{i+1}'] = result_list[i][-1]
        for variable, value in variables.items():
            print(f"{variable} = {value}")

    return result_list, N

#反復法(ガウス・ザイデル法)
def GaussSeitel_method(solve_list, eps = 1e-4, max_iter = 30, print_info=True):
    if print_info:
        print("与えられたリスト:",*solve_list, sep='\n')
    N = len(solve_list)

    x = [0]*N
    y = [0]*N

    for i in range(0,N,1):
        x[i] = 1.0
    for i in range(0,N,1):
        y[i] = x[i]

    for k in range(max_iter):
        for i in range(0, N, 1):
            sum = 0
            for j in range(0, N, 1):
                if i != j:
                   sum += solve_list[i][j] * x[j]
            x[i] = (solve_list[i][N] - sum) / solve_list[i][i]
        
        q = 0
        for i in range(0, N ,1):
            q += abs(x[i] - y[i])
            y[i] = x[i]
        
        if(q < eps):
            if print_info:
                print("解:")
                for i, value in enumerate(x):
                    print(f"x{i} = {value}")
                print(f"反復回数: {k + 1} 回")
            return x, k+1
    
    if print_info:
        print("収束せず")
    return None, None  # 収束しなかった場合は None を返す

list3 = [
    [10,2,0,5],
    [4,10,6,4],
    [0,8,10,3]
]

print("数値解析前半課題")
print("\n【問1】")
#result_list = GaussJordan_method(list3)
GaussJordan_method(list3)

print("\n【問2】")
GaussSeitel_method(list3)

# ガウス・ジョルダン法の解
result_list, N = GaussJordan_method(list3, print_info=False)
gj_solution = [result_list[i][-1] for i in range(N)]

# ガウス・ザイデル法の解
x, N = GaussSeitel_method(list3, print_info=False)
gs_solution = x

# 誤差の計算
errors = np.abs(np.array(gj_solution) - np.array(gs_solution))

# 解の表示
print("\n")
print("ガウス・ジョルダン法の解:", gj_solution)
print("ガウス・ザイデル法の解:", gs_solution)
print("誤差:", errors)


'''-----------------------------------
はさみうち法
-----------------------------------'''
#はさみうち法
def bisection_method(f, a, b, eps=1e-6):
    # print("f(a)=", f(a))
    # print("f(b)=", f(b))
    if f(a) * f(b) >= 0:
        return ValueError("f(a)とf(b)の符号が同じです。")
    
    while (b - a) >= eps:
        midpoint = (a + b) / 2
        if f(midpoint) == 0:
            return midpoint
        if f(midpoint) * f(a) < 0:
            b = midpoint
        else:
            a = midpoint
    
    return (a + b) / 2

def bis_equation(lambda_value):
    return 1.25*np.sin(0.4*lambda_value)*np.sin(0.6*lambda_value)-lambda_value*np.sin(lambda_value)

# 初期区間設定
initial_intervals = [(2, 3), (4, 5), (6, 7)]

# 解を求める
roots = []
for a, b in initial_intervals:
    try:
        root = bisection_method(bis_equation, a, b)
        roots.append((a, b, root))
    except ValueError as e:
        roots.append((a, b, str(e)))

# 結果表示
print("\n【問3】")
for a, b, root in roots:
    if isinstance(root, float):
        print(f"初期区間 [{a}, {b}] での解: λ = {root}")
    else:
        print(f"初期区間 [{a}, {b}] での解: {root}")

# lambdaの範囲
lambda_range = np.linspace(-8*np.pi, 8*np.pi, 5000)

# 方程式のグラフをプロット
plt.plot(lambda_range, bis_equation(lambda_range), label='Equation: 1.25sin(0.4λ)sin(0.6λ) - λsin(λ)')
for a, b, root in roots:
    plt.scatter([a, b], [bis_equation(a), bis_equation(b)], color='red', label=f'Initial Points ({a}, {b})')
    if isinstance(root, float):
        plt.scatter(root, bis_equation(root), color='blue', label=f'Root λ ≈ {root:.2f}')
plt.xlabel('λ')
plt.ylabel('f(λ)')
plt.title('Graph of the Equation')
plt.grid(True)
plt.legend()
# グラフを保存
plt.savefig(os.path.join(output_dir, "bisection_method_multiple_roots.png"))
plt.close()

'''-----------------------------------
ニュートン法
-----------------------------------'''
#ニュートン法
def Newton_method(f, df, x0, eps, max_iterations=1000):
    x = x0
    iterations_data = []
    for i in range(max_iterations):
        fx = f(x)
        dfx = df(x)
        iterations_data.append((i+1, x ,fx))
        if abs(fx) < epsilon:
            return x, i+1, iterations_data
        x = x - fx / dfx
    raise ValueError("収束しませんでした")

def new_f(x):
    return x**2 - 5

def new_df(x):
    return 2*x

# 初期値と精度を設定
x0 = 300
epsilon=1e-6

# ニュートン法を適用して根を求める
print("\n【問4】")
root, iterations, iterations_data = Newton_method(new_f, new_df, x0, epsilon)

# 繰り返し数と解の精度の表を作成して表示
print(f"{'繰り返し数':<10}{'x':<20}{'f(x)':<20}")
for iteration, x, fx in iterations_data:
    print(f"{iteration:<10}{x:<20}{fx:<20}")

print(f"近似解: {root}, 繰り返し回数: {iterations}")

# 結果のコメント
print("\nコメント:")
print(f"初期値を {x0} に設定し方程式 x^2 - 5 = 0 の根を求めた結果")
print(f"近似解は {root} ")
print(f"収束には {iterations} 回の繰り返しが必要")
print(f"許容誤差 ε = {epsilon} を満たす精度")


'''-----------------------------------
最小二乗法
-----------------------------------'''
#最小二乗法
def LeastSquares_method(x, y):
    n = len(x)
    a = ((np.dot(x, y)- y.sum() * x.sum()/n)/
        ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum())/n
    return a, b

LSx = np.array([10, 15, 31, 42, 50, 62])
LSy = np.array([32.2, 39.8, 27.2, 24.2, 21.8, 19.3])

a, b = LeastSquares_method(LSx, LSy)

# 近似直線の式を出力
print("\n【問5】")
print(f"近似直線の式: y = {a}x + {b}")

# プロット
plt.scatter(LSx, LSy, color="k")
plt.plot([0, LSx.max()], [b, a * LSx.max() + b], color="r", label=f"y = {a:.2f}x + {b:.2f}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
#plt.show()
plt.savefig(os.path.join(output_dir, "least_squares_method.png"))
plt.close()