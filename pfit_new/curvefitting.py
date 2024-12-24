import os
import pandas as pd
from decimal import Decimal, getcontext
import math

# 設定高精度
getcontext().prec = 50

# 讀取數據
size = 8000
file_path = f'penergys/penergy{size}.csv'
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Eigenstate'] = data['Eigenstate'].astype(int)  # 轉換為 Python 的 int
data['Potential Energy'] = data['Potential Energy'].apply(lambda x: Decimal(x))

x_data = data['Eigenstate'].values
y_data = data['Potential Energy'].values

# 自定義擬合函數
def custom_model(x, a):
    return a * Decimal(math.log(x)) + Decimal('0.5')

# 擬合數據
def fit_function(x_data, y_data):
    # 初始參數猜測
    initial_guess = [Decimal('0.1')]
    # 將 x_data 轉換為 Python int 並處理為 Decimal
    x_data_decimal = [Decimal(int(x)) for x in x_data]
    # 擬合過程
    try:
        # 手動執行擬合過程
        popt = [Decimal('0.1')]
        pcov = []
        for _ in range(100):  # 手動迭代更新
            # 這裡可加入具體的擬合方法，例如 Gradient Descent
            pass
    except Exception as e:
        print(f"擬合過程中出現錯誤: {e}")
        return [], []
    return popt, pcov

popt, pcov = fit_function(x_data, y_data)

# 計算擬合結果
y_fit = [custom_model(Decimal(int(x)), Decimal(popt[0])) for x in x_data]

# 計算 R²
ss_res = sum((Decimal(y) - Decimal(fit)) ** 2 for y, fit in zip(y_data, y_fit))
ss_tot = sum((Decimal(y) - Decimal(sum(y_data) / len(y_data))) ** 2 for y in y_data)
r_squared = 1 - (ss_res / ss_tot)

# 隨機生成 x 值範圍
State = [Decimal(i) for i in range(1, size + 1)]

# 使用擬合函數計算 x 值對應的預測 y 值
predicted_y = [custom_model(Decimal(x), Decimal(popt[0])) for x in State]

# 從原始數據中找到對應的原始 y 值
original_y = []
for x in State:
    matched_row = data[data['Eigenstate'] == int(x)]
    if not matched_row.empty:
        original_y.append(Decimal(matched_row['Potential Energy'].values[0]))
    else:
        original_y.append(Decimal('NaN'))  # 如果找不到，填入 NaN

# 計算誤差
errors = [(pred - orig) / orig if orig != 0 else Decimal('NaN') for pred, orig in zip(predicted_y, original_y)]

formula = f"{Decimal(popt[0]):.20f}ln(x) + 0.5"
print(f"擬合公式: y = {formula}")
print(f"R² = {r_squared:.5f}\n")

# 儲存結果
result = pd.DataFrame({
    'State': [int(s) for s in State],
    'Predicted energy': [float(p) for p in predicted_y],
    'Original energy': [float(o) for o in original_y],
    'Error': [float(e) for e in errors]
})
result['Formula'] = formula
output_dir = f'pfit_new/fitting{size}'
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, f'{formula}.csv')
result.to_csv(output_file, index=False)
print(f"結果已儲存成功至: {output_file}")