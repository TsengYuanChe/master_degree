import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

# 讀取數據
coes = pd.read_csv('allpfit/a * np.log(x) + 0.5_with_diff.csv')

# 固定目標 Coefficient 值
target_coefficient = Decimal('0.20538607769749079947273263691541492034021485093921')

# 計算差值與其對數
differences = []
log_differences = []

for coef in coes['Coefficient']:
    # 確保計算高精度差值
    coef_decimal = Decimal(str(coef))
    difference = coef_decimal - target_coefficient
    differences.append(difference)

    # 計算對數差值，確保差值非零且正數
    if difference > 0:
        log_difference = Decimal(math.log10(float(difference)))
    elif difference < 0:
        log_difference = Decimal(math.log10(float(-difference)))  # 絕對值
    else:
        log_difference = np.nan
    log_differences.append(log_difference)

# 建立新的 DataFrame
new_df = pd.DataFrame({
    'Coefficient': coes['Coefficient'],
    'Difference': differences,
    'Log(Difference)': log_differences
})

# 儲存為新的 CSV 文件
output_file = 'findingcoe/coefficients.csv'
new_df.to_csv(output_file, index=False)
print(f"結果已成功儲存至: {output_file}")