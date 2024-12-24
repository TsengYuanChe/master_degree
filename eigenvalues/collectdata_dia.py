import os
import pandas as pd
from decimal import Decimal, getcontext
import numpy as np

getcontext().prec = 50

data_list = []
N = 2
n = N - 1

def compute_ref(n):
    """
    根據公式計算 ref 值
    ref = 0.4 * n * (n + 2) + 2 / sqrt(10) / pi * sum(1 / (j + 1/2) for j in range(2*n + 2)) - 0.4222 / (n + 1)**0.98270
    """
    n = Decimal(n)  # 將 n 轉為 Decimal 類型以確保高精度
    term1 = Decimal('0.4') * n * (n + Decimal('2'))
    term2 = Decimal('2') / Decimal(np.sqrt(10)) / Decimal(np.pi) * sum(Decimal('1') / (Decimal(j) + Decimal('0.5')) for j in range(2 * int(n) + 2))
    term3 = Decimal('-0.4222') / (n + Decimal('1')) ** Decimal('0.98270')
    ref = term1 + term2 + term3
    return ref

ref_value = compute_ref(n)

folder_name = f"eigenvalues/datas_diagonal"
os.makedirs(folder_name, exist_ok=True)

for i in range(N, 10001):
    file_name = f"energys/Energy{i}.csv"  
    try:
        df = pd.read_csv(file_name, header=None, dtype=str)
        first_row = df.iloc[n].apply(Decimal)
        data_list.append({'File Number': i, 'First Data': first_row.values[0]})
    except FileNotFoundError:
        print(f"檔案 {file_name} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 {file_name} 時發生錯誤: {e}")

result_df = pd.DataFrame(data_list)

# 計算新欄位
result_df['Difference'] = result_df['First Data'].apply(lambda x: Decimal(x) - ref_value)
result_df['Log Difference'] = result_df['Difference'].apply(lambda x: Decimal(np.log(float(x))) if x > 0 else Decimal('NaN'))

# 儲存結果
output_file = os.path.join(folder_name, f'ev_of_es{N}.csv')
result_df.to_csv(output_file, index=False, float_format='%.50f')
print(f"結果已儲存至: {output_file}")