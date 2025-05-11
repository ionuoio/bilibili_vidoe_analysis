# Bilibili 视频数据分析项目

**项目简介**

本项目基于哔哩哔哩平台视频数据，构建从数据清洗、统计分析到可视化展示的全流程。目标是帮助内容创作者和运营人员：

* 分析不同内容分区（`tname_v2`）的播放量与互动表现差异；
* 提取标题关键词与播放量/互动率的关联；
* 构建用户互动行为指标体系，分析点赞、收藏、投币等行为偏好；
* 评估视频时长对完播率及互动率的影响；
* 挖掘高效的标签组合策略。

**技术栈**

* Python：Pandas、NumPy、Matplotlib、SciPy、jieba、mlxtend
* 可视化：Jupyter Notebook、Tableau Public
* 数据可视化：柱状图、箱线图、热力图、散点图、词云、关联规则网络图

## 项目目录结构

```plain
bilibili_analysis/
├── data/                      # 原始与处理后数据
│   ├── raw/
│   │   ├── table1.csv         # 表1: title, play_count, date, duration
│   │   └── table2.csv         # 表2: title, tname, tname_v2, view, reply, favorite, coin, share, like, dislike, tags
│   └── processed/
│       ├── merged_data.csv    # 清洗合并后的主数据表
│       └── tableau_data.csv   # 导出给 Tableau 使用的可视化数据
├── notebooks/                 # Jupyter 分析笔记本
│   ├── 1_data_preprocessing.ipynb
│   ├── 2_content_performance.ipynb
│   ├── 3_title_keyword_analysis.ipynb
│   ├── 4_user_interaction_analysis.ipynb
│   ├── 5_duration_optimization.ipynb
│   └── 6_tag_combination_strategy.ipynb
├── src/                       # 可复用模块
│   ├── data_loader.py         # 数据加载与预处理函数
│   ├── text_utils.py          # 分词与词云函数
│   ├── stats_utils.py         # 统计检验与相关性分析
│   └── viz_utils.py           # 可视化封装（柱状图、热力图、箱线图）
├── reports/                   # 输出报告与 PPT
│   └── bilibili_analysis_report.pdf
├── requirements.txt           # Python 依赖
└── README.md                  # 项目说明文档
```

## 快速开始

1. 克隆项目到本地：

   ```bash
   git clone https://github.com/yourname/bilibili_analysis.git
   cd bilibili_analysis
   ```

2. 创建并激活 Python 虚拟环境（推荐使用 conda 或 venv）：

   ```bash
   conda create -n bila_analysis python=3.8
   conda activate bila_analysis
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 将原始数据放入 `data/raw/` 目录：
   * 需要数据私信本人获取，说明来意和使用本项目的目的。
   * `table1.csv`：包含 `title, play_count, date, duration`
   * `table2.csv`：包含 `title, tname, tname_v2, view, reply, favorite, coin, share, like, dislike, tags`

## 数据预处理（Notebook 1）

运行 `notebooks/1_data_preprocessing.ipynb`：

* 读取两张原始表
* 去重、缺失值处理、类型转换（解析 `mm:ss` 时长为秒数）
* 合并成 `data/processed/merged_data.csv`

## Python 分析流程

* **内容表现分析**（notebooks/2\_content\_performance.ipynb）：分区对比播放量与互动率，用柱状图和 T 检验支持结论。
* **标题关键词分析**（notebooks/3\_title\_keyword\_analysis.ipynb）：jieba 分词、词云可视化、皮尔逊相关分析。
* **用户互动分析**（notebooks/4\_user\_interaction\_analysis.ipynb）：构建互动率矩阵，用热力图展示指标相关性。
* **时长优化**（notebooks/5\_duration\_optimization.ipynb）：时长分桶后，使用箱线图分析各区间播放量及互动率分布。
* **标签组合策略**（notebooks/6\_tag\_combination\_strategy.ipynb）：Apriori 关联规则挖掘，网络图展示高频标签组合。

## Tableau 可视化 Dashboard

1. 使用 `data/processed/tableau_data.csv` 作为数据源在 Tableau Public 中创建 Dashboard。
2. 主要页面：

   * 内容分区对比（柱状图 + 互动率颜色编码）
   * 用户行为页（热力图 + 散点图）
   * 视频时长优化页（箱线图 + 滑块筛选）
   * 标签策略页（条形图 + 关联网络图）
   * 总览页（KPI 卡片 + TopN 列表）
3. 发布到 Tableau Public，获得分享链接。

## 成果展示

* **GitHub 仓库**：[https://github.com/yourname/bilibili\_analysis](https://github.com/yourname/bilibili_analysis)
* **Tableau Dashboard**：[https://public.tableau.com/app/profile/yourname/dashboard/xxxxxxxx](https://public.tableau.com/app/profile/yourname/dashboard/xxxxxxxx)
* **项目报告**：`reports/bilibili_analysis_report.pdf`

## 联系方式

* **邮箱**：[yujia_cai@163.com](mailto:yujia_cai@163.com)


欢迎反馈与交流！
