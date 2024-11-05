import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
data = pd.read_csv('ground_data.csv')  # Replace 'data.csv' with the actual file path

# Preview the first few rows to ensure data is loaded correctly
print(data.head())

# Plot the data assuming it's a time series or sequence (index vs. column values)
plt.figure(figsize=(10, 6))
plt.plot(data['File Number'], data['First Data'], label='Energy', color='Red', linewidth=2.5)  # data.iloc[:, 0] selects the first column
plt.xlabel('Number of matrix size (N)')  # X-axis representing index
plt.ylabel('Ground stat energy (E$_h$)')  # Y-axis representing the data values in the column
plt.xlim(left=0)
plt.ylim(0.4999999, 0.5000001)
plt.title('Plot of ground state energies')
plt.legend()
plt.grid(True)
#plt.savefig('ground_energyi.png', dpi=300, bbox_inches='tight')
plt.show()