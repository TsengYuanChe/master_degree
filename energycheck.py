import pandas as pd

data = pd.read_csv('ground_data.csv')
column = data['First Data']

a = 0
for i in range(0, len(column)):
    if column[1]>column[0]:
        print(f'incorrect at {i}')
    else:
        a = a+1
        
if a==(len(column)):
    print('All Correct')