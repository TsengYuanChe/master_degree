import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

data = pd.read_csv('ground_data.csv')

plt.figure(figsize=(14, 6))
plt.plot(data['File Number'], data['First Data'], label='Energy', color='Red', linewidth=2.5) 
plt.axhline(y=0.5, color='blue', linestyle='-', linewidth=2, label='0.5')

plt.ticklabel_format(style='plain', axis='y')
plt.tick_params(axis='y', labelsize=6)
plt.tick_params(axis='x', labelsize=16)
plt.xlabel('Number of matrix size (N)', fontsize=16)  
plt.ylabel('Ground stat energy (E$_h$)', fontsize=16) 
plt.xlim(9700,10000)
plt.ylim(0.49999999999995, 0.50000000000005)

plt.gca().yaxis.tick_right()
plt.gca().yaxis.set_label_position("right")
plt.gca().spines['right'].set_visible(True)
plt.gca().spines['left'].set_visible(False)

plt.title('Plot of ground state energies')
plt.legend()
plt.grid(True)

plt.gcf().text(
    0.1, 0.93,  # 相對座標：x=0.01, y=1.02，位於圖片框架外
    '(c)',
    fontsize=16,
    color='black',
    ha='left',  # 水平對齊
    va='top'    # 垂直對齊
)

plt.savefig('thesis/rightpartenergy.png', dpi=300, bbox_inches='tight')
plt.show()