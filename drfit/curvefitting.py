import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# 讀取數據
data = pd.read_csv('drfit/re10000_1987.csv')
x_data = data['Eigenstate'].values
y_data = data['Residual Energy_10000'].values

datad = pd.read_csv('denergy/diagonalenergy10000.csv')
constdata = datad['Diagonal Energy'][0]

const = 0.5 - constdata

def custom_model(x, a, b, c):
    return a*x**(b) + c

# 擬合數據
popt, pcov = curve_fit(custom_model, x_data, y_data, maxfev=5000)

# 計算擬合結果
y_fit = custom_model(x_data, *popt)

# 計算 R²
ss_res = np.sum((y_data - y_fit) ** 2)  # 殘差平方和
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  # 總平方和
r_squared = 1 - (ss_res / ss_tot)

# 隨機生成 10 個 x 值
State = np.arange(1, len(x_data)+1)

# 使用擬合函數計算隨機 x 值對應的 y 值
predicted_y = custom_model(State, *popt)

# 從原始數據中找到對應的原始 y 值
original_y = []
for x in State:
    matched_row = data[data['Eigenstate'] == x]
    if not matched_row.empty:
        original_y.append(matched_row['Residual Energy_10000'].values[0])
    else:
        original_y.append(np.nan)  # 如果找不到，填入 NaN

original_y = np.array(original_y)

# 計算誤差
errors = (predicted_y - original_y)/original_y
constant = popt[0] + const

formula = f"{popt[0]:.5f}x^({popt[1]:.5f})+{popt[2]:.5f}"
print(f"擬合公式: y = {formula}")
print(f"R² = {r_squared:.5f}\n")

result = pd.DataFrame({
    'State': State,
    'Predicted energy': predicted_y,
    'Original energy': original_y,
    'Error': errors
})
# 將公式加入 DataFrame
result['Formula'] = formula
result.to_csv(f'drfit/fit1987/{formula}.csv', index=False)
print("結果已儲存成功")