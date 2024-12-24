import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

# 讀取數據
file_path = 'alleigenvalues/all_eigenvalues10.csv'  # 修改為你的檔案路徑
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['State'] = data['State'].astype(int)
data['Eigenvalue 1'] = data['Eigenvalue 1'].apply(lambda x: Decimal(x) if x != 'nan' else np.nan)

# 計算 `Eigenvalue {1} - 0.5`、`log(Eigenvalue {1} - 0.5)` 和 `log(Eigenvalue 1)`
adjusted_values = []
log_adjusted_values = []
log_values = []

for value in data['Eigenvalue 1']:
    if pd.notna(value):
        # 計算 `Eigenvalue 1 - 0.5`
        adjusted_value = value - Decimal('0.5')
        adjusted_values.append(adjusted_value)
        
        # 計算 `log(Eigenvalue 1 - 0.5)`
        if adjusted_value > 0:
            log_adjusted_values.append(Decimal(math.log10(adjusted_value)))
        else:
            log_adjusted_values.append(np.nan)  # 對於無法計算的值填入 NaN
        
        # 計算 `log(Eigenvalue 1)`
        if value > 0:
            log_values.append(Decimal(math.log10(value)))
        else:
            log_values.append(np.nan)  # 對於無法計算的值填入 NaN
    else:
        adjusted_values.append(np.nan)
        log_adjusted_values.append(np.nan)
        log_values.append(np.nan)

# 建立新的 DataFrame
new_data = pd.DataFrame({
    'Matrix size': data['State'],
    'Eigenvalue 1': data['Eigenvalue 1'],
    'Adjusted Eigenvalue': adjusted_values,
    'Log(Adjusted Eigenvalue)': log_adjusted_values,
    'Log(Eigenvalue 1)': log_values
})

# 儲存為新的 CSV 文件
output_file = 'fiteigenvalues/eigenvalue1/eigenvalue1_data.csv'
new_data.to_csv(output_file, index=False)
print(f"結果已成功儲存至: {output_file}")