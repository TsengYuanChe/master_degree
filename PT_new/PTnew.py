import numpy as np
import pandas as pd
from sympy import symbols, Sum, pi, Rational, Abs, Min, KroneckerDelta, lambdify

# 定義符號變數
k, l, j, n, m, R, M = symbols('k l j n m R M', integer=True, positive=True)
delta_kl = KroneckerDelta(k, l)

# 定義公式 f(k, l)
f = delta_kl * (k * (k + 2)) / (M * R**2) + ((-1)**(k + l)) / (pi * R) * Sum(1 / (j + Abs(k - l) + Rational(1, 2)), (j, 0, 2 * Min(k, l) + 1))
f_numeric = lambdify((k, l, M, R), f.doit(), 'numpy')

# 計算修正能量 Ecorr[n]
def calculate_Ecorr(n, Kmax, M, R, scale_factor=0.01):
    """
    計算修正能量 Ecorr[n]。

    參數:
        n (int): 態編號。
        Kmax (int): 截斷級數的最大項數。
        M (float): 質量。
        R (float): 半徑。
        scale_factor (float): 縮小擾動的比例。

    返回:
        float: 修正後的能量 Ecorr[n]。
    """
    f_nn = f_numeric(n-1, n-1, M, R)
    f_n0 = f_numeric(n-1, 0, M, R) * scale_factor  # 縮小影響
    E2 = 0.0
    for k in range(1, Kmax + 1):
        if k != n:
            f_kk = f_numeric(k-1, k-1, M, R)
            term = (f_n0**2) / (f_kk - f_nn + 1e-5)  # 正則化分母
            E2 += term
            print(n, k)
    Ecorr = f_nn + E2
    return Ecorr

# 參數設定
N = 10
M = 1.0
R = np.sqrt(10) / 2
Kmax = 10000
scale_factor = 0.0001

# 讀取 energy10000.csv
input_file = "energy10000.csv"
energy_data = pd.read_csv(input_file, header=None).squeeze()
energy_data = energy_data[:N].to_numpy()  # 取前 5 筆資料

# 計算 n = 1 到 5 的修正能量
results = []
for n in range(1, N + 1):
    Ecorr_n = calculate_Ecorr(n, Kmax, M, R, scale_factor)
    original_energy = energy_data[n-1]  # 對應的 energy10000.csv 資料
    diff = abs(original_energy - Ecorr_n)
    log_diff = np.log(diff) if diff > 0 else -np.inf  # 避免 log(0)
    results.append((n, original_energy, Ecorr_n, diff, log_diff))
    print(f"n={n}, Original={original_energy:.12f}, Ecorr={Ecorr_n:.12f}, Diff={diff:.12e}, Log(Diff)={log_diff:.12f}")

# 儲存結果到 CSV 文件
output_file = "PT_new/Ecorr_comparison.csv"
df = pd.DataFrame(results, columns=["n", "Original_Energy", "Ecorr", "Diff", "Log_Diff"])
df.to_csv(output_file, index=False)
print(f"結果已儲存到 {output_file}")