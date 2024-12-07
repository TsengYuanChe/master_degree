import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# 讀取 CSV 文件
filename = '-0.04222x^(-0.98270)'
data = pd.read_csv(f'drfit/fit1000/{filename}.csv')

# 繪製圖表
plt.figure(figsize=(10, 6))

# 繪製 State vs Predicted energy
plt.plot(data['State'], data['Predicted energy'], label=f'E$_r$=-0.04222(n+1)^(-0.98270)', color='blue', linewidth=1.5)

# 繪製 State vs Original energy
plt.plot(data['State'], data['Original energy'], label='Residual value', color='red', linestyle='--', linewidth=1.5)

# 設定軸範圍
#plt.xlim(xleft, xright)  # 替換為你的 x 軸範圍
#plt.ylim(ybottom, ytop)      # 替換為你的 y 軸範圍

#plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.ticklabel_format(style='plain', axis='x')
plt.ticklabel_format(style='plain', axis='y')

# 設定標籤與標題
plt.xlabel('Number of eigenstates (n+1)', fontsize=16)
plt.ylabel('Residual value (E$_r$)', fontsize=16)
plt.title(f'Comparison of residual value and E$_r$=-0.04222(n+1)^(-0.98270)', fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=12)

# 顯示圖例與網格
plt.legend()
plt.grid(True)

# 儲存圖檔並顯示
plt.savefig(f'drfit/fit1000/{filename}_comparison_energy.png', dpi=300, bbox_inches='tight')
plt.show()