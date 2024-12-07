import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 文件
msize = 10000
data = pd.read_csv(f'denergy/diagonalenergy{msize}.csv')

# 忽略第一筆數據
x = data['Eigenstate'].iloc[0:]  # 從第二筆數據開始
y = data['Residual Energy'].iloc[0:]  # 同樣忽略第一筆數據

xleft = 1
xright = 10000
#ybottom = -0.001
#ytop = 0.001
ybottom = data.loc[data['Eigenstate'] == xleft, 'Residual Energy'].values[0] * 0.9
ytop = data.loc[data['Eigenstate'] == xright, 'Residual Energy'].values[0] * 1.1

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Residual value', color='red', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Number of eigenstates (n+1)', fontsize=14)
plt.ylabel('Residual value (E$_r$)', fontsize=14)
plt.title('Residual value of the obtained energies and diagonal values', fontsize=16)

# 設定 x 軸和 y 軸範圍（可選）
#plt.xlim(xleft, xright)  # 替換為你的 x 軸範圍
#plt.ylim(ybottom, ytop)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
plt.savefig(f'print/renergy.png', dpi=300, bbox_inches='tight')
plt.show()