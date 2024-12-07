import pandas as pd
from decimal import Decimal

# 讀取數據
file_path = 'renergy/merged_residual_energy.csv'
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Eigenstate'] = data['Eigenstate'].astype(int)
data['Residual Energy_10000'] = data['Residual Energy_10000'].apply(Decimal)

# 提取前 1987 筆數據並只保留兩列
subset_data = data[['Eigenstate', 'Residual Energy_10000']].iloc[:1987]

# 儲存為新的 CSV 文件
output_file = 'drfit/re10000_1987.csv'
subset_data.to_csv(output_file, index=False)
print(f"前 1987 筆數據已成功儲存至: {output_file}")