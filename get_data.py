import pandas as pd
import numpy as np
import os

# 构造 30 天模拟销售记录
data = {
    '日期': pd.date_range(start='2023-01-01', periods=30),
    '销量': np.random.randint(100, 500, size=30),
    '价格': np.round(np.random.uniform(10.0, 20.0, size=30), 2),
    '地区': np.random.choice(['华东', '华南', '华北', '西南'], size=30)
}
df = pd.DataFrame(data)

# 确保导出目录存在
os.makedirs("exports", exist_ok=True)
df.to_csv('exports/mock_sales.csv', index=False)