# 可视化封装（柱状图、箱线图、热力图、网络图）

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_group_bar(df, group_col, value_cols, title=None, ylabel=None, figsize=(10, 6), rotation=30, legend_loc='best', top_n=None, horizontal=True, facet=True):
    """
    分组柱状图，支持多列对比、横向、TopN、分面。
    df: DataFrame
    group_col: 分组列名
    value_cols: 需要对比的数值列名列表
    title: 图标题
    ylabel: y轴标签
    figsize: 图尺寸
    rotation: x轴标签旋转角度
    legend_loc: 图例位置
    top_n: 只显示前N个分组（按第一个value_col排序）
    horizontal: 是否横向柱状图
    facet: 是否每个value_col单独画一张子图
    """
    group_df = df.groupby(group_col)[value_cols].mean().reset_index()
    group_df = group_df.sort_values(value_cols[0], ascending=False)
    if top_n is not None:
        group_df = group_df.head(top_n)
    if facet and len(value_cols) > 1:
        n = len(value_cols)
        fig, axes = plt.subplots(n, 1, figsize=(figsize[0], figsize[1]*n))
        for i, col in enumerate(value_cols):
            ax = axes[i]
            if horizontal:
                sns.barplot(data=group_df, y=group_col, x=col, ax=ax, orient='h')
            else:
                sns.barplot(data=group_df, x=group_col, y=col, ax=ax)
            ax.set_title(f'{col} by {group_col}')
            if horizontal:
                ax.set_ylabel(group_col)
                ax.set_xlabel(col)
            else:
                ax.set_xlabel(group_col)
                ax.set_ylabel(col)
            for label in ax.get_yticklabels():
                label.set_fontsize(10)
            for label in ax.get_xticklabels():
                label.set_fontsize(10)
                label.set_rotation(rotation)
        plt.tight_layout()
        if title:
            plt.suptitle(title, y=1.02, fontsize=16)
        plt.show()
    else:
        ax = group_df.set_index(group_col)[value_cols].plot(kind='barh' if horizontal else 'bar', figsize=figsize)
        plt.title(title or f'{group_col}分组对比')
        plt.ylabel(ylabel or group_col)
        plt.xlabel('数值')
        plt.legend(loc=legend_loc)
        plt.tight_layout()
        plt.show()

def plot_heatmap(df, columns, title=None, figsize=(10, 8), cmap='RdBu_r', center=0, annot=True, fmt='.2f'):
    """
    绘制相关性热力图
    df: DataFrame
    columns: 需要计算相关性的列名列表
    title: 图标题
    figsize: 图尺寸
    cmap: 颜色映射
    center: 颜色中心值
    annot: 是否显示数值
    fmt: 数值格式
    """
    corr = df[columns].corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr, cmap=cmap, center=center, annot=annot, fmt=fmt, square=True)
    plt.title(title or '相关性热力图')
    plt.tight_layout()
    plt.show()