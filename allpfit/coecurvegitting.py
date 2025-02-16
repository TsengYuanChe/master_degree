import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# 讀取數據
data = pd.read_csv('allpfit/a * np.log(x) + 0.5.csv')
const = 0.20549

# 忽略第一筆數據
x_data = data['Matrix size'].values[1:]  # 忽略第一筆
y_data = data['Coefficient'].values[1:]  # 忽略第一筆

# 自定義擬合函數 (例子：指數函數)
def custom_model(x, a, b):
    return a * np.exp(-x**b) + const

# 擬合數據
popt, pcov = curve_fit(custom_model, x_data, y_data, maxfev=10000)

# 計算擬合結果
y_fit = custom_model(x_data, *popt)

# 計算 R²
ss_res = np.sum((y_data - y_fit) ** 2)  # 殘差平方和
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  # 總平方和
r_squared = 1 - (ss_res / ss_tot)

# 使用擬合函數計算預測值
predicted_y = custom_model(x_data, *popt)

# 原始數據的對應 y 值
original_y = data['Coefficient'].values[1:]  # 忽略第一筆數據

# 計算誤差
errors = (predicted_y - original_y) / original_y

adjusted_values = original_y - const

formula = f"{popt[0]:.5f}exp(-x^{popt[1]:.5f}) + {const}"
print(f"擬合公式: y = {formula}")
print(f"R² = {r_squared:.5f}\n")

# 建立結果 DataFrame
result = pd.DataFrame({
    'Matrix size': data['Matrix size'].values[1:],  # 忽略第一筆數據
    'Predicted Coefficient': predicted_y,
    'Original Coefficient': original_y,
    'Original - Constant': adjusted_values,
    'Error': errors
})
# 將公式加入 DataFrame
result['Formula'] = formula
result.to_csv(f'coefit/{r_squared}_{formula}.csv', index=False)
print("結果已儲存成功")