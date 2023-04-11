import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 215606022 # Ваш chat ID, не меняйте название переменной

SGN_LVL = 0.07

def solution(x: np.array, y: np.array) -> bool:
    pval = anderson_ksamp([x, y])[2]
    if pval < SGN_LVL:
        return True
    # true: выборки не равны
    return False
