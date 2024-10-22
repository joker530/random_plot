from flask import Flask, jsonify, render_template, make_response
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import matplotlib
from flask_cors import CORS
matplotlib.use('Agg')  # 使用非 GUI 后端，不让容易出现GUI抢线程回不来的情况，会有多线程问题

app = Flask(__name__)
CORS(app)

#
def generate_random_plot():
    x = np.random.rand(10)
    y = np.random.rand(10)

    plt.figure()
    plt.scatter(x, y)
    plt.title("Random Scatter Plot")

    image_path = 'static/plot.png'  # 保存图像的路径
    plt.savefig(image_path)
    plt.close()

    return image_path


@app.route('/')
def index():
    return render_template('index.html')  # 返回 HTML 页面


@app.route('/generate_plot')
def generate_plot():
    image_path = generate_random_plot()

    # 生成一个唯一的时间戳
    unique_timestamp = int(time.time())
    unique_image_url = f"{image_path}?_={unique_timestamp}"  # 添加时间戳作为查询参数

    response = make_response(jsonify(image_url=unique_image_url))
    # 下面三行进行缓存控制
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response  # 返回 JSON 格式的图像 URL


if __name__ == '__main__':
    if not os.path.exists('static'):
        os.mkdir('static')
    app.run(host='0.0.0.0', port=5000, debug=True)   # 这里设置端口可以开放给任何主机进行访问，而不是只有本电脑能访问，并强制约定访问端口
