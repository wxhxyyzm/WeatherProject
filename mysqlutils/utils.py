# 数据库工具
import mysql.connector
from pypinyin import pinyin, Style

def hanzi_to_pinyin(hanzi):
    # 转换为不带声调的拼音
    pinyin_list = pinyin(hanzi, style=Style.NORMAL)
    flatten_list = [element for sublist in pinyin_list for element in sublist]
    length = len(flatten_list)
    if flatten_list[length - 1] == 'shi':
        length -= 1
    pinyin_str = ""
    for i in range(length):
        pinyin_str += flatten_list[i]
    # 拼接成字符串并返回
    return pinyin_str



def searchPage2(begin, end, city):
    # 在函数内链接数据库
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '111111',
        'database': 'climate',
    }  # 数据库配置

    # 连接到MySQL数据库
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()
    # 查询第二页
    # 给定起始时间和终止时间查询温度、露点温度、降水、可见度、风速等信息
    city = hanzi_to_pinyin(city)
    # 构建查询语句
    query = f"SELECT TREASURE_DATE, LATITUDE, LONGITUDE, TEMP, MAX_TEMPERATURE, MIN_TEMPERATURE, DEWP, VISIB, WDSP, MXSPD, GUST, PRCP, SNDP FROM {city} WHERE TREASURE_DATE BETWEEN %s AND %s"
    # 执行查询
    cursor.execute(query, (begin, end))
    # 提取查询结果
    result = cursor.fetchall()
    # 构造字典形式的结果
    data = {'TREASURE_DATE': [], 'LATITUDE': [], 'LONGITUDE': [], 'TEMP': [], 'MAX_TEMPERATURE': [],
            'MIN_TEMPERATURE': [], 'DEWP': [], 'VISIB': [], 'WDSP': [],
            'MXSPD': [], 'GUST': [], 'PRCP': [], 'SNDP': []}  # 构建字典
    for row in result:
        row = ['0.00' if value == '9999.9' or value == '999.9' or value == '99.99' else value for value in row]
        data['TREASURE_DATE'].append(row[0])
        data['LATITUDE'].append(row[1])
        data['LONGITUDE'].append(row[2])
        data['TEMP'].append(str(round((float(row[3]) - 32)/1.8, 2)))  # 摄氏度
        data['MAX_TEMPERATURE'].append(str(round((float(row[4]) - 32)/1.8, 2)))  # 摄氏度
        data['MIN_TEMPERATURE'].append(str(round((float(row[5]) - 32)/1.8, 2)))  # 摄氏度
        data['DEWP'].append(str(round((float(row[6]) - 32)/1.8, 2)))  # 摄氏度
        data['VISIB'].append(str(round(float(row[7])*1.609344, 2)))
        data['WDSP'].append(str(round(float(row[8])*0.5144, 2)))
        data['MXSPD'].append(str(round(float(row[9])*0.5144, 2)))
        data['GUST'].append(str(round(float(row[10])*0.5144, 2)))
        data['PRCP'].append(str(round(float(row[11])*25.4, 2)))  # 降雨转换为mm
        data['SNDP'].append(str(round(float(row[12])*25.4, 2)))

    # 关闭数据库连接
    cursor.close()
    conn.close()

    return data

def searchPage3(city):
    # 查询第三页
    # 在函数内链接数据库
    mysql_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '111111',
        'database': 'statistic',
    }  # 数据库配置

    # 连接到MySQL数据库
    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    # 查询第三页
    # 给定起始时间和终止时间查询温度、露点温度、降水、可见度、风速等信息
    city = hanzi_to_pinyin(city)
    begin = "2000"
    end = "2023"
    # 构建查询语句
    query = f"SELECT YearData, High_Threshold, Weak_Heatwave, Moderate_Heatwave, Strong_Heatwave, " \
            f"General_Coldwave, Moderate_Coldwave, Strong_Coldwave, Severe_Coldwave, Heavy_Rainfall, " \
            f"Severe_Rainfall, Extreme_Rainfall, Grade_6_Wind, Grade_7_Wind, Grade_8_Wind, Grade_9_Wind, " \
            f"Grade_10_Wind, Grade_11_Wind, Grade_12_Wind FROM {city} WHERE YearData BETWEEN %s AND %s"
    # 执行查询
    cursor.execute(query, (begin, end))
    # 提取查询结果
    result = cursor.fetchall()
    # 构造字典形式的结果
    data = {'YearData': [], 'High_Threshold': [], 'Weak_Heatwave': [], 'Moderate_Heatwave': [], 'Strong_Heatwave': [],
            'General_Coldwave': [], 'Moderate_Coldwave': [], 'Strong_Coldwave': [], 'Severe_Coldwave': [],
            'Heavy_Rainfall': [], 'Severe_Rainfall': [], 'Extreme_Rainfall': [], 'Grade_6_Wind': [], 'Grade_7_Wind': [],
            'Grade_8_Wind': [], 'Grade_9_Wind': [], 'Grade_10_Wind': [], 'Grade_11_Wind': [], 'Grade_12_Wind': []}  # 构建字典
    for row in result:
        row = ['0.00' if value == '9999.9' or value == '999.9' or value == '99.99' else value for value in row]
        data['YearData'].append(row[0])
        data['High_Threshold'].append(row[1])
        data['Weak_Heatwave'].append(row[2])
        data['Moderate_Heatwave'].append(row[3])
        data['Strong_Heatwave'].append(row[4])
        data['General_Coldwave'].append(row[5])
        data['Moderate_Coldwave'].append(row[6])
        data['Strong_Coldwave'].append(row[7])
        data['Severe_Coldwave'].append(row[8])
        data['Heavy_Rainfall'].append(row[9])
        data['Severe_Rainfall'].append(row[10])
        data['Extreme_Rainfall'].append(row[11])
        data['Grade_6_Wind'].append(row[12])
        data['Grade_7_Wind'].append(row[13])
        data['Grade_8_Wind'].append(row[14])
        data['Grade_9_Wind'].append(row[15])
        data['Grade_10_Wind'].append(row[16])
        data['Grade_11_Wind'].append(row[17])
        data['Grade_12_Wind'].append(row[18])

    # 关闭数据库连接
    cursor.close()
    conn.close()

    return data


