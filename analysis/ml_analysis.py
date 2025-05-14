from sklearn.cluster import KMeans
import pandas as pd

def run_kmeans(df):
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        return '无数值列用于聚类'
    model = KMeans(n_clusters=3)
    model.fit(numeric_df)
    return pd.Series(model.labels_).value_counts().to_dict()