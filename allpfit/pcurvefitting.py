import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

Size = []
Coefficient = []
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
    except FileNotFoundError:
        print(f"檔案 energy{i} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 energy{i} 時發生錯誤: {e}")
 
result = pd.DataFrame({
    'Matrix size': Size,
    'Coefficient': Coefficient,
    'R square': rsqrt,
})
result.to_csv('allpfit/a * np.log(x) + 0.5.csv', index=False)
print("結果已儲存成功至：allpfit/a * np.log(x) + 0.5.csv")