'''-----------------------------------JAIWANT D--------------------------------------
------------------------------------------------------------------------------------
                                      _oo0oo_
                                     o8888888o
                                     88" . "88
                                     (| -_- |)
                                     0\  =  /0
                                   ___/`---'\___
                                 .' \\|     |// '.
                                / \\|||  :  |||// |
                               / _||||| -:- |||||- |
                              |   | \\\  -  /// |   |
                              | \_|  ''\---/''  |_/ |
                              \  .-\__  '-'  ___/-. /
                            ___'. .'  /--.--\  `. .'___
                         ."" '<  `.___\_<|>_/___.' >' "".
                        | | :  `- \`.;`\ _ /`;.`/ - ` : | |
                        \  \ `_.   \_ __\ /__ _/   .-` /  /
                      =====`-.____`.___ \_____/___.-`___.-'=====
                                      `=---='
------------------------------------------------------------------------------------'''



# from flask import Flask, request, render_template, redirect, url_for
# import os
# import shutil
# import numpy as np
# from werkzeug.utils import secure_filename
# from tensorflow.keras.models import load_model
# from PIL import Image, ImageOps
# import io

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['MODEL_PATH'] = 'keras_Model.h5'
# app.config['LABELS_PATH'] = 'labels.txt'
# app.config['PRICES'] = {
#     '0 none': 10.0,
#     '1 book': 15.0,
#     'Item3': 20.0
# }

# # Ensure the uploads folder exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# # Load the model and labels
# model = load_model(app.config['MODEL_PATH'], compile=False)
# class_names = open(app.config['LABELS_PATH'], 'r').read().splitlines()

# def classify_image(image_path):
#     data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
#     image = Image.open(image_path).convert('RGB')
#     image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
#     image_array = np.asarray(image)
#     normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
#     data[0] = normalized_image_array
#     prediction = model.predict(data)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     return class_name

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'file' in request.files:
#             files = request.files.getlist('file')
#             for file in files:
#                 if file and file.filename != '':
#                     filename = secure_filename(file.filename)
#                     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#                     file.save(file_path)
#             return redirect(url_for('index'))
#         elif 'proceed' in request.form:
#             return redirect(url_for('billing'))
#     return render_template('index.html')

# @app.route('/billing')
# def billing():
#     items = []
#     total_amount = 0.0

#     for filename in os.listdir(app.config['UPLOAD_FOLDER']):
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         class_name = classify_image(file_path)
#         price = app.config['PRICES'].get(class_name, 0)
#         total_amount += price
#         items.append({'name': class_name, 'price': price})

#     return render_template('billing.html', items=items, total_amount=total_amount)

# @app.route('/new_user', methods=['POST'])
# def new_user():
#     # Delete the uploads folder
#     if os.path.exists(app.config['UPLOAD_FOLDER']):
#         shutil.rmtree(app.config['UPLOAD_FOLDER'])
#     # Recreate the uploads folder
#     os.makedirs(app.config['UPLOAD_FOLDER'])
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)

'''----------------------------------------------------------------------------------------------------------'''
'''
    Above code works perfect for new user.
    In case of miscommits, rollback to it.
'''

'''New with existing modification'''

from flask import Flask, request, render_template, redirect, url_for
import os
import shutil
import numpy as np
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps
import io
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MODEL_PATH'] = 'keras_Model.h5'
app.config['LABELS_PATH'] = 'labels.txt'
app.config['PRICES'] = {
    'Item1': 10.0,
    'Item2': 15.0,
    'Item3': 20.0
}

# Ensure the uploads folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

'''
        ________TRAINING DATASET STARTS HERE________
'''
model = load_model(app.config['MODEL_PATH'], compile=False)
class_names = open(app.config['LABELS_PATH'], 'r').read().splitlines()

def classify_image(image_path):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert('RGB')
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    return class_name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            files = request.files.getlist('file')
            for file in files:
                if file and file.filename != '':
    # Add a timestamp: File change conflict ah epoch value genrate pannadhula irundhu evlo time eduthirukku retrive panni andha value ah file namme oda prefix la vecha problem soved!!!!
                    timestamp = str(int(time.time()))
                    filename = secure_filename(f"{timestamp}_{file.filename}")
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
            return redirect(url_for('index'))
        elif 'proceed' in request.form:
            return redirect(url_for('billing'))
        elif 'continue' in request.form:
            return redirect(url_for('index'))  # Veetukku poga return button -> redirct function use pannanum
    return render_template('index.html')

@app.route('/billing')
def billing():
    items = []
    total_amount = 0.0

    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        class_name = classify_image(file_path)
        price = app.config['PRICES'].get(class_name, 0)
        total_amount += price
        items.append({'name': class_name, 'price': price})

    return render_template('billing.html', items=items, total_amount=total_amount)

@app.route('/new_user', methods=['POST'])
def new_user():
    # Delete the uploads folder  
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        shutil.rmtree(app.config['UPLOAD_FOLDER'])
    # Recreate the uploads folder
    os.makedirs(app.config['UPLOAD_FOLDER'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
