import pandas as pd

H0_csv = "matrix10000.csv"
V_csv = "purturb10000.csv"

H = pd.read_csv(V_csv, header=None, sep=' ').values
V = pd.read_csv(V_csv, header=None, sep=' ').values