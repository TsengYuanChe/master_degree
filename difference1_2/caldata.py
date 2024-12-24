import pandas as pd
import numpy as np
from decimal import Decimal, getcontext
import math

getcontext().prec = 50

file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path, dtype=str)

data['State'] = data['State'].astype(int)
data['Eigenvalue 1'] = data['Eigenvalue 1'].apply(lambda x: Decimal(x) if x != 'nan' else np.nan)
data['Eigenvalue 2'] = data['Eigenvalue 2'].apply(lambda x: Decimal(x) if x != 'nan' else np.nan)

difference12 = []
log_difference = []

length = len(data['State'])

for i in range(0,length):
    if pd.notna(data['Eigenvalue 2'][i]):
        difference = data['Eigenvalue 2'][i] - data['Eigenvalue 1'][i]
        difference12.append(difference)
        log_difference.append(Decimal(math.log10(difference)))
    else:
        difference12.append(np.nan)
        log_difference.append(np.nan)

new_data = pd.DataFrame({
    'Matrix size': data['State'],
    'Eigenvalue 1': data['Eigenvalue 1'],
    'Eigenvalue 2': data['Eigenvalue 2'],
    'Difference': difference12,
    'Log(Adjusted Eigenvalue)': log_difference,
})

output_file = 'difference1_2/eigenvalue_df.csv'
new_data.to_csv(output_file, index=False)
print(f"結果已成功儲存至: {output_file}")