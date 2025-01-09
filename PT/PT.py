import numpy as np
import pandas as pd

def load_matrix_from_csv(file_path):
    """
    從 CSV 檔案中讀取矩陣。
    
    參數:
        file_path (str): CSV 檔案的路徑。
    
    返回:
        ndarray: 讀取的矩陣。
    """
    return pd.read_csv(file_path, header=None).values

def load_vector_from_csv(file_path):
    """
    從 CSV 檔案中讀取向量。
    
    參數:
        file_path (str): CSV 檔案的路徑。
    
    返回:
        ndarray: 讀取的向量。
    """
    return pd.read_csv(file_path, header=None).squeeze().values

def calculate_energy_corrections(H0, V):
    """
    計算修正後的能量 E = E0 + E1 + E2。
    
    參數:
        H0 (ndarray): 未擾動的哈密頓矩陣 (N x N)。
        V (ndarray): 擾動矩陣 (N x N)。
    
    返回:
        E (ndarray): 修正後的能量 (N,)。
    """
    # 計算未擾動能量 E0 和本徵向量
    E0, eigenvectors = np.linalg.eigh(H0)

    # 初始化一階和二階能量修正
    E1 = np.zeros_like(E0)  # 一階修正
    E2 = np.zeros_like(E0)  # 二階修正

    # 一階修正: E1 = <n|V|n>
    for n in range(len(E0)):
        E1[n] = np.dot(eigenvectors[:, n].T, np.dot(V, eigenvectors[:, n]))

    # 二階修正: E2 = sum_{m != n} |<m|V|n>|^2 / (E0[n] - E0[m])
    N = len(E0)
    for n in range(N):
        for m in range(N):
            if m != n:
                V_mn = np.dot(eigenvectors[:, m].T, np.dot(V, eigenvectors[:, n]))
                E2[n] += np.abs(V_mn) ** 2 / (E0[n] - E0[m])

    # 修正後的總能量
    E = E0 + E1 + E2
    return E

if __name__ == "__main__":
    # CSV 檔案路徑
    H0_csv = "H0.csv"  # H0 為未擾動哈密頓矩陣
    V_csv = "V.csv"    # V 為擾動矩陣

    # 從 CSV 檔案讀取 H0 和 V
    H0 = load_matrix_from_csv(H0_csv)
    V = load_matrix_from_csv(V_csv)

    # 計算修正後的能量
    E = calculate_energy_corrections(H0, V)

    print("修正後的能量 E:")
    print(E)