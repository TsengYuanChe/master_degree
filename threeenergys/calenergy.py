import pandas as pd
from decimal import Decimal, getcontext

getcontext().prec = 50

for i in range(1, 10001):
    try:       
        datak = pd.read_csv('kenergys/kenergy10000.csv', dtype=str)
        your_datak = datak['E'].apply(Decimal).values
        data = pd.read_csv(f'energys/Energy{i}.csv', header=None, dtype=str)
        your_data = data.iloc[:, 0].apply(Decimal).values

        min_length = min(len(your_data), len(your_datak))
        your_data = your_data[:min_length]
        your_datak = your_datak[:min_length]

        new_data = pd.DataFrame({
            'Eigenstate': range(1, len(your_data) + 1),
            'Energy': your_data,
            'Kinetic Energy': your_datak,
            'Potential Energy': [val1 - val2 for val1, val2 in zip(your_data, your_datak)]
        })

        new_data.to_csv(f'threeenergys/threeEnergy_of_{i}.csv', index=False)
        print(f"已成功生成檔案：threeenergys/threeEnergy_of_{i}.csv",len(your_data))
    except FileNotFoundError:
        print(f"檔案 energy{i} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 energy{i} 時發生錯誤: {e}")