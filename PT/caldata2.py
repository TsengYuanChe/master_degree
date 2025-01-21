import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path, dtype=str)

matrix_size = data['State'].astype(int).rename('Matrix Size')
eigenvalue_1 = data['Eigenvalue 1'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_2 = data['Eigenvalue 2'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_3 = data['Eigenvalue 3'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_4 = data['Eigenvalue 4'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)

file_path2 = 'PT/10matrix_10states.csv'
data2 = pd.read_csv(file_path2, dtype=str)
EPT = data2['E']

E_1_inf = Decimal(EPT[1])
E_2_inf = Decimal(EPT[2])
E_3_inf = Decimal(EPT[3])
E_4_inf = Decimal(EPT[4])

# 初始化結果列表
adjusted_values_1 = []
adjusted_values_2 = []
adjusted_values_3 = []
adjusted_values_4 = []
log_adjusted_values_1 = []
log_adjusted_values_2 = []
log_adjusted_values_3 = []
log_adjusted_values_4 = []

# 計算 Adjusted 和 Log Adjusted 值
for value in eigenvalue_1:
    if pd.notna(value):
        adjusted_value = value - E_1_inf
        adjusted_values_1.append(adjusted_value)
        
        log_adjusted_values_1.append(Decimal(math.log10(abs(adjusted_value))))
        
    else:
        adjusted_values_1.append(np.nan)
        log_adjusted_values_1.append(np.nan)

for value in eigenvalue_2:
    if pd.notna(value):
        adjusted_value = value - E_2_inf
        adjusted_values_2.append(adjusted_value)
        
        log_adjusted_values_2.append(Decimal(math.log10(abs(adjusted_value))))
        
    else:
        adjusted_values_2.append(np.nan)
        log_adjusted_values_2.append(np.nan)
        
for value in eigenvalue_3:
    if pd.notna(value):
        adjusted_value = value - E_3_inf
        adjusted_values_3.append(adjusted_value)
        
        log_adjusted_values_3.append(Decimal(math.log10(abs(adjusted_value))))
        
    else:
        adjusted_values_3.append(np.nan)
        log_adjusted_values_3.append(np.nan)
        
for value in eigenvalue_4:
    if pd.notna(value):
        adjusted_value = value - E_4_inf
        adjusted_values_4.append(adjusted_value)
        
        log_adjusted_values_4.append(Decimal(math.log10(abs(adjusted_value))))
        
    else:
        adjusted_values_4.append(np.nan)
        log_adjusted_values_4.append(np.nan)

# 建立新的 DataFrame
new_data = pd.DataFrame({
    'Matrix size': matrix_size,
    'Eigenvalue 1': eigenvalue_1,
    'Adjusted Eigenvalue 1': adjusted_values_1,
    'Log(Adjusted Eigenvalue 1)': log_adjusted_values_1,
    'Eigenvalue 2': eigenvalue_2,
    'Adjusted Eigenvalue 2': adjusted_values_2,
    'Log(Adjusted Eigenvalue 2)': log_adjusted_values_2,
    'Eigenvalue 3': eigenvalue_3,
    'Adjusted Eigenvalue 3': adjusted_values_3,
    'Log(Adjusted Eigenvalue 3)': log_adjusted_values_3,
    'Eigenvalue 4': eigenvalue_4,
    'Adjusted Eigenvalue 4': adjusted_values_4,
    'Log(Adjusted Eigenvalue 4)': log_adjusted_values_4,
})

# 儲存為新的 CSV 文件
output_file = 'PT/eigenvalues_data2.csv'
new_data.to_csv(output_file, index=False, float_format='%.50f')
print(f"結果已成功儲存至: {output_file}")