import pandas as pd
from decimal import Decimal, getcontext

getcontext().prec = 50
# 讀取之前儲存的檔案
data = pd.read_csv('threeEnergy_of_10000.csv', dtype=str)

Eigenstate = data['Eigenstate'].apply(Decimal).values
penergy = data['Potential Energy'].apply(Decimal).values

new_data = pd.DataFrame({
    'Eigenstate': Eigenstate,
    'Potential Energy': penergy
})
new_data.to_csv('penergy.csv', index=False)
print("已成功儲存檔案：penergy.csv")