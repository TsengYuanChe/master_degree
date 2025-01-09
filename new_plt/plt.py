import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 讀取數據
file_path = 'alleigenvalues/all_eigenvalues10.csv'
data = pd.read_csv(file_path)

start = 1
end = 10

# 提取 State 和 Eigenvalue {1-10}
x_data = data['State']
eigenvalue_columns = [f'Eigenvalue {i}' for i in range(start, end + 1)]

# 建立一個新的 DataFrame 用於儲存處理過的數據
normalized_data_df = pd.DataFrame({'Matrix size (N)': x_data})

# 繪製圖表
plt.figure(figsize=(12, 8))

for col in eigenvalue_columns:
    if col in data.columns:  # 確保該欄位存在
        # 計算 normalized_data
        normalized_data = np.log10((data[col] - data[col].min()) / data[col].min())
        
        # 儲存 normalized_data 到 DataFrame
        normalized_data_df[col] = normalized_data
        
        # 繪製圖表
        plt.plot(x_data, normalized_data.interpolate(), label=col, linewidth=1.5)  # 使用 interpolate 確保線條連續

# 設定標籤與標題
plt.xlabel('Matrix size (N)', fontsize=14)
plt.ylabel('Logarithm of normalized eigenvalue', fontsize=14)
plt.title(f'Eigenvalues {start}-{end} vs Matrix size', fontsize=16)

plt.ylim(-14, -10)
plt.legend(fontsize=8, title_fontsize=14)
plt.grid(True)

# 儲存圖表
output_file = f'new_plt/eigenvalues_{start}_{end}_smallest.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
plt.show()

print(f"圖表已儲存至: {output_file}")

# 儲存處理過的數據為 CSV
normalized_data_file = f'new_plt/eigenvalues_{start}_{end}_normalized_data.csv'
normalized_data_df.to_csv(normalized_data_file, index=False)
print(f"處理過的數據已儲存至: {normalized_data_file}")