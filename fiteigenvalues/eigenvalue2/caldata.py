import pandas as pd
import numpy as np
from decimal import Decimal, getcontext

# 設定高精度
getcontext().prec = 50

# 讀取數據
file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path, dtype=str)

# 提取 matrix size 和 eigenvalue 2 並轉換為高精度
matrix_size = data['State'].astype(int).rename('Matrix Size')
eigenvalue_2 = data['Eigenvalue 2'].apply(Decimal)

# 定義 curve fitting 的公式
# log(E - x) = -2.99367 * log(N) + -1.53109
# x = E - 10**(-2.99367 * log(N) + -1.53109)
def compute_x(eigenvalue, matrix_size):
    results = []
    for E, N in zip(eigenvalue, matrix_size):
        log_term = Decimal('-2.99367') * Decimal(np.log10(N)) + Decimal('-1.53109')
        x = E - Decimal(10) ** log_term
        results.append(x)
    return results

# 計算 predict value
predict_value = compute_x(eigenvalue_2, matrix_size)

# 計算 eigenvalue_2 - predict_value
difference = [eigen - pred for eigen, pred in zip(eigenvalue_2, predict_value)]

# 建立新的 DataFrame
result_df = pd.DataFrame({
    'Matrix Size': matrix_size,
    'Eigenvalue 2': eigenvalue_2,
    'Predict Value (x)': predict_value,
    'Difference (Eigenvalue 2 - Predict Value)': difference
})

# 儲存為 CSV
output_file = 'fiteigenvalues/eigenvalue2/predict_values.csv'
result_df.to_csv(output_file, index=False)
print(f"結果已儲存至: {output_file}")