import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 讀取數據
file_path = 'difference_fit/eigenvalues_data.csv'
data = pd.read_csv(file_path)

# 過濾掉沒有 Log(Adjusted Eigenvalue) 的數據
data = data.dropna(subset=['Eigenvalue 1'])
data = data.dropna(subset=['Eigenvalue 2'])
data = data.dropna(subset=['Eigenvalue 3'])
filtered_data = data.dropna(subset=['Eigenvalue 4'])

def custom_model(x, a, b):
    return x**a + 10**b + 0.5

formula = []
r_squared = []
y_data = []
y_fit = []

# 提取有效的 x 和 y 值
for i in range(0,1):
    x_data = filtered_data['Matrix size'].values
    y_data.append(filtered_data[f'Eigenvalue {i+1}'].values)
    
    popt, pcov = curve_fit(custom_model, x_data, y_data[i])
    
    # 計算擬合結果
    y_fit.append(custom_model(x_data, *popt))
    
    # 計算 R²
    ss_res = np.sum((y_data[i] - y_fit[i]) ** 2)  # 殘差平方和
    ss_tot = np.sum((y_data[i] - np.mean(y_data[i])) ** 2)  # 總平方和
    r_squared.append(1 - (ss_res / ss_tot))
    
    # 擬合公式
    formula.append(f"x^{popt[0]:.5f} + 10^{popt[1]:.5f} + 0.5")
    print(f"擬合公式 {i+1}: y = {formula[i]}")
    print(f"R² {i+1} = {r_squared[i]:.5f}")
    
plt.figure(figsize=(10, 6))

# 原始數據
plt.scatter(x_data, y_data[0], label=f'Adjusted Data for Eigenvalue {1}', color='blue', s=10)
# 擬合曲線
plt.plot(x_data, y_fit[0], label=f'Fitting: {formula[0]}\n$R^2={r_squared[0]:.5f}$', color='blue', linewidth=2)

# 設定標籤與標題
plt.xlabel('Matrix size', fontsize=14)
plt.ylabel('Log(Adjusted Eigenvalue)', fontsize=14)
plt.title('Fitting Result and Original Data', fontsize=16)

# 顯示圖例與格線
plt.legend(fontsize=12)
plt.grid(True)

plt.show()