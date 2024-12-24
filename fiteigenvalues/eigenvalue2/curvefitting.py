import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 讀取數據
file_path = 'fiteigenvalues/eigenvalue2/eigenvalue2_data.csv'
data = pd.read_csv(file_path)

# 過濾掉沒有 Log(Adjusted Eigenvalue) 的數據
filtered_data = data.dropna(subset=['Log(Adjusted Eigenvalue)'])

# 提取有效的 x 和 y 值
x_data = filtered_data['Matrix size'].values
y_data = filtered_data['Log(Adjusted Eigenvalue)'].values

# 自定義擬合函數
def custom_model(x, a, b):
    return a * np.log10(x)+b

# 執行曲線擬合
try:
    popt, pcov = curve_fit(custom_model, x_data, y_data)
    
    # 計算擬合結果
    y_fit = custom_model(x_data, *popt)
    
    # 計算 R²
    ss_res = np.sum((y_data - y_fit) ** 2)  # 殘差平方和
    ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  # 總平方和
    r_squared = 1 - (ss_res / ss_tot)
    
    # 擬合公式
    formula = f"{popt[0]:.5f}log(x) + {popt[1]:.5f}"
    print(f"擬合公式: y = {formula}")
    print(f"R² = {r_squared:.5f}")
    
    # 繪製原始數據與擬合曲線
    plt.figure(figsize=(10, 6))
    
    # 原始數據
    plt.scatter(x_data, y_data, label='Original Data', color='blue', s=10)
    
    # 擬合曲線
    plt.plot(x_data, y_fit, label=f'Fitting: {formula}\n$R^2={r_squared:.5f}$', color='red', linewidth=2)
    
    # 設定標籤與標題
    plt.xlabel('Matrix size', fontsize=14)
    plt.ylabel('Log(Adjusted Eigenvalue)', fontsize=14)
    plt.title('Fitting Result and Original Data', fontsize=16)
    
    # 顯示圖例與格線
    plt.legend(fontsize=12)
    plt.grid(True)
    
    # 儲存與顯示圖表
    output_file = 'fiteigenvalues/eigenvalue2/fitting_result.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"圖表已儲存至: {output_file}")
except Exception as e:
    print(f"曲線擬合失敗: {e}")