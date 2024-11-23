import pandas as pd

data = pd.read_csv('energy10000.csv', header=None)
your_data = data.iloc[:, 0].values

new_data = pd.DataFrame({
    'Eigenstate': range(1, len(your_data) + 1),  
    'Energy': your_data
})

new_data.to_csv('Enery_of_10000.csv', index=False)
