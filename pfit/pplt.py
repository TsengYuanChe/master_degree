import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 文件
data = pd.read_csv('penergy.csv')

# 提取 Eigenstate 和 Potential Energy 欄位
x = data['Eigenstate']
y = data['Potential Energy']

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Potential Energy', color='red', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of eigenstates', fontsize=14)
plt.ylabel('Potential Energy (E$_h$)', fontsize=14)
plt.title('Potential Energy', fontsize=16)

# 設定 x 軸和 y 軸範圍（可選）
plt.xlim(left=x.min(), right=x.max())  # 根據數據自動設定
plt.ylim(bottom=y.min() * 0.9, top=y.max()*1.1)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
plt.savefig('pfit/penergy.png', dpi=300, bbox_inches='tight')
plt.show()