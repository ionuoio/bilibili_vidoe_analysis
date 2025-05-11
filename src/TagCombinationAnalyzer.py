import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

class TagCombinationAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['tags_list'] = self.df['tags'].apply(lambda x: x.split(' '))
        self.transactions = self.df['tags_list'].tolist()
        self.te = TransactionEncoder()
        self.te_ary = self.te.fit(self.transactions).transform(self.transactions)
        self.tags_df = pd.DataFrame(self.te_ary, columns=self.te.columns_)
        self.rules = None

    def mine_frequent_itemsets(self, min_support=0.02):
        self.freq_itemsets = apriori(self.tags_df, min_support=min_support, use_colnames=True)
        return self.freq_itemsets

    def generate_rules(self, min_threshold=1.1):
        self.rules = association_rules(self.freq_itemsets, metric="lift", min_threshold=min_threshold)
        return self.rules

    def plot_network(self, min_lift=1.1, min_support=0.02):
        if self.rules is None:
            self.generate_rules(min_threshold=min_lift)
        G = nx.Graph()
        for _, row in self.rules.iterrows():
            if row['support'] >= min_support and row['lift'] >= min_lift:
                for a in row['antecedents']:
                    for c in row['consequents']:
                        G.add_edge(a, c, weight=row['lift'])
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, k=0.5)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=14)
        plt.title("标签高效组合网络图")
        plt.show()

    def plot_matrix(self, min_lift=1.1, min_support=0.02):
        if self.rules is None:
            self.generate_rules(min_threshold=min_lift)
        matrix = self.rules.pivot_table(index='antecedents', columns='consequents', values='lift', fill_value=0)
        plt.figure(figsize=(14, 10))
        sns.heatmap(matrix, annot=True, cmap='YlGnBu')
        plt.title("标签组合Lift矩阵")
        plt.show()

    def analyze_play_count_increase(self, tag_combo):
        # tag_combo: list of tags, e.g. ['测评', '数码']
        mask = self.df['tags_list'].apply(lambda x: all(tag in x for tag in tag_combo))
        combo_play = self.df[mask]['play_count'].mean()
        overall_play = self.df['play_count'].mean()
        increase_pct = (combo_play - overall_play) / overall_play * 100
        print(f"组合{tag_combo}出现时平均播放量：{combo_play:.0f}")
        print(f"全局平均播放量：{overall_play:.0f}")
        print(f"提升百分比：{increase_pct:.2f}%")
        return increase_pct
