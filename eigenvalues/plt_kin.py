import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

# 讀取生成的 CSV 文件
file_path = "eigenvalues/kinetic_data/kinetic_of_es2.csv"
data = pd.read_csv(file_path, dtype=str)

# 確保高精度處理
data['Matrix Size'] = data['Matrix Size'].astype(int)
data['Log Kinetic Difference'] = data['Log Kinetic Difference'].apply(Decimal)

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.plot(data['Matrix Size'], data['Log Kinetic Difference'], label='Log Kinetic Difference', color='blue', linewidth=1.5)

# 設定標籤與標題
plt.xlabel('Matrix Size', fontsize=14)
plt.ylabel('Log Kinetic Difference', fontsize=14)
plt.title('Log Kinetic Difference vs Matrix Size', fontsize=16)

# 設定格線與圖例
plt.grid(True)
plt.legend()

# 儲存圖檔並顯示
output_image = "eigenvalues/plt_kin/log_kinetic_difference_plot2.png"
plt.savefig(output_image, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已成功儲存至: {output_image}")