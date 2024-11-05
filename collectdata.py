import pandas as pd

data_list = []

for i in range(1, 10001):
    file_name = f"energys/Energy{i}.csv"  
    try:
        df = pd.read_csv(file_name, header=None)
        first_row = df.iloc[0]
        data_list.append({'File Number': i, 'First Data': first_row.values[0]})
    except FileNotFoundError:
        print(f"檔案 {file_name} 找不到，跳過該檔案")
    except Exception as e:
        print(f"讀取檔案 {file_name} 時發生錯誤: {e}")

result_df = pd.DataFrame(data_list)
result_df.to_csv('ground_data.csv', index=False)