from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import pandas as pd
from analysis.data_cleaning import clean_data
from analysis.ml_analysis import run_kmeans
from analysis.visualization import create_visualizations

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    df = pd.read_csv(filepath) if file.filename.endswith('.csv') else pd.read_excel(filepath)

    df_cleaned = clean_data(df)
    df_cleaned.to_csv(filepath, index=False)

    charts = create_visualizations(df_cleaned)
    clusters = run_kmeans(df_cleaned)

    return render_template('result.html', charts=charts, clusters=clusters)

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(UPLOAD_FOLDER, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
