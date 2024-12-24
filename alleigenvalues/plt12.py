import pandas as pd
import matplotlib.pyplot as plt

# 讀取數據
file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path)

# 提取 State 和指定 Eigenvalue
x_data = data['State']
eigenvalue_1 = data['Eigenvalue 1']
eigenvalue_2 = data['Eigenvalue 2']

# 建立圖表
fig, ax1 = plt.subplots(figsize=(12, 8))

# 繪製 Eigenvalue 1
ax1.plot(x_data, eigenvalue_1.interpolate(), label='Eigenvalue 1', color='blue', linewidth=1.5)
ax1.set_xlabel('State', fontsize=14)
ax1.set_ylabel('Eigenvalue 1', fontsize=14, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title('Eigenvalue 1 and 2 with Separate Y Axes', fontsize=16)

# 添加第二個 y 軸
ax2 = ax1.twinx()
ax2.plot(x_data, eigenvalue_2.interpolate(), label='Eigenvalue 2', color='red', linewidth=1.5)
ax2.set_ylabel('Eigenvalue 2', fontsize=14, color='red')
ax2.tick_params(axis='y', labelcolor='red')

# 顯示圖例與格線
fig.legend(loc="upper right", bbox_to_anchor=(1, 0.9), fontsize=12)
ax1.grid(True)

# 儲存與顯示圖表
output_file = 'alleigenvalues/eigenvalues_1_and_2_separate_axes.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已儲存至: {output_file}")