import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import math
from scipy.optimize import curve_fit

# 設定高精度
getcontext().prec = 50

# 已知數據
indices = np.array([1, 2, 3, 4], dtype=float)
differences = [
    Decimal('-8.51110511e-05'),
    Decimal('-7.11372885e-05'),
    Decimal('-6.08515826e-05'),
    Decimal('-5.29925993e-05')
]

# 計算 -log10(差值)
log_differences = [-Decimal(math.log10(abs(float(diff)))) for diff in differences]

# 1. 二次多項式擬合
def quadratic_model(x, a, b):
    return a * x**2 + b

popt, pcov = curve_fit(quadratic_model, indices, [float(log_diff) for log_diff in log_differences])
a, b = [Decimal(coef) for coef in popt]

# 擬合公式
print(f"擬合公式: -log10(Difference) = {a} * index^2 + {b}")

# 計算擬合結果
fitted_log_differences = [float(quadratic_model(x, float(a), float(b))) for x in indices]

# 計算 R²
ss_res = sum((float(log_diff) - fitted) ** 2 for log_diff, fitted in zip(log_differences, fitted_log_differences))  # 殘差平方和
ss_tot = sum((float(log_diff) - np.mean([float(log_diff) for log_diff in log_differences])) ** 2 for log_diff in log_differences)  # 總平方和
r_squared = 1 - (ss_res / ss_tot)
print(f"R² = {r_squared:.10f}")

# 2. 模擬計算，逐步增加 index，直到 -log10(Difference) 超過 10
current_index = 1
while True:
    # 計算 -log10(Difference) 的值
    log_diff = a * Decimal(current_index)**2 + b
    if log_diff >= Decimal(10):  # 當超過目標值 10 時停止
        break
    current_index += 1

print(f"外插索引 (當 -log10(Difference) 接近 10): {current_index}")

# 3. 計算從 1 到 current_index 的差值總和
def difference_from_log(index):
    log_diff = a * Decimal(index)**2 + b
    diff = Decimal(10) ** (-log_diff)  # 反轉 log10 回到差值
    return -diff  # 確保是負值

# 計算總和
total_difference_sum = sum(difference_from_log(i) for i in range(1, current_index + 1))

# 加上 initial_coefficient
initial_coefficient = Decimal('0.20576932297854927')
final_coefficient = initial_coefficient + total_difference_sum

print(f"總和差值: {total_difference_sum}")
print(f"目標 Coefficient 值: {final_coefficient}")

# 4. 繪製原始數據與擬合結果
plt.scatter(indices, log_differences, label='(-log10(Difference))', color='blue')
fitted_curve = [float(a * Decimal(x)**2 + b) for x in range(1, current_index + 1)]
plt.plot(range(1, current_index + 1), fitted_curve, label=f'curve fitting (R²={r_squared:.10f})', color='red')
plt.axhline(y=10, color='green', linestyle='--', label='-log10(Difference) = 10')
plt.xlabel('Index')
plt.ylabel('-log10(Difference)')
plt.legend()
plt.title('Logarithmic Transformation of Differences with Quadratic Fit')
plt.grid(True)

# 儲存圖表
plt.savefig('log_difference_fit_quadratic.png', dpi=300, bbox_inches='tight')
plt.show()