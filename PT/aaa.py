import pandas as pd

data = pd.read_csv('matrix10000.csv', header=None, skip_blank_lines=True).values

print(data[10000, 10000])