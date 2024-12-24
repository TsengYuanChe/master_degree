import pandas as pd
import numpy as np
from decimal import Decimal, getcontext

# 設定高精度
getcontext().prec = 50

# 讀取數據
file_path = 'energy10000.csv'
data = pd.read_csv(file_path, header=None, dtype=str)

# 將數據轉為 Decimal 類型以確保高精度
energy = data.applymap(lambda x: Decimal(x) if x != 'nan' else None).values

# 指定索引和參數
n = 1000  # 注意這裡的索引是從 0 開始
coe = Decimal('0.20559607769749079947273263691541492034021485093921')

# 計算預測能量
pre_energy = Decimal('0.4') * n * (n + Decimal('2')) + coe * Decimal(np.log(n + 1)) + Decimal('0.5')

# 獲取實際能量並計算差值
actual_energy = energy[n][0]  # 假設每一行的能量數據在第 0 列
difference = Decimal(actual_energy) - pre_energy

print(f"實際能量: {actual_energy}")
print(f"預測能量: {pre_energy}")
print(f"差值: {difference}")