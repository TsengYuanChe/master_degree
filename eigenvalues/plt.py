import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

# 讀取生成的 CSV 文件
input_file = "eigenvalues/datas_diagonal/ev_of_es2.csv"
data = pd.read_csv(input_file, dtype=str)

# 確保高精度處理
data['File Number'] = data['File Number'].astype(int)
data['Log Difference'] = data['Log Difference'].apply(lambda x: Decimal(x) if x != 'NaN' else None)

# 移除 NaN 值的數據
filtered_data = data.dropna(subset=['Log Difference'])

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['File Number'], filtered_data['Log Difference'], label='Log Difference', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('File Number', fontsize=14)
plt.ylabel('Log Difference', fontsize=14)
plt.title('Log Difference vs File Number', fontsize=16)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
output_image = "eigenvalues/plts_dia/log_difference_plot.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已成功儲存至: {output_image}")