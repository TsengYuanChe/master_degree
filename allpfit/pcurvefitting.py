import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

Size = []
Coefficient = []
Coefficient_Diff = []
rsqrt = []

for i in range(1, 10001):
    try:
        data = pd.read_csv(f'penergys/penergy{i}.csv')
        x_data = data['Eigenstate'].values
        y_data = data['Potential Energy'].values

        def custom_model(x, a):
            return a * np.log(x) + 0.5

        popt, pcov = curve_fit(custom_model, x_data, y_data)

        y_fit = custom_model(x_data, *popt)

        ss_res = np.sum((y_data - y_fit) ** 2) 
        ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  
        r_squared = 1 - (ss_res / ss_tot)

        Size.append(i)
        Coefficient.append(popt[0])
        rsqrt.append(r_squared)

        # 計算 Coefficient 與前一個的差異
        if len(Coefficient) > 1:
            diff = Coefficient[-1] - Coefficient[-2]
        else:
            diff = 0  # 第一個值沒有差異
        Coefficient_Diff.append(diff)

    except FileNotFoundError:
        print(f"檔案 energy{i} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 energy{i} 時發生錯誤: {e}")

# 建立 DataFrame
result = pd.DataFrame({
    'Matrix size': Size,
    'Coefficient': Coefficient,
    'Coefficient Difference': Coefficient_Diff,
    'R square': rsqrt,
})

# 儲存到 CSV
result.to_csv('allpfit/a * np.log(x) + 0.5_with_diff.csv', index=False)
print("結果已儲存成功至：allpfit/a * np.log(x) + 0.5_with_diff.csv")