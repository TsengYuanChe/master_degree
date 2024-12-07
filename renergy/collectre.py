import pandas as pd
from decimal import Decimal, getcontext

# 設定高精度
getcontext().prec = 50

# 讀取三個檔案
file1 = 'denergy/diagonalenergy6000.csv'
file2 = 'denergy/diagonalenergy8000.csv'
file3 = 'denergy/diagonalenergy10000.csv'

def read_file_with_precision(file_path, column_name):
    """讀取 CSV 文件，將指定的欄位轉換為 Decimal 高精度型別"""
    data = pd.read_csv(file_path, dtype=str)  # 以字串讀取，保留精度
    data[column_name] = data[column_name].apply(Decimal)  # 轉換為 Decimal 型別
    return data[['Eigenstate', column_name]]  # 僅保留所需欄位

# 讀取並處理每個檔案
data1 = read_file_with_precision(file1, 'Residual Energy').rename(columns={'Residual Energy': 'Residual Energy_6000'})
data2 = read_file_with_precision(file2, 'Residual Energy').rename(columns={'Residual Energy': 'Residual Energy_8000'})
data3 = read_file_with_precision(file3, 'Residual Energy').rename(columns={'Residual Energy': 'Residual Energy_10000'})

# 合併所有的 Eigenstate，並去重後排序，得到最長的 Eigenstate 列
all_eigenstates = pd.concat([data1['Eigenstate'], data2['Eigenstate'], data3['Eigenstate']]).drop_duplicates().sort_values(key=lambda x: x.astype(int))

# 建立一個新的 DataFrame，包含完整的 Eigenstate
final_data = pd.DataFrame({'Eigenstate': all_eigenstates})

# 使用 merge 方法合併數據
final_data = final_data.merge(data1, on='Eigenstate', how='left')
final_data = final_data.merge(data2, on='Eigenstate', how='left')
final_data = final_data.merge(data3, on='Eigenstate', how='left')

# 儲存為 CSV 文件
final_data.to_csv('renergy/merged_residual_energy.csv', index=False)
print("已成功儲存合併後的數據至 merged_residual_energy.csv")