import numpy as np
import pandas as pd
from decimal import Decimal, getcontext
import math
from scipy.optimize import curve_fit

# 設定高精度
getcontext().prec = 50

# 讀取數據
size = 10000
data = pd.read_csv(f'penergys/penergy{size}.csv', dtype=str)
data['Eigenstate'] = data['Eigenstate'].apply(Decimal)
data['Potential Energy'] = data['Potential Energy'].apply(Decimal)

# 擷取數據並轉換為浮點數用於擬合
x_data = np.array([float(x) for x in data['Eigenstate']])  # 使用浮點數進行擬合
y_data = np.array([float(y) for y in data['Potential Energy']])

# 自定義擬合函數
def custom_model(x, a):
    return a * np.log(x) + 0.5

# 擬合數據
popt, pcov = curve_fit(custom_model, x_data, y_data)

# 計算擬合結果
y_fit = custom_model(x_data, *popt)

# 計算 R²
ss_res = np.sum((y_data - y_fit) ** 2)  # 殘差平方和
ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)  # 總平方和
r_squared = 1 - (ss_res / ss_tot)

# 使用擬合函數計算所有 x 值對應的 y 值
State = np.arange(1, size + 1)
predicted_y = custom_model(State, *popt)

# 從原始數據中找到對應的原始 y 值
original_y = []
for x in State:
    matched_row = data[data['Eigenstate'] == Decimal(str(x))]  # 明確轉換為字符串再轉為 Decimal
    if not matched_row.empty:
        original_y.append(Decimal(matched_row['Potential Energy'].values[0]))
    else:
        original_y.append(None)  # 如果找不到，填入 None

# 計算誤差
errors = [
    (Decimal(py) - oy) / oy if oy is not None and oy != 0 else None
    for py, oy in zip(predicted_y, original_y)
]

# 高精度公式
formula = f"{Decimal(popt[0]):.50f}ln(x) + 0.5"
print(f"擬合公式: y = {formula}")
print(f"R² = {Decimal(r_squared):.50f}\n")

# 建立結果 DataFrame
result = pd.DataFrame({
    'State': State,
    'Predicted energy': [float(py) for py in predicted_y],
    'Original energy': [float(oy) if oy is not None else np.nan for oy in original_y],
    'Error': [float(err) if err is not None else np.nan for err in errors]
})

# 將公式加入 DataFrame
result['Formula'] = formula
output_file = f'pfit/fitting{size}/{formula}.csv'
result.to_csv(output_file, index=False)
print(f"結果已儲存成功至: {output_file}")