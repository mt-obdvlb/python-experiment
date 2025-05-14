from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import pandas as pd

# 运行分析，默认聚类
def run_analysis(df):
    results = {}
    # 示例：K-Means 聚类
    k = 3
    km = KMeans(n_clusters=k)
    labels = km.fit_predict(df.select_dtypes(include=[float, int]))
    df['cluster'] = labels
    results['cluster_centers'] = km.cluster_centers_.tolist()
    # 示例：线性回归（第一个数值列 vs 第二个数值列）
    nums = df.select_dtypes(include=[float, int]).columns
    if len(nums) >= 2:
        X = df[[nums[0]]]
        y = df[nums[1]]
        lr = LinearRegression()
        lr.fit(X, y)
        results['linear_coef'] = lr.coef_[0]
        results['linear_intercept'] = lr.intercept_
    return results