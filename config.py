import os

# 项目根目录
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# 上传文件夹
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
# 导出文件夹
EXPORT_FOLDER = os.path.join(BASE_DIR, 'exports')
# 允许的文件后缀
ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx'}

# 检查文件是否允许上传

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
