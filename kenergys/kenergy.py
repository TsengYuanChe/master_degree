import pandas as pd

# 計算 k 從 0 到 9999 的 E 值
state = range(1,10002)
energy = [4 * (k-1) * (k + 1) / 10 for k in state]

# 創建 DataFrame
data = pd.DataFrame({'Eigenstate': state, 'E': energy})

# 儲存到 CSV 文件
output_file = 'kenergy10000.csv'
data.to_csv(output_file, index=False)

print(f"已將 k 和 E 的值儲存到 {output_file} 中。")