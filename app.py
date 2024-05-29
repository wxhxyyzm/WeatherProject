from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

from mysqlutils.utils import searchPage2, searchPage3

app = Flask(__name__)
cors = CORS(app, resources={r"/getMessage": {"origins": "*"}})
cors3 = CORS(app, resources={r"/getMessage3": {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'test!'

# 监听127.0.0.1:5000/getMessage请求
@app.route('/getMessage', methods=['GET', 'POST'])
def page2():
    # 查询条件
    begin_time = request.args.get('begin_time')
    end_time = request.args.get('end_time')
    province = request.args.get('province')
    city = request.args.get('city')

    # 从数据库中取数据
    if province == '北京市' or province == '天津市' or province == '重庆市' or province == '上海市':
        city = province
    print(begin_time, " ", end_time, " ", city)
    data_dict = searchPage2(begin_time, end_time, city)
    response = {
        'msg': data_dict
    }
    print(data_dict)
    return response

# 监听127.0.0.1:5000/getMessage3请求
@app.route('/getMessage3', methods=['GET', 'POST'])
def page3():
    # 查询条件
    province = request.args.get('province')
    city = request.args.get('city')

    # 从数据库中取数据
    if province == '北京市' or province == '天津市' or province == '重庆市' or province == '上海市':
        city = province
    data_dict = searchPage3(city)
    data_add = searchPage2('2000-01-01', '2000-01-31', city)
    data_dict['LATITUDE'] = data_add['LATITUDE'][0]  # 纬度
    data_dict['LONGITUDE'] = data_add['LONGITUDE'][0]  # 经度
    print(data_dict['LATITUDE'], " ", data_dict['LONGITUDE'])
    response = {
        'msg': data_dict
    }
    print(data_dict)
    return response

if __name__ == '__main__':
    app.run()

