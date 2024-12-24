import os
import pandas as pd
from decimal import Decimal, getcontext
import numpy as np

# 設定高精度
getcontext().prec = 50

# 設定資料夾名稱
folder_name = "alleigenvalues"
os.makedirs(folder_name, exist_ok=True)

# 初始化結果 DataFrame
result_df = pd.DataFrame({'State': range(1, 10001)})

# 遍歷每個 N
for N in range(1, 11):
    n = N - 1
    column_name = f'Eigenvalue {N}'  # 欄位名稱

    data_list = []
    for i in range(N, 10001):  # 改為從 N 開始
        file_name = f"energys/Energy{i}.csv"
        try:
            # 讀取檔案
            df = pd.read_csv(file_name, header=None, dtype=str)
            # 提取對應值，並轉為高精度 Decimal
            value = Decimal(df.iloc[n, 0])
            data_list.append(value)
        except FileNotFoundError:
            print(f"檔案 {file_name} 找不到，跳過該檔案")
            data_list.append(np.nan)  # 若檔案找不到，填入 NaN
        except Exception as e:
            print(f"讀取檔案 {file_name} 時發生錯誤: {e}")
            data_list.append(np.nan)

    # 補充缺失值以匹配行數
    data_list = [np.nan] * (N - 1) + data_list  # 在開頭補充 (N-1) 個 NaN

    # 確保 data_list 的長度與 result_df 相同
    if len(data_list) < 10000:
        data_list += [np.nan] * (10000 - len(data_list))

    # 將當前欄位加入到結果 DataFrame
    result_df[column_name] = data_list

# 儲存最終結果到 CSV
output_file = os.path.join(folder_name, 'all_eigenvalues10.csv')
result_df.to_csv(output_file, index=False, float_format='%.50f')
print(f"所有結果已儲存至: {output_file}")