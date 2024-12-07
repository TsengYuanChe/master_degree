import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

formula = "0.20550ln(x) + 0.5"
data = pd.read_csv(f'pfit/{formula}.csv')

# 計算 log(abs(Error))
data['Log(abs(Error))'] = np.log(np.abs(data['Error']))

# 繪製 State 和 Log(abs(Error)) 的圖
plt.figure(figsize=(10, 6))
plt.plot(data['State'], data['Log(abs(Error))'], label='Log(abs(Difference))', color='red', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of state', fontsize=12)
plt.ylabel('Log(abs(Difference))', fontsize=12)
plt.title(f'Log(abs(Difference)) between residual value and {formula}', fontsize=14)

# 顯示網格與圖例
plt.grid(True)
plt.legend()

# 儲存圖表並顯示
plt.savefig(f'pfit/compare/{formula}_difference.png', dpi=300, bbox_inches='tight')
plt.show()