# 提取极端天气数据
import mysql.connector
import openpyxl
import matplotlib.pyplot as plt

def msToRank(wind_ms_list):
    # 将风速转换为等级
    wind_rank_list = []  # 风力
    for i in range(len(wind_ms_list)):
        ms = wind_ms_list[i]
        if ms >= 0 and ms <= 0.2:
            wind_rank_list.append(0)  # 0级
        elif ms > 0.2 and ms <= 1.5:
            wind_rank_list.append(1)  # 1级
        elif ms > 1.5 and ms <= 3.3:
            wind_rank_list.append(2)  # 2级
        elif ms > 3.3 and ms <= 5.4:
            wind_rank_list.append(3)  # 3级
        elif ms > 5.4 and ms <= 7.9:
            wind_rank_list.append(4)  # 4级
        elif ms > 7.9 and ms <= 10.7:
            wind_rank_list.append(5)  # 5级
        elif ms > 10.7 and ms <= 13.8:
            wind_rank_list.append(6)
        elif ms > 13.8 and ms <= 17.1:
            wind_rank_list.append(7)
        elif ms > 17.1 and ms <= 20.7:
            wind_rank_list.append(8)
        elif ms > 20.7 and ms <= 24.4:
            wind_rank_list.append(9)
        elif ms > 24.4 and ms <= 28.4:
            wind_rank_list.append(10)
        elif ms > 28.4 and ms <= 32.6:
            wind_rank_list.append(11)
        elif ms > 32.6:
            wind_rank_list.append(12)
        # elif ms > 37 and ms <= 41.4:
        #     wind_rank_list.append(13)
        # elif ms > 41.4 and ms < 46.1:
        #     wind_rank_list.append(14)
        # elif ms > 46.1 and ms < 50.9:
        #     wind_rank_list.append(15)
        # elif ms > 50.9 and ms <= 56:
        #     wind_rank_list.append(16)
        # elif ms > 56 and ms <= 61.2:
        #     wind_rank_list.append(17)
        # elif ms > 61.2:
        #     wind_rank_list.append(18)
    return wind_rank_list

def count_heatwaves(temperatures, threshold):
    # 热浪天气
    heatwave_counts = {
        'weak': 0,
        'medium': 0,
        'strong': 0
    }
    consecutive_days = 0  # 对连续天数进行计数
    for temp in temperatures:
        if temp >= threshold:
            consecutive_days += 1  # 连续天数加一
        else:
            # 不连续了，就判断
            if consecutive_days >= 3 and consecutive_days < 5:
                heatwave_counts['weak'] += 1
            elif consecutive_days >= 5 and consecutive_days < 7:
                heatwave_counts['medium'] += 1
            elif consecutive_days >= 7:
                heatwave_counts['strong'] += 1
            consecutive_days = 0
    return heatwave_counts

def count_cold_waves(min_data, diff_data):
    # 寒潮
    cold_wave_counts = {
        'weak': 0,
        'medium': 0,
        'strong': 0,
        'extreme': 0
    }
    for i in range(len(min_data)):
        if min_data[i] <= 0 and diff_data[i] >= 16:
            cold_wave_counts['extreme'] += 1
        elif min_data[i] <= 0 and diff_data[i] >= 12:
            cold_wave_counts['strong'] += 1
        elif min_data[i] <= 4 and diff_data[i] >= 10:
            cold_wave_counts['medium'] += 1
        elif min_data[i] <= 4 and diff_data[i] >= 8:
            cold_wave_counts['weak'] += 1

    return cold_wave_counts

def count_rainfall_levels(rainfall_data):
    # 暴雨天气
    rainfall_counts = {
        'torrential': 0,
        'heavy': 0,
        'extreme': 0
    }

    for rainfall in rainfall_data:
        if rainfall >= 50 and rainfall < 100:
            rainfall_counts['torrential'] += 1
        elif rainfall >= 100 and rainfall < 250:
            rainfall_counts['heavy'] += 1
        elif rainfall >= 250:
            rainfall_counts['extreme'] += 1

    return rainfall_counts

def count_wind_levels(wind_rank_data):
    # 热带风暴天气
    wind_counts = {
        'Category 6': 0,
        'Category 7': 0,
        'Category 8': 0,
        'Category 9': 0,
        'Category 10': 0,
        'Category 11': 0,
        'Category 12': 0
    }
    for level in wind_rank_data:
        if level == 6:
            wind_counts['Category 6'] += 1
        elif level == 7:
            wind_counts['Category 7'] += 1
        elif level == 8:
            wind_counts['Category 8'] += 1
        elif level == 9:
            wind_counts['Category 9'] += 1
        elif level == 10:
            wind_counts['Category 10'] += 1
        elif level == 11:
            wind_counts['Category 11'] += 1
        elif level == 12:
            wind_counts['Category 12'] += 1
    return wind_counts

beginYearList = ['2000-01-01', '2001-01-01', '2002-01-01', '2003-01-01', '2004-01-01', '2005-01-01',
                 '2006-01-01', '2007-01-01', '2008-01-01', '2009-01-01', '2010-01-01', '2011-01-01',
                 '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01',
                 '2018-01-01', '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01']

