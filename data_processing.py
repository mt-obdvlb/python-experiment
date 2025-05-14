import pandas as pd

# 加载数据
def load_data(filepath):
    ext = filepath.rsplit('.', 1)[1].lower()
    if ext == 'csv':
        return pd.read_csv(filepath)
    else:
        return pd.read_excel(filepath)

# 数据清洗
def clean_data(df, params):
    # 缺失值处理
    method = params.get('na_method', 'drop')
    if method == 'drop':
        df = df.dropna()
    elif method == 'fill_mean':
        df = df.fillna(df.mean())
    # 异常值检测（简单示例: z-score）
    if params.get('outlier') == 'remove':
        from scipy import stats
        df = df[(stats.zscore(df.select_dtypes(include=[float, int])) < 3).all(axis=1)]
    return df