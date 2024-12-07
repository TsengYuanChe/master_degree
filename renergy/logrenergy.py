import pandas as pd
from decimal import Decimal, getcontext
import numpy as np

# 設置高精度
getcontext().prec = 50

# 讀取 CSV 文件
input_file = 'denergy/diagonalenergy.csv'  # 原始文件名
data = pd.read_csv(input_file, dtype=str)

# 提取 eigenstate 和 residual energy 欄位，確保高精度
eigenstate = data['Eigenstate'].astype(int)
residual_energy = data['Residual Energy'].apply(Decimal)

# 平移 Residual Energy，使最小值為 0
min_energy = min(residual_energy)
adjusted_residual_energy = [energy - min_energy for energy in residual_energy]

# 計算 log(adjusted residual energy)
log_adjusted_residual_energy = []
for energy in adjusted_residual_energy:
    if energy > 0:
        log_adjusted_residual_energy.append(Decimal(np.log(float(energy))))
    else:
        log_adjusted_residual_energy.append(Decimal('-Infinity'))  # 對 0 的處理

# 新建 DataFrame
new_data = pd.DataFrame({
    'Eigenstate': eigenstate,
    'Residual Energy': residual_energy,
    'Adjusted Residual Energy': adjusted_residual_energy,
    'log(Adjusted Residual Energy)': log_adjusted_residual_energy
})

# 儲存為原始的輸出檔案
output_file = 'renergy/logre.csv'
new_data.to_csv(output_file, index=False)
print(f"結果已成功儲存至: {output_file}")