import pandas as pd

def clean_data(df):
    df = df.dropna()  # 简单处理缺失值
    return df