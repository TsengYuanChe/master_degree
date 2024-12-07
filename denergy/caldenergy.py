import pandas as pd
from decimal import Decimal, getcontext

getcontext().prec = 50
msize = 10000

datad = pd.read_csv('dia10000.csv', header=None, dtype=str)
your_datad = datad.iloc[:, 0].apply(Decimal).values
data = pd.read_csv(f'energys/Energy{msize}.csv', header=None, dtype=str)
your_data = data.iloc[:, 0].apply(Decimal).values

min_length = min(len(your_data), len(your_datad))
your_data = your_data[:min_length]
your_datad = your_datad[:min_length]

new_data = pd.DataFrame({
    'Eigenstate': range(1, len(your_data) + 1),
    'Energy': your_data,
    'Diagonal Energy': your_datad,
    'Residual Energy': [val1 - val2 for val1, val2 in zip(your_data, your_datad)],
    
})

new_data.to_csv(f'denergy/diagonalenergy{msize}.csv', index=False)
print(f"已成功生成檔案：denergy/diagonalenergy{msize}.csv",len(your_data))