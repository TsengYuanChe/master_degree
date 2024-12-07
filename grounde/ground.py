import pandas as pd
from decimal import Decimal, getcontext
import numpy as np

# 設定精度
getcontext().prec = 50

ref = Decimal(0.5)  # 高精度參考值
data_list = []

for i in range(1, 10001):
    file_name = f"energys/Energy{i}.csv"
    try:
        # 讀取檔案並處理第一行數據
        df = pd.read_csv(file_name, header=None, dtype=str)
        first_row = Decimal(df.iloc[0, 0])  # 提取第一行第一列並轉換為 Decimal

        # 計算數據並添加到列表
        data_list.append({'Matrix size': i, 'Lowest energy': first_row, 'Difference': first_row - ref, 'Log': np.log10(first_row - ref)})
    except FileNotFoundError:
        print(f"檔案 {file_name} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 {file_name} 時發生錯誤: {e}")

# 將結果轉換為 DataFrame 並儲存為 CSV
result_df = pd.DataFrame(data_list)
result_df.to_csv('grounde/lowestenergys.csv', index=False)
print("結果已成功儲存至 grounde/lowestenergys.csv")