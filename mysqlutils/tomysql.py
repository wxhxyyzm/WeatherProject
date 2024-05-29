import csv
import os
import string

import pandas as pd
import mysql.connector
import chardet

def revise(province, city):
    # 修正省份和城市
    if province == 'fujian' and city == 'fuzhou':
        city += 'fu'  # 福建福州
    elif province == 'jiangxi' and city == 'fuzhou':
        city += 'jiang'  # 江西抚州
    elif province == 'shandong' and city == 'jining':
        city += 'shan'
    elif province == 'neimenggu' and city == 'jining':
        city += 'nei'
    elif province == 'jiangsu' and city == 'suzhou':
        city += 'jiang'
    elif province == 'anhui' and city == 'suzhou':
        city += 'an'
    elif province == 'jiangsu' and city == 'taizhou':
        city += 'jiang'
    elif province == 'zhejiang' and city == 'taizhou':
        city += 'zhe'
    elif province == 'jiangxi' and city == 'yichun':
        city += 'jiang'
    elif province == 'heilongjiang' and city == 'yichun':
        city += 'hei'
    elif province == 'shaanxi' and city == 'yulin':
        city += 'shan'
    elif province == 'guangxi' and city == 'yulin':
        city += 'guang'
    return city

# 数据文件夹路径
# 获取当前工作目录的路径
current_dir = os.getcwd()

# "data"文件夹的绝对路径
data_folder = os.path.join(current_dir, '../data')

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

# 删除每个表格
for table in tables:
    table_name = table[0]
    drop_table_query = f"DROP TABLE {table_name}"
    cursor.execute(drop_table_query)
    print(f"表格 {table_name} 已删除")

conn.commit()

# 遍历数据文件夹下的所有CSV文件
for folder_name in os.listdir(data_folder):  # 省份名字
    folder_path = os.path.join(data_folder, folder_name)
    # 遍历data文件夹下所有的小文件夹，fold_name就是每个小文件夹的名字
    for inner_folder_name in os.listdir(folder_path):  # 城市名字
        inner_folder_path = os.path.join(folder_path, inner_folder_name)
        if len(os.listdir(folder_path)) == 0:
            continue
        if os.path.isdir(inner_folder_path):
            # 修正一下
            table_name = revise(folder_name, inner_folder_name)
            # # 以每个小文件夹的名字命名表
            # table_name = inner_folder_name

            # 创建表
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (STATION VARCHAR(255), TREASURE_DATE VARCHAR(255), LATITUDE VARCHAR(255), LONGITUDE VARCHAR(255), ELEVATION VARCHAR(255), STATION_NAME VARCHAR(255), TEMP VARCHAR(255), TEMP_ATTRIBUTES VARCHAR(255), DEWP VARCHAR(255), DEWP_ATTRIBUTES VARCHAR(255), SLP VARCHAR(255), SLP_ATTRIBUTES VARCHAR(255), STP VARCHAR(255), STP_ATTRIBUTES VARCHAR(255), VISIB VARCHAR(255), VISIB_ATTRIBUTES VARCHAR(255), WDSP VARCHAR(255), WDSP_ATTRIBUTES VARCHAR(255), MXSPD VARCHAR(255), GUST VARCHAR(255), MAX_TEMPERATURE VARCHAR(255), MAX_ATTRIBUTES VARCHAR(255), MIN_TEMPERATURE VARCHAR(255), MIN_ATTRIBUTES VARCHAR(255), PRCP VARCHAR(255), PRCP_ATTRIBUTES VARCHAR(255), SNDP VARCHAR(255), FRSHTT VARCHAR(255));"
            print(create_table_query)
            cursor.execute(create_table_query)
            conn.commit()

            # 检查表中是否已经存在数据
            check_data_query = f"SELECT COUNT(*) FROM {table_name}"
            cursor.execute(check_data_query)
            result = cursor.fetchone()

            if result[0] == 0:
                #  如果表中没有数据，则读取csv文件内容并插入到表中
                for file_name in os.listdir(inner_folder_path):
                    if file_name.endswith('.csv'):
                        file_path = os.path.join(inner_folder_path, file_name)
                        with open(file_path, 'r') as csv_file:
                            csv_reader = csv.reader(csv_file)
                            next(csv_reader)  # 跳过标题行
                            for row in csv_reader:
                                row = ['0.00' if value == '9999.9' or value == '999.9' or value == '99.99' else value
                                       for value in row]
                                # 改一下时间格式
                                row[1] = row[1].replace('/', '-')
                                year, month, day = row[1].split("-")
                                month = month.zfill(2)
                                day = day.zfill(2)
                                row[1] = ""
                                row[1] = "-".join([year, month, day])
                                # 查询语句
                                insert_query = f"INSERT INTO {table_name} (STATION, TREASURE_DATE, LATITUDE, LONGITUDE, " \
                                               f"ELEVATION, STATION_NAME, TEMP, TEMP_ATTRIBUTES, DEWP, DEWP_ATTRIBUTES, " \
                                               f"SLP, SLP_ATTRIBUTES, STP, STP_ATTRIBUTES, VISIB, VISIB_ATTRIBUTES, " \
                                               f"WDSP, WDSP_ATTRIBUTES, MXSPD, GUST, MAX_TEMPERATURE, MAX_ATTRIBUTES, " \
                                               f"MIN_TEMPERATURE, MIN_ATTRIBUTES, PRCP, PRCP_ATTRIBUTES, SNDP, FRSHTT) VALUES (%s, %s, %s, %s, " \
                                               f"%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
                                cursor.execute(insert_query, row)
                            conn.commit()
                print(f"<{table_name}> 表已经创建完成并插入数据")
            else:
                # 如果表中已经存在数据，读取csv文件内容并追加到表中
                for file_name in os.listdir(inner_folder_path):
                    if file_name.endswith('.csv'):
                        file_path = os.path.join(inner_folder_path, file_name)
                        with open(file_path, 'r') as csv_file:
                            csv_reader = csv.reader(csv_file)
                            next(csv_reader)  # 跳过标题行
                            for row in csv_reader:
                                row = ['0.00' if value == '9999.9' or value == '999.9' or value == '99.99' else value
                                       for value in row]
                                row[1] = row[1].replace('/', '-')
                                year, month, day = row[1].split("-")
                                month = month.zfill(2)
                                day = day.zfill(2)
                                row[1] = ""
                                row[1] = "-".join([year, month, day])
                                insert_query = f"INSERT INTO {table_name} (STATION, TREASURE_DATE, LATITUDE, LONGITUDE, " \
                                               f"ELEVATION, STATION_NAME, TEMP, TEMP_ATTRIBUTES, DEWP, DEWP_ATTRIBUTES, " \
                                               f"SLP, SLP_ATTRIBUTES, STP, STP_ATTRIBUTES, VISIB, VISIB_ATTRIBUTES, " \
                                               f"WDSP, WDSP_ATTRIBUTES, MXSPD, GUST, MAX_TEMPERATURE, MAX_ATTRIBUTES, " \
                                               f"MIN_TEMPERATURE, MIN_ATTRIBUTES, PRCP, PRCP_ATTRIBUTES, SNDP, FRSHTT) VALUES (%s, %s, %s, %s, " \
                                               f"%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s)"
                                cursor.execute(insert_query, row)
                            conn.commit()
                print(f"<{table_name}> 表已经存在，并追加数据")

# 关闭数据库连接
cursor.close()
conn.close()