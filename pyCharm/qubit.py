import numpy as np
from scipy.linalg import kron
from IPython.display import Markdown as md


spin_up = np.array([[1, 0]]).T
spin_down = np.array([[0, 1]]).T
# bit[0] = |0>, bit[1] = |1>
bit = [spin_up, spin_down]

def basis(string='00010'):
    '''string: the qubits sequence'''
    res = np.array([[1]])
    # 从最后一位开始往前数，做直积
    for idx in string[::-1]:
        res = kron(bit[int(idx)], res)
    return np.matrix(res)
