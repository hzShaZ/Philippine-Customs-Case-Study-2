from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_bar_chart(top10_df: pd.DataFrame, cat_col: str, output_path: Path) -> None:
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top10_df, x=cat_col, y="sum", palette="mako")
    plt.title("Top 10 Countries by Total Dutiable Value (2015)")
    plt.xlabel("Country Origin (ISO3)")
    plt.ylabel("Dutiable Value (PHP)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    
def generate_heatmap(pivot_df: pd.DataFrame, output_path: Path) -> None:
    heatmap_data = pivot_df.drop(index="Total", columns="Total", errors="ignore")
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap="Blues", annot=False, cbar_kws={'label': 'Value (PHP)'})
    plt.title("Dutiable Value Heatmap by Origin Country and TQ")
    plt.xlabel("TQ Category")
    plt.ylabel("Country Origin (ISO3)")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()