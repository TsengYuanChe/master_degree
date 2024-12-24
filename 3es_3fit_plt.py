import pandas as pd
import matplotlib.pyplot as plt

# 檔案路徑
files = {
    "8000": "pfit/fitting8000/8000data.csv",
    "9000": "pfit/fitting9000/9000data.csv",
    "10000": "pfit/fitting10000/10000data.csv"
}

# 初始化資料
data_dict = {}

for size, file_path in files.items():
    data = pd.read_csv(file_path)
    data_dict[size] = {
        "State": data["State"],
        "Predicted energy": data["Predicted energy"],
        "Original energy": data["Original energy"]
    }

xleft = 80
xright = 100
reference_data = pd.read_csv(files["10000"])  # 使用 10000data.csv 作為參考
ybottom = reference_data.loc[reference_data["State"] == xleft, "Original energy"].values[0] * 0.9999
ytop = reference_data.loc[reference_data["State"] == xright, "Original energy"].values[0] * 1.0001

# 繪製圖表
plt.figure(figsize=(12, 8))

for size, data in data_dict.items():
    # 繪製 Predicted energy
    plt.plot(
        data["State"], data["Predicted energy"],
        label=f"Predicted Energy (Size {size})", linestyle="-", linewidth=1.5
    )
    # 繪製 Original energy
    plt.plot(
        data["State"], data["Original energy"],
        label=f"Original Energy (Size {size})", linestyle="--", linewidth=1.5
    )

# 設定標籤與標題
plt.xlabel("State", fontsize=14)
plt.ylabel("Energy", fontsize=14)
plt.title("Comparison of Predicted and Original Energy", fontsize=16)

plt.xlim(xleft, xright)
plt.ylim(ybottom, ytop)
# 顯示圖例與格線
plt.legend(fontsize=12)
plt.grid(True)

# 儲存圖檔並顯示
output_file = "final_compare.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.show()

print(f"圖表已儲存至: {output_file}")