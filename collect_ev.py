import os
import pandas as pd
from decimal import Decimal, getcontext

# 設定精度
getcontext().prec = 50

data_list = []
N = 2
n = N - 1

# 定義資料夾名稱
folder_name = f"eigenstate{N}"
# 如果資料夾不存在，則創建
os.makedirs(folder_name, exist_ok=True)

for i in range(N, 10001):
    file_name = f"energys/Energy{i}.csv"  
    try:
        # 使用 dtype=str 確保讀取的數據為字符串格式
        df = pd.read_csv(file_name, header=None, dtype=str)
        # 提取第一行數據並轉換為 Decimal
        first_row = df.iloc[n].apply(Decimal)
        data_list.append({'File Number': i, 'First Data': first_row.values[0]})
    except FileNotFoundError:
        print(f"檔案 {file_name} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 {file_name} 時發生錯誤: {e}")

# 創建 DataFrame，確保高精度
result_df = pd.DataFrame(data_list)

# 儲存檔案，保留高精度
output_file = os.path.join(folder_name, f'ev_of_es{N}.csv')
result_df.to_csv(output_file, index=False, float_format='%.50f')
print(f"結果已儲存至: {output_file}")