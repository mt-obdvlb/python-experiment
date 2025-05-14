import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER, EXPORT_FOLDER, allowed_file
from data_processing import load_data, clean_data
from ml import run_analysis
from utils import save_file, generate_plots, export_csv

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXPORT_FOLDER'] = EXPORT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(EXPORT_FOLDER, exist_ok=True)

# 首页：上传与预览
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            filename = save_file(f, app.config['UPLOAD_FOLDER'])
            df = load_data(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('index.html', tables=[df.head().to_html(classes='data')], filename=filename)
        else:
            flash('Unsupported file type')
            return redirect(request.url)
    return render_template('index.html')

# 数据清洗
@app.route('/clean/<filename>', methods=['GET', 'POST'])
def clean(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = load_data(path)
    if request.method == 'POST':
        params = request.form.to_dict()
        cleaned = clean_data(df, params)
        cleaned_filename = 'cleaned_' + filename
        cleaned.to_csv(os.path.join(app.config['EXPORT_FOLDER'], cleaned_filename), index=False)
        return render_template('clean.html', tables=[cleaned.head().to_html(classes='data')], filename=filename)
    return render_template('clean.html', tables=[df.head().to_html(classes='data')], filename=filename)

# 分析
@app.route('/analyze/<filename>')
def analyze(filename):
    cleaned_filename = 'cleaned_' + filename
    path = os.path.join(app.config['EXPORT_FOLDER'], cleaned_filename)
    df = load_data(path)
    results = run_analysis(df)
    return render_template('analyze.html', results=results)

# 可视化
@app.route('/visualize')
def visualize():
    print('Visualizing...')
    filename = 'mock_sales.csv'
    cleaned_filename = 'cleaned_' + filename
    path = os.path.join(app.config['EXPORT_FOLDER'], cleaned_filename)
    df = load_data(path)
    plot_paths = generate_plots(df, app.config['EXPORT_FOLDER'])
    return render_template('visualize.html', plots=plot_paths)

@app.route('/download/<path:filename>')
def download(filename):
    return send_from_directory(app.config['EXPORT_FOLDER'], filename, as_attachment=True)

# 新增：静态提供 exports 文件夹下的图片
@app.route('/exports/<path:filename>')
def exports(filename):
    return send_from_directory(app.config['EXPORT_FOLDER'], filename)
if __name__ == '__main__':
    app.run(debug=True)
