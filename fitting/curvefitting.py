import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# 讀取數據
data = pd.read_csv('Energy_of_10000.csv')
x_data = data['Eigenstate'].values
y_data = data['Energy'].values

# 自定義擬合函數 (例子：二次多項式)
def custom_model(x, a, b):
    return 0.4 * x**2 + 0.1*x + a*(x-1)**b

# 擬合數據
popt, pcov = curve_fit(custom_model, x_data, y_data)

# 計算擬合結果
y_fit = custom_model(x_data, *popt)

# 計算 R²
ss_res = np.sum((y_data - y_fit) ** 2)  # 殘差平方和
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  # 總平方和
r_squared = 1 - (ss_res / ss_tot)

# 隨機生成 10 個 x 值
State = np.arange(1, 10001)

# 使用擬合函數計算隨機 x 值對應的 y 值
predicted_y = custom_model(State, *popt)

# 從原始數據中找到對應的原始 y 值
original_y = []
for x in State:
    matched_row = data[data['Eigenstate'] == x]
    if not matched_row.empty:
        original_y.append(matched_row['Energy'].values[0])
    else:
        original_y.append(np.nan)  # 如果找不到，填入 NaN

original_y = np.array(original_y)

# 計算誤差
errors = (predicted_y - original_y)/original_y

formula = f"0.4x^2 + 0.1x + {popt[0]:.5f}(x-1)^{popt[1]:.5f}"
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
result.to_csv(f'fitting/{formula}.csv', index=False)
print("結果已儲存成功")








# 可視化結果
#plt.figure(figsize=(10, 6))
#plt.scatter(x_data, y_data, label='原始數據', color='red')
#plt.plot(x_data, y_fit, label=f'擬合曲線\n$R^2={r_squared:.5f}$', color='blue', linewidth=2)
#plt.xlabel('Eigenstate', fontsize=12)
#plt.ylabel('Energy', fontsize=12)
#plt.title('自定義函數擬合結果', fontsize=14)
#plt.legend(fontsize=12)
#plt.grid(True)
#plt.tight_layout()
#plt.show()