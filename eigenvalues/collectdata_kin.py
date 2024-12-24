import os
import pandas as pd
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

data_list = []
N = 2
n = N - 1

def compute_ref(n):
    """
    根據公式計算 ref 值：
    ref = 0.4 * n * (n + 2) + 0.20549 * ln(n + 1) + 0.5
    """
    n = Decimal(n)
    term1 = Decimal('0.4') * n * (n + Decimal('2'))
    term2 = Decimal('0.20549') * Decimal(math.log(n + Decimal('1')))  # 自然對數
    term3 = Decimal('0.5')
    return term1 + term2 + term3

ref_value = compute_ref(n)

# 建立資料夾
folder_name = f"eigenvalues/kinetic_data"
os.makedirs(folder_name, exist_ok=True)

for i in range(N, 10001):
    file_name = f"energys/Energy{i}.csv"
    try:
        df = pd.read_csv(file_name, header=None, dtype=str)
        eigenvalue = Decimal(df.iloc[n, 0])  # 提取對應的數值，並轉為 Decimal
        kinetic_diff = eigenvalue - ref_value
        log_kinetic_diff = Decimal(math.log10(abs(kinetic_diff))) if kinetic_diff != 0 else Decimal('-Infinity')

        data_list.append({
            'Matrix Size': i,
            'Eigenvalue': eigenvalue,
            'Kinetic Difference': kinetic_diff,
            'Log Kinetic Difference': log_kinetic_diff
        })
    except FileNotFoundError:
        print(f"檔案 {file_name} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 {file_name} 時發生錯誤: {e}")

result_df = pd.DataFrame(data_list)

output_file = os.path.join(folder_name, f'kinetic_of_es{N}.csv')
result_df.to_csv(output_file, index=False)
print(f"結果已儲存至: {output_file}")