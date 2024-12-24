import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

# 已知數據
indices = [1, 2, 3, 4]
differences = [
    Decimal('-8.51110511e-05'),
    Decimal('-7.11372885e-05'),
    Decimal('-6.08515826e-05'),
    Decimal('-5.29925993e-05')
]

# 計算 -log10(差值)
log_differences = [-Decimal(math.log10(abs(float(diff)))) for diff in differences]

# 1. 線性擬合
m, b = np.polyfit(indices, [float(log_diff) for log_diff in log_differences], 1)
m = Decimal(m)
b = Decimal(b)

# 擬合公式
print(f"擬合公式: -log10(Difference) = {m} * index + {b}")

# 2. 外插計算，尋找 -log10(Difference) 接近 10 的點
target_log = Decimal(10)
target_index = Decimal((target_log - b) / m)
target_index_int = int(target_index)  # 取整數部分
print(f"外插索引 (當 -log10(Difference) 接近 10): {target_index_int}")

# 3. 計算從 1 到 target_index 的差值總和
def difference_from_log(index):
    log_diff = m * Decimal(index) + b
    diff = Decimal(10) ** (-log_diff)  # 反轉 log10 回到差值
    return -diff  # 確保是負值

# 計算總和
total_difference_sum = sum(difference_from_log(i) for i in range(1, target_index_int + 1))

# 加上 initial_coefficient
initial_coefficient = Decimal('0.20576932297854927')
final_coefficient = initial_coefficient + total_difference_sum

print(f"總和差值: {total_difference_sum}")
print(f"目標 Coefficient 值: {final_coefficient}")

# 4. 繪製原始數據與擬合結果
plt.scatter(indices, log_differences, label='(-log10(Difference))', color='blue')
plt.plot(range(1, target_index_int + 1),
         [float(m * Decimal(i) + b) for i in range(1, target_index_int + 1)],
         label='curve fitting', color='red')
plt.axhline(y=float(target_log), color='green', linestyle='--', label='-log10(Difference) = 10')
plt.xlabel('Index')
plt.ylabel('-log10(Difference)')
plt.legend()
plt.title('Logarithmic Transformation of Differences')
plt.grid(True)

# 儲存圖表
plt.savefig('findingcoe/log_difference_fit.png', dpi=300, bbox_inches='tight')
plt.show()