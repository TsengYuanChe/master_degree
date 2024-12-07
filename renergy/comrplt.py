import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

# 讀取合併後的數據
file_path = 'renergy/merged_residual_energy.csv'
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Eigenstate'] = data['Eigenstate'].astype(int)
data['Residual Energy_6000'] = data['Residual Energy_6000'].apply(Decimal)
data['Residual Energy_8000'] = data['Residual Energy_8000'].apply(Decimal)
data['Residual Energy_10000'] = data['Residual Energy_10000'].apply(Decimal)

xleft = 1
xright = 1000
#ybottom = -0.00001
#ytop = 0.00001
ybottom = data.loc[data['Eigenstate'] == xleft, 'Residual Energy_10000'].values[0] * Decimal(0.9)
ytop = data.loc[data['Eigenstate'] == xright, 'Residual Energy_10000'].values[0] * Decimal(1.1)
# 繪製圖表
plt.figure(figsize=(10, 6))

plt.plot(data['Eigenstate'], data['Residual Energy_6000'], label='Residual value for H$_{6000}$', color='green', linewidth=1.5, linestyle='-')
plt.plot(data['Eigenstate'], data['Residual Energy_8000'], label='Residual value for H$_{8000}$', color='blue', linewidth=1.5, linestyle='--')
plt.plot(data['Eigenstate'], data['Residual Energy_10000'], label='Residual value for H$_{10000}$', color='red', linewidth=1.5, linestyle=':')

# 設定標籤與標題
plt.xlabel('Number of eigenstates (n+1)', fontsize=14)
plt.ylabel('Residual value (E$_r$)', fontsize=14)
plt.title('Comparison of residual values for different sizes of Hamiltonian matrices', fontsize=16)

plt.xlim(xleft, xright)
plt.ylim(ybottom, ytop)

# 顯示圖例與格線
plt.legend(fontsize=12)
plt.grid(True)

# 儲存圖檔並顯示
output_file = f'printcom/detail{xleft}-{xright}.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已儲存至: {output_file}")