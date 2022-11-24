from flask import *
import datetime
import logging
import torch
import numpy as np
import shutil
import os
import core.main

UPLOAD_FOLDER = r'./uploads'
ALLOWED_EXTENSIONS = {'png', 'tiff'}

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


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    print(datetime.datetime.now(), file.filename)
    if file and allowed_file(file.filename):
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(src_path)
        shutil.copy(src_path, './tmp/ct')
        image_path = os.path.join('./tmp/ct', file.filename)
        # print(image_path)
        pid, image_info = core.main.c_main(image_path, current_app.model)
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/tmp/image/' + pid,
                        'draw_url': 'http://127.0.0.1:5003/tmp/draw/' + pid,
                        'image_info': image_info
                        })

    return jsonify({'status': 0})


# show photo
@app.route('/tmp/<path:file>', methods=['GET'])
def show_photo(file):
    # print(file)
    if file is None:
        app.logger.info('file is None')
        abort(401)
    else:
        try:
            with open(f'tmp/{file}', "rb") as f:
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
    return send_from_directory('data', file, as_attachment=True)


if __name__ == '__main__':
    # with app.app_context():
    #     current_app.model = init_model()
    app.run(host='127.0.0.1', port=5003, debug=True)
