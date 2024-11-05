import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_list = []
# Load the CSV file
data = pd.read_csv('energy10000.csv', header=None)  # Replace 'data.csv' with the actual file path
for i in range(1, 10000):
    first_column = data.iloc[:,0]
    data_list.append({'File Number': i, 'First Data': first_column.values[i]})
    
df = pd.DataFrame(data_list)
# Preview the first few rows to ensure data is loaded correctly
print(df.head())

plt.figure(figsize=(10, 6))
plt.plot(df['File Number'], df['First Data'], label='Energy', color='Red', linewidth=2.5)
plt.plot(df['File Number'], (df['File Number'])**2/3, label='x^2', color='Green', linewidth=2.5)
plt.plot(df['File Number'], (df['File Number'])**3/20000, label='x^3', color='Blue', linewidth=2.5)
#plt.plot(df['File Number'], np.exp(df['File Number'])/(1000000000000000*1000000000000000), label='e^x', color='Yellow', linewidth=2.5)
plt.xlabel('Number of eigenstates')  # X-axis representing index
plt.ylabel('Energy (E$_h$)')  # Y-axis representing the data values in the column
plt.xlim(left=0)
plt.ylim(0, max(df['First Data']))
plt.title('Plot of energies for different eigenstates')
plt.legend()
plt.grid(True)
plt.savefig('10000eeee.png', dpi=300, bbox_inches='tight')
plt.show()