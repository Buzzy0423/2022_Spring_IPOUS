from flask import *
import datetime
import logging
import torch
import numpy as np
import shutil
import os
from core.main import process
from time import sleep

UPLOAD_FOLDER = os.path.join('data', 'unprocessed')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



# 添加header解决跨域
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


@app.route('/')
def hello_world():
    return 'Hello World!'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload/<model_name>', methods=['GET', 'POST'])
def upload_file(model_name):
    file = request.files['file']
    # print(datetime.datetime.now(), file.filename)
    # print(os.path.splitext(file.filename)[1])
    msg = ''
    if file and allowed_file(file.filename):
        file_id = find_next()
        file_name = str(file_id) + os.path.splitext(file.filename)[1]
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(src_path)
        process(src_path, model_name)
        # shutil.copy(src_path, 'data/processed')
        # msg = core.main.process(src_path, model_name)
        # if msg == 'Success':
        return jsonify({'id':file_name})
    app.logger.info("Failed to deal with image!\n", msg)
    return jsonify({'id':file_name})

def find_next():
    file_list = os.listdir(UPLOAD_FOLDER)
    max = -1
    for f in file_list:
        if not f.startswith('.'):
            id = int(os.path.splitext(f)[0])
            if id > max:
                max = id
    return max + 1


# show photo
@app.route('/show/<path:file>', methods=['GET'])
def show_photo(file):
    # print(file)
    if file is None:
        app.logger.info('file is None')
        abort(401)
    else:
        try:
            with open(f'data/processed/{file}', "rb") as f:
                image_data = f.read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
        except:
            app.logger.info('Exception!')
            abort(401)


@app.route("/download/<path:file>", methods=['GET'])
def download_file(file):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory('data/processed', file, as_attachment=True)


if __name__ == '__main__':
    # with app.app_context():
    #     current_app.model = init_model()
    app.run(host='127.0.0.1', port=5003, debug=True)
