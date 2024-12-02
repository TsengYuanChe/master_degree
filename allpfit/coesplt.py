import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 文件
data = pd.read_csv('allpfit/a * np.log(x) + 0.5.csv')

x = data['Matrix size']
y = data['Coefficient']

xleft = 1
xright = 10000
ybottom = 0.19
ytop = 0.3
# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Coefficients', color='red', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Matrix size (N)', fontsize=14)
plt.ylabel('Value of coefficient (C$_N$)', fontsize=14)
plt.title('Coefficients of different matrix size', fontsize=16)

# 設定 x 軸和 y 軸範圍（可選）
plt.xlim(xleft, xright)  # 根據數據自動設定
plt.ylim(ybottom, ytop)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
plt.savefig('allpfit/coefficients.png', dpi=300, bbox_inches='tight')
plt.show()