import numpy as np
import pandas as pd
import os
from mpmath import mp

def load_matrix_from_csv(file_path):
    """從 CSV 檔案讀取矩陣，嘗試自動識別分隔符。"""
    print(f'Loading: {file_path}')
    # 嘗試不同的分隔符
    possible_separators = ['\t', ',', ' ']
    for sep in possible_separators:
        try:
            data = pd.read_csv(file_path, header=None, sep=sep).values
            print(f"Loaded matrix with separator '{sep}', shape: {data.shape}")
            if data.shape[0] == data.shape[1]:
                return data
        except Exception as e:
            continue
    raise ValueError(f"無法正確讀取檔案，請檢查格式：{file_path}")

def load_vector_from_csv(file_path):
    """從 CSV 檔案讀取單列向量。"""
    print(f'Loading: {file_path}')
    return pd.read_csv(file_path, header=None).squeeze().values  # 將單列數據轉換為一維向量

def save_vector_to_csv(vector, file_path):
    """
    將高精度向量儲存到 CSV 檔案。
    
    參數:
        vector (list): 高精度數值列表。
        file_path (str): 輸出的檔案路徑。
    """
    print(f"Saving E to: {file_path}")
    # 將每個數字格式化為小數點後 24 位的字串
    formatted_vector = [f"{x:.24f}" for x in vector]
    pd.DataFrame(formatted_vector).to_csv(file_path, header=False, index=False)
    
def calculate_energy_corrections(H0, V, E0, limit):
    """
    計算修正後的能量 E = E0 + E1 + E2，使用 numpy。
    
    參數:
        H0 (ndarray): 未擾動的哈密頓矩陣 (N x N)。
        V (ndarray): 擾動矩陣 (N x N)。
        E0 (ndarray): 預計算的本徵值 (N,)。
    
    返回:
        E (ndarray): 修正後的能量 (N,)。
    """
    # 計算本徵值和本徵向量
    print("計算本徵向量...")
    _, eigenvectors = np.linalg.eigh(H0)

    # 初始化一階和二階修正
    E1 = np.zeros_like(E0)
    E2 = np.zeros_like(E0)

    # 計算一階修正
    print("計算一階修正...")
    for n in range(limit):
        E1[n] = np.dot(eigenvectors[:, n].T, np.dot(V, eigenvectors[:, n]))

    # 計算二階修正
    print("計算二階修正...")
    for n in range(limit):
        for m in range(len(E0)):
            if m != n:
                V_mn = np.dot(eigenvectors[:, m].T, np.dot(V, eigenvectors[:, n]))
                E2[n] += (np.abs(V_mn) ** 2) / (E0[n] - E0[m])
            print(n, m)

    # 計算修正後的總能量
    E = E0 + E1 + E2
    return E

def save_energy_comparison_to_csv(E0, E, file_path):
    """
    將 E0、E 和能量差儲存到三欄的 CSV 檔案。
    
    參數:
        E0 (list or ndarray): 未擾動能量值。
        E (list or ndarray): 修正後的能量值。
        file_path (str): 輸出的檔案路徑。
    """
    print(f"Saving comparison to: {file_path}")
    # 計算能量差
    energy_diff = np.array(E0) - np.array(E)
    log_diff = np.log10(abs(energy_diff))
    # 建立 DataFrame
    data = pd.DataFrame({
        "E0": E0,
        "E": E,
        "diff": energy_diff,
        "log(diff)": log_diff,
    })
    # 儲存到 CSV
    data.to_csv(file_path, index=False)
    print(f"成功存到:{file_path}")

if __name__ == "__main__":
    # 檔案路徑
    limit = 10
    maximumsize = 10

    H0_csv = "matrix10000.csv"      # 未擾動哈密頓矩陣
    V_csv = "purturb10000.csv"     # 擾動矩陣
    E0_csv = "energy10000.csv"
    saving_csv = f'PT/{maximumsize}matrix_{limit}states.csv'

    # 讀取矩陣
    H0 = load_matrix_from_csv(H0_csv)
    V = load_matrix_from_csv(V_csv)
    E0 = load_vector_from_csv(E0_csv)

    V = V * 2*10**(-11)
    
    H0 = H0[:maximumsize, :maximumsize]
    V = V[:maximumsize, :maximumsize]
    E0 = E0[:maximumsize]

    # 計算修正後的能量
    print("開始計算能量修正...")
    E = calculate_energy_corrections(H0, V, E0, limit)
    save_energy_comparison_to_csv(E0[:limit], E, saving_csv)
