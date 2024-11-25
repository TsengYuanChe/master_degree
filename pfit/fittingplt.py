import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 讀取 CSV 文件
filename = '0.20550ln(x) + 0.5'
data = pd.read_csv(f'pfit/{filename}.csv')
xleft = 1
xright = 10000
ybottom = data.loc[data['State'] == xleft, 'Original energy'].values[0] * 0.99
ytop = data.loc[data['State'] == xright, 'Original energy'].values[0] * 1.01

# 繪製圖表
plt.figure(figsize=(10, 6))

# 繪製 State vs Predicted energy
plt.plot(data['State'], data['Predicted energy'], label=f'{filename}', color='blue', linewidth=1.5)

# 繪製 State vs Original energy
plt.plot(data['State'], data['Original energy'], label='Energy', color='red', linestyle='--', linewidth=1.5)

# 設定軸範圍
plt.xlim(xleft, xright)  # 替換為你的 x 軸範圍
plt.ylim(ybottom, ytop)      # 替換為你的 y 軸範圍

#plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.ticklabel_format(style='plain', axis='x')
plt.ticklabel_format(style='plain', axis='y')

# 設定標籤與標題
plt.xlabel('Number of eigenstates', fontsize=16)
plt.ylabel('Potential Energy (E$_h$)', fontsize=16)
plt.title(f'Comparison of potential energy and {filename}', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=12)

# 顯示圖例與網格
plt.legend()
plt.grid(True)

# 儲存圖檔並顯示
plt.savefig(f'pfit/compare/{xleft}_to_{xright}_comparison_energy.png', dpi=300, bbox_inches='tight')
plt.show()