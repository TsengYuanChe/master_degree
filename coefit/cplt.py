import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 讀取 CSV 文件
filename = '0.7747740209829155_0.15552exp(-x^0.25187) + 0.20549'
data = pd.read_csv(f'coefit/{filename}.csv')

# 忽略第一筆數據
x = data['Matrix size'].iloc[1:]  # 從第二筆數據開始
y = data['Original - Constant'].iloc[1:]  # 同樣忽略第一筆數據

# 計算 log(abs(y))
log_y = np.log(np.abs(y))

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(x, log_y, label='Log(abs(Difference))', color='red', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Matrix size (N)', fontsize=14)
plt.ylabel('Log(abs(Difference))', fontsize=14)
plt.title('Log(abs(Difference) between coefficient and 0.15552e^{-N^{0.25187}} + 0.20549)', fontsize=12)

# 設定 x 軸和 y 軸範圍（可選）
# plt.xlim(left=x.min(), right=x.max())  # 根據數據自動設定
# plt.ylim(bottom=log_y.min() * 0.9, top=log_y.max() * 1.1)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
plt.savefig('coefit/logc.png', dpi=300, bbox_inches='tight')
plt.show()