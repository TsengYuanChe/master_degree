import pandas as pd
from decimal import Decimal, getcontext

getcontext().prec = 50
# 讀取之前儲存的檔案
for i in range(1, 10001):
    try:
        data = pd.read_csv(f'threeenergys/threeEnergy_of_{i}.csv', dtype=str)

        Eigenstate = data['Eigenstate'].apply(Decimal).values
        penergy = data['Potential Energy'].apply(Decimal).values

        new_data = pd.DataFrame({
            'Eigenstate': Eigenstate,
            'Potential Energy': penergy
        })
        new_data.to_csv(f'penergys/penergy{i}.csv', index=False)
        print(f"已成功儲存檔案：penergys/penergy{i}.csv")
    except FileNotFoundError:
        print(f"檔案 penergy{i} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 penergy{i} 時發生錯誤: {e}")