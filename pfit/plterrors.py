import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

formula = "0.20146ln(0.20146x) + 0.5"
data = pd.read_csv(f'pfit/{formula}.csv')

mpe = data['Error'].mean() * 100  # 平均百分誤差 (MPE)
mape = data['Error'].abs().mean() * 100  # 平均絕對百分誤差 (MAPE)
log_error = np.log1p(data['Error'].abs()).mean()  # 對數誤差 (避免負值問題用 log1p)

# 繪製 Random x 和 Error 的圖
plt.figure(figsize=(10, 6))
plt.plot(data['State'], data['Error'], label='Error', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of state', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.title(f'Error of {formula}', fontsize=14)

text_x = 0.75  # x 軸文字位置 (圖表百分比位置)
text_y = 0.80  # y 軸文字位置 (圖表百分比位置)
plt.text(text_x, text_y, f"MPE: {mpe:.10f}%\nMAPE: {mape:.10f}%\nLog Error: {log_error:.10f}",
         transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# 顯示網格與圖例
plt.grid(True)
plt.legend()

# 儲存圖表並顯示
plt.savefig(f'pfit/{formula}.png', dpi=300, bbox_inches='tight')
plt.show()