import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 讀取 CSV 文件
formula = '0.7747740209829155_0.15552exp(-x^0.25187) + 0.20549'
data = pd.read_csv(f'coefit/{formula}.csv')
xleft = 2
xright = 10000
ybottom = data.loc[data['Matrix size'] == xright, 'Original Coefficient'].values[0] * 0.9
ytop = data.loc[data['Matrix size'] == xleft, 'Original Coefficient'].values[0] * 1.1

# 繪製圖表
plt.figure(figsize=(10, 6))

# 繪製 State vs Predicted energy
plt.plot(data['Matrix size'], data['Predicted Coefficient'], label=f'Eq.(14.5)', color='blue', linewidth=1.5)

# 繪製 State vs Original energy
plt.plot(data['Matrix size'], data['Original Coefficient'], label='Coefficients', color='red', linestyle='--', linewidth=1.5)

# 設定軸範圍
plt.xlim(xleft, xright)  # 替換為你的 x 軸範圍
plt.ylim(ybottom, ytop)      # 替換為你的 y 軸範圍

#plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.ticklabel_format(style='plain', axis='x')
plt.ticklabel_format(style='plain', axis='y')

# 設定標籤與標題
plt.xlabel('Matrix size (N)', fontsize=16)
plt.ylabel('Value of coefficient (C$_N$)', fontsize=16)
plt.title('Comparison of the curve of coefficient and Eq.(14.5)', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=12)

# 顯示圖例與網格
plt.legend()
plt.grid(True)

# 儲存圖檔並顯示
plt.savefig(f'coefit/{xleft}_to_{xright}_comparison_energy.png', dpi=300, bbox_inches='tight')
plt.show()