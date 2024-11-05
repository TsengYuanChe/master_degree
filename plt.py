import numpy as np
import matplotlib.pyplot as plt

# 生成 x 值的範圍，假設 x 範圍是 -2 到 2，且步長為 0.1
x = np.linspace(-10, 10, 1000)

# 計算 y = x^6 的對應 y 值
y = x ** 6

# 繪製 x^6 的曲線
plt.plot(x, y, label='x^6', color='Red', linewidth=2.5)

# 設置標籤和標題
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^6')

# 顯示圖表
plt.grid(True)  # 可選，增加網格
plt.legend()
plt.savefig('x6.png', dpi=300, bbox_inches='tight')
plt.show()