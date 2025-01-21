import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path, dtype=str)

Einf = []
E_10000 = []

matrix_size = data['State'].astype(int).rename('Matrix Size')
eigenvalue_1 = data['Eigenvalue 1'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_2 = data['Eigenvalue 2'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_3 = data['Eigenvalue 3'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)
eigenvalue_4 = data['Eigenvalue 4'].apply(lambda x: Decimal(x) if pd.notna(x) else np.nan)


E_1_inf = Decimal(0.5)
E_2_inf = eigenvalue_2.min() - eigenvalue_1.min() + Decimal(0.5) - Decimal(0.17*10**(-12))
E_3_inf = eigenvalue_3.min() - eigenvalue_1.min() + Decimal(0.5) - Decimal(0.55*10**(-12))
E_4_inf = eigenvalue_4.min() - eigenvalue_1.min() + Decimal(0.5) - Decimal(1.15*10**(-12))

Einf.append(E_1_inf)
Einf.append(E_2_inf)
Einf.append(E_3_inf)
Einf.append(E_4_inf)

E_10000.append(eigenvalue_1.min())
E_10000.append(eigenvalue_2.min())
E_10000.append(eigenvalue_3.min())
E_10000.append(eigenvalue_4.min())

diff = []
logdiff = []
for i in range(0, 4):
    diff.append(E_10000[i] - Einf[i])
    logdiff.append(np.log10(E_10000[i] - Einf[i]))



new_data = pd.DataFrame({
    'Energy at infinity': Einf,
    'Energy of 10000matrix': E_10000,
    'Difference': diff,
    'log(Difference)': logdiff,
})

# 儲存為新的 CSV 文件
output_file = 'difference_fit/Einfinity.csv'
new_data.to_csv(output_file, index=False, float_format='%.50f')
print(f"結果已成功儲存至: {output_file}")