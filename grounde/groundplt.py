import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv('grounde/lowestenergys.csv')

xleft = 1
xright = 10000
ybottom = data.loc[data['Matrix size'] == xleft, 'Log'].values[0] * 0.99
ytop = data.loc[data['Matrix size'] == xright, 'Log'].values[0] * 1.01
# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(data['Matrix size'], data['Log'], label='Logarithm of difference', color='red', linewidth=1.5)

plt.xlim(xleft, xright)
plt.ylim(ybottom, ytop)

# 設定標籤與標題
plt.xlabel('Matrix size', fontsize=14)
plt.ylabel('Logarithm of difference', fontsize=14)
#plt.title('The difference between the obtained values and 0.5', fontsize=16)

# 顯示網格與圖例
plt.grid(True)
plt.legend(fontsize=12)

# 儲存圖表並顯示
plt.savefig('grounde/logground.png', dpi=300, bbox_inches='tight')
plt.show()