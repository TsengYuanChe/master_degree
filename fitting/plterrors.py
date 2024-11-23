import pandas as pd
import matplotlib.pyplot as plt

formula = "0.4x^2 + 0.1 + -0.09681(x-1)^1.00335"
data = pd.read_csv(f'fitting/{formula}.csv')

# 繪製 Random x 和 Error 的圖
plt.figure(figsize=(10, 6))
plt.plot(data['State'], data['Error'], label='Error', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of state', fontsize=12)
plt.ylabel('Error', fontsize=12)
plt.title('Error of different state', fontsize=14)

# 顯示網格與圖例
plt.grid(True)
plt.legend()

# 儲存圖表並顯示
plt.savefig(f'fitting/{formula}.png', dpi=300, bbox_inches='tight')
plt.show()