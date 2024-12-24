import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

# 讀取數據
file_path = 'fiteigenvalues/eigenvalue2/predict_values.csv'  # 修改為你的檔案路徑
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Matrix size'] = data['Matrix Size'].astype(int)
data['Eigenvalue 2'] = data['Eigenvalue 2'].apply(lambda x: Decimal(x) if x != 'nan' else np.nan)
data['Predict Value (x)'] = data['Predict Value (x)'].apply(lambda x: Decimal(x) if x != 'nan' else np.nan)

# 獲取 Predict Value (x) 的最後一個值
last_predict_value = data['Predict Value (x)'].iloc[-1]

# 計算 `Eigenvalue 2 - Predict Value (x)` 和 `log(Eigenvalue 2 - Predict Value (x))`
adjusted_values = []
log_values = []
for value in data['Eigenvalue 2']:
    if pd.notna(value):
        adjusted_value = value - last_predict_value
        adjusted_values.append(adjusted_value)
        # 計算對數，確保值為正數
        if adjusted_value > 0:
            log_values.append(Decimal(math.log10(adjusted_value)))
        else:
            log_values.append(np.nan)  # 對於無法計算的值填入 NaN
    else:
        adjusted_values.append(np.nan)
        log_values.append(np.nan)

# 建立新的 DataFrame
new_data = pd.DataFrame({
    'Matrix size': data['Matrix size'],
    'Eigenvalue 2': data['Eigenvalue 2'],
    'Adjusted Eigenvalue': adjusted_values,
    'Log(Adjusted Eigenvalue)': log_values
})

# 儲存為新的 CSV 文件
output_file = 'fiteigenvalues/eigenvalue2/eigenvalue2_data.csv'
new_data.to_csv(output_file, index=False)
print(f"結果已成功儲存至: {output_file}")