endYearList = ['2000-12-31', '2001-12-31', '2002-12-31', '2003-12-31', '2004-12-31', '2005-12-31',
               '2006-12-31', '2007-12-31', '2008-12-31', '2009-12-31', '2010-12-31', '2011-12-31',
               '2012-12-31', '2013-12-31', '2014-12-31', '2015-12-31', '2016-12-31', '2017-12-31',
               '2018-12-31', '2019-12-31', '2020-12-31', '2021-12-31', '2022-12-31', '2023-12-31']

tempThresholdList = {'2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 0, '2005': 0, '2006': 0,
                     '2007': 0, '2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, '2013': 0,
                     '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0,
                     '2021': 0, '2022': 0, '2023': 0}  # 温度阈值

# MySQL数据库连接配置
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'swj',
    'database': 'climate',
}

# 连接到MySQL数据库
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# 获取所有表格的列表
show_tables_query = "SHOW TABLES"
cursor.execute(show_tables_query)
tables = cursor.fetchall()
cityList = [city for tpl in tables for city in tpl]
cities_condition = {}  # 全部城市的情况
print(cityList)  # 城市

for j in range(len(cityList)):
    city = cityList[j]  # 获取城市
    city_condition = []  # 每个城市的情况
    for i in range(len(beginYearList)):
        beginYear = beginYearList[i]  # 获取时间
        endYear = endYearList[i]  # 获取结束时间
        # 执行查询<高温阈值>
        query = f"SELECT MAX_TEMPERATURE FROM {city} WHERE TREASURE_DATE >= '{beginYear}' AND " \
                f"TREASURE_DATE <= '{endYear}' ORDER BY MAX_TEMPERATURE"
        cursor.execute(query)
        # 获取结果集
        results = cursor.fetchall()
        if results:
            # 计算95%处的索引位置
            index = int(len(results) * 0.9)
            # 获取95%处的数据
            tempThresholdF = float(results[index][0])
            # 将高温阈值写入字典
            tempThreshold = round((tempThresholdF - 32)/1.8, 2)
            tempThresholdList[beginYear] = tempThresholdF

            # 执行查询<强中弱高温热浪>
            query = f"""SELECT MAX_TEMPERATURE 
                        FROM {city} 
                        WHERE TREASURE_DATE >= '{beginYear}' AND TREASURE_DATE <= '{endYear}';"""
            cursor.execute(query)
            # 获取查询结果
            results = cursor.fetchall()
            max_list_F = [float(num) for tpl in results for num in tpl]
            heatDict = count_heatwaves(max_list_F, tempThresholdF)  # 热浪字典

            # 执行查询<寒潮>
            # 执行查询<强中弱高温热浪>
            query = f"""SELECT MIN_TEMPERATURE
                        FROM {city} 
                        WHERE TREASURE_DATE >= '{beginYear}' AND TREASURE_DATE <= '{endYear}';"""
            cursor.execute(query)
            # 获取查询结果
            results = cursor.fetchall()
            min_list = [(float(num) - 32)/1.8 for tpl in results for num in tpl]  # 低温列表
            max_list= [(fahrenheit - 32) * 5/9 for fahrenheit in max_list_F]
            diff_list = [x - y for x, y in zip(max_list, min_list)]  # 温差
            coldDict = count_cold_waves(min_list, diff_list)

            # 执行查询<暴雨>
            # 执行查询语句
            query = f"""SELECT PRCP
                        FROM {city} 
                        WHERE TREASURE_DATE >= '{beginYear}' AND TREASURE_DATE <= '{endYear}';"""
            cursor.execute(query)
            # 获取查询结果
            results = cursor.fetchall()
            rain_list = [float(num)*25.4 for tpl in results for num in tpl]
            rainDict = count_rainfall_levels(rain_list)

            # 执行查询<暴风>
            # 执行查询语句
            query = f"""SELECT MXSPD, GUST
                        FROM {city} 
                        WHERE TREASURE_DATE >= '{beginYear}' AND TREASURE_DATE <= '{endYear}';"""
            cursor.execute(query)
            # 获取查询结果
            results = cursor.fetchall()
            # 节转换为米每秒的转换因子
            knots_to_mps = 0.514444
            # 提取第一个数据的列表
            max_sus_wind_list = [float(item[0])*knots_to_mps for item in results]  # 最大持续风速
            # 提取第二个数据的列表
            max_wind_list = [float(item[1])*knots_to_mps for item in results]  # 最大阵风
            max_wind_rank_list = msToRank(max_wind_list)  # 得到风力等级
            windDict = count_wind_levels(max_wind_rank_list)

            # 将某年的数据写入
            values = [beginYear[:4], tempThreshold, heatDict['weak'], heatDict['medium'], heatDict['strong'],
                      coldDict['weak'], coldDict['medium'], coldDict['strong'], coldDict['extreme'],
                      rainDict['torrential'], rainDict['heavy'], rainDict['extreme'], windDict['Category 6'],
                      windDict['Category 7'], windDict['Category 8'], windDict['Category 9'], windDict['Category 10'],
                      windDict['Category 11'], windDict['Category 12']]
            # 写入数据
        else:
            # 写入数据
            values = [beginYear[:4], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        city_condition.append(values)
    cities_condition[city] = city_condition
    # print(cities_condition[city])
    print(city, " 的数据已经筛选完毕")
# 关闭数据库连接
cursor.close()
conn.close()
