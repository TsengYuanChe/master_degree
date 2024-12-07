import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

# 讀取 CSV 文件
file_path = 'drfit/re10000_1987.csv'
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Eigenstate'] = data['Eigenstate'].astype(int)
data['Residual Energy_10000'] = data['Residual Energy_10000'].apply(Decimal)

# 繪製圖表
plt.figure(figsize=(10, 6))

plt.plot(data['Eigenstate'], data['Residual Energy_10000'], label='Residual Energy 10000', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Eigenstate', fontsize=14)
plt.ylabel('Residual Energy', fontsize=14)
plt.title('Residual Energy for First 1987 Eigenstates', fontsize=16)

# 設定 x 軸和 y 軸範圍（可選）
plt.xlim(left=1, right=100)
#plt.ylim(bottom=min(data['Residual Energy_10000']) * 0.9, top=max(data['Residual Energy_10000']) * 1.1)

# 顯示圖例與格線
plt.legend(fontsize=12)
plt.grid(True)

# 儲存圖檔並顯示
output_file = 'drfit/re10000_1987_plot.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已成功儲存至: {output_file}")