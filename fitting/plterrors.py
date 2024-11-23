import pandas as pd
import matplotlib.pyplot as plt

formula = "0.4x^2 + 0.1x + -0.09681(x-1)**1.00335"
data = pd.read_csv(f'fitting/{formula}.csv')

mse = (data['Error'] ** 2).mean()  # 均方誤差
mae = data['Error'].abs().mean()  # 平均絕對誤差

# 繪製 Random x 和 Error 的圖
plt.figure(figsize=(10, 6))
plt.plot(data['State'], data['Error'], label='Error', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of state', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.title(f'Error of {formula}', fontsize=14)

text_x = 0.80  # x 軸文字位置 (圖表百分比位置)
text_y = 0.82  # y 軸文字位置 (圖表百分比位置)
plt.text(text_x, text_y, f"MSE: {mse:.10f}\nMAE: {mae:.10f}", transform=plt.gca().transAxes,
         fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

# 顯示網格與圖例
plt.grid(True)
plt.legend()

# 儲存圖表並顯示
plt.savefig(f'fitting/{formula}.png', dpi=300, bbox_inches='tight')
plt.show()