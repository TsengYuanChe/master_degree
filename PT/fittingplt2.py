import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 讀取數據
file_path = 'PT/eigenvalues_data2.csv'
data = pd.read_csv(file_path)

# 過濾掉沒有 Log(Adjusted Eigenvalue) 的數據
data = data.dropna(subset=['Log(Adjusted Eigenvalue 1)'])
data = data.dropna(subset=['Log(Adjusted Eigenvalue 2)'])
data = data.dropna(subset=['Log(Adjusted Eigenvalue 3)'])
filtered_data = data.dropna(subset=['Log(Adjusted Eigenvalue 4)'])

def custom_model(x, a, b):
    return a * np.log10(x) + b

formula = []
r_squared = []
y_data = []
y_fit = []

# 提取有效的 x 和 y 值
for i in range(0,4):
    x_data = filtered_data['Matrix size'].values
    y_data.append(filtered_data[f'Log(Adjusted Eigenvalue {i+1})'].values)
    
    popt, pcov = curve_fit(custom_model, x_data, y_data[i])
    
    # 計算擬合結果
    y_fit.append(custom_model(x_data, *popt))
    
    # 計算 R²
    ss_res = np.sum((y_data[i] - y_fit[i]) ** 2)  # 殘差平方和
    ss_tot = np.sum((y_data[i] - np.mean(y_data[i])) ** 2)  # 總平方和
    r_squared.append(1 - (ss_res / ss_tot))
    
    # 擬合公式
    formula.append(f"{popt[0]:.5f}log(N) + {popt[1]:.5f}")
    print(f"擬合公式 {i+1}: y = {formula[i]}")
    print(f"R² {i+1} = {r_squared[i]:.5f}")
    
# 繪製原始數據與擬合曲線
plt.figure(figsize=(10, 6))

# 原始數據
plt.scatter(x_data, y_data[0], label=f'Adjusted Data for Eigenvalue {1}', color='blue', s=10)
plt.scatter(x_data, y_data[1], label=f'Adjusted Data for Eigenvalue {2}', color='red', s=10)
plt.scatter(x_data, y_data[2], label=f'Adjusted Data for Eigenvalue {3}', color='green', s=10)
plt.scatter(x_data, y_data[3], label=f'Adjusted Data for Eigenvalue {4}', color='purple', s=10)

# 擬合曲線
plt.plot(x_data, y_fit[0], label=f'Fitting: {formula[0]}\n$R^2={r_squared[0]:.5f}$', color='blue', linewidth=2)
plt.plot(x_data, y_fit[1], label=f'Fitting: {formula[1]}\n$R^2={r_squared[1]:.5f}$', color='red', linewidth=2)
plt.plot(x_data, y_fit[2], label=f'Fitting: {formula[2]}\n$R^2={r_squared[2]:.5f}$', color='green', linewidth=2)
plt.plot(x_data, y_fit[3], label=f'Fitting: {formula[3]}\n$R^2={r_squared[3]:.5f}$', color='purple', linewidth=2)

#plt.xlim(6000, 10100)
#plt.ylim(-13.6, -11.8)
# 設定標籤與標題
plt.xlabel('Matrix size (N)', fontsize=14)
plt.ylabel('Log(Adjusted Eigenvalue)', fontsize=14)
plt.title('Fitting functions and adjusted data', fontsize=16)

# 顯示圖例與格線
plt.legend(fontsize=12)
plt.grid(True)

# 儲存與顯示圖表
output_file = 'PT/fitting_result2_detail.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已儲存至: {output_file}")
