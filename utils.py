import os
import matplotlib
matplotlib.use('Agg')
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt

# 保存上传的文件
def save_file(fileobj, folder):
    filename = secure_filename(fileobj.filename)
    path = os.path.join(folder, filename)
    fileobj.save(path)
    return filename

# 导出 CSV
def export_csv(df, folder, filename):
    path = os.path.join(folder, filename)
    df.to_csv(path, index=False)
    return filename

# 生成图表，返回文件路径列表
def generate_plots(df, export_folder):
    plot_paths = []
    # 生成直方图示例
    nums = df.select_dtypes(include=[float, int]).columns
    for col in nums[:3]:
        plt.figure()
        df[col].hist()
        fname = f"hist_{col}.png"
        path = os.path.join(export_folder, fname)
        plt.savefig(path)
        plt.close()
        plot_paths.append(fname)
    return plot_paths