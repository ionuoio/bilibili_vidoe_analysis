# 统计检验（T 检验、皮尔逊相关等）
import numpy as np
from scipy import stats

def t_test(group1, group2, alpha=0.05):
    """
    两独立样本T检验
    group1, group2: array-like
    alpha: 显著性水平
    返回: p值, 是否显著
    """
    t_stat, p_value = stats.ttest_ind(group1, group2, nan_policy='omit')
    significant = p_value < alpha
    return {'t_stat': t_stat, 'p_value': p_value, 'significant': significant}

def pearson_corr(x, y):
    """
    计算皮尔逊相关系数
    x, y: array-like
    返回: 相关系数, p值
    """
    corr, p = stats.pearsonr(x, y)
    return {'corr': corr, 'p_value': p}