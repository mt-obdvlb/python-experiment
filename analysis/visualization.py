import seaborn as sns
import matplotlib.pyplot as plt
import os
import uuid

CHART_DIR = 'static'
os.makedirs(CHART_DIR, exist_ok=True)


def create_visualizations(df):
    charts = []
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols[:3]:
        plt.figure()
        sns.histplot(df[col], kde=True)
        path = os.path.join(CHART_DIR, f"{uuid.uuid4()}.png")
        plt.savefig(path)
        charts.append('/' + path)
        plt.close()
    return charts
