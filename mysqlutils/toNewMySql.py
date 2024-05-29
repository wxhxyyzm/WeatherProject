import extract
import mysql.connector

# 创建表
def create_table(city):
    create_query = f'''CREATE TABLE IF NOT EXISTS {city} (
                        YearData VARCHAR(255),
                        High_Threshold VARCHAR(255),
                        Weak_Heatwave VARCHAR(255),
                        Moderate_Heatwave VARCHAR(255),
                        Strong_Heatwave VARCHAR(255),
                        General_Coldwave VARCHAR(255),
                        Moderate_Coldwave VARCHAR(255),
                        Strong_Coldwave VARCHAR(255),
                        Severe_Coldwave VARCHAR(255),
                        Heavy_Rainfall VARCHAR(255),
                        Severe_Rainfall VARCHAR(255),
                        Extreme_Rainfall VARCHAR(255),
                        Grade_6_Wind VARCHAR(255),
                        Grade_7_Wind VARCHAR(255),
                        Grade_8_Wind VARCHAR(255),
                        Grade_9_Wind VARCHAR(255),
                        Grade_10_Wind VARCHAR(255),
                        Grade_11_Wind VARCHAR(255),
                        Grade_12_Wind VARCHAR(255)
                    )'''
    cursor.execute(create_query)

# 遍历字典并录入数据
def insert_data(city, weather_data):
    for data in weather_data:
        insert_query = f"INSERT INTO {city} (YearData, High_Threshold, Weak_Heatwave, Moderate_Heatwave, " \
                       f"Strong_Heatwave, General_Coldwave,  Moderate_Coldwave, Strong_Coldwave, Severe_Coldwave, Heavy_Rainfall, " \
                       f"Severe_Rainfall, Extreme_Rainfall, Grade_6_Wind, Grade_7_Wind, Grade_8_Wind, Grade_9_Wind, " \
                       f"Grade_10_Wind, Grade_11_Wind, Grade_12_Wind) VALUES (%s, %s, %s, %s, " \
                       f"%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s)"
        print(data)
        cursor.execute(insert_query, data)


# 将新数据写入新的数据库
cities_condition = extract.cities_condition

# MySQL数据库连接配置
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'swj',
    'database': 'statistic',
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

# weather_dict = {
#     'City1': [
#         [2020, 30, 5, 2, 1, 10, 2, 1, 0, 50, 20, 5, 6, 7, 8, 9, 10, 11, 12],
#         [2021, 32, 8, 3, 2, 12, 3, 2, 0, 60, 25, 8, 7, 8, 9, 10, 11, 12, 13]
#     ],
#     'City2': [
#         [2020, 28, 3, 1, 0, 8, 1, 0, 0, 40, 18, 4, 5, 6, 7, 8, 9, 10, 11]
#     ]
# }

# 遍历字典并创建表，插入数据
for city, weather_data in cities_condition.items():
    create_table(city)
    insert_data(city, weather_data)
    print(city + " 数据已经录入完毕...")

# 提交更改并关闭连接
conn.commit()
cursor.close()
conn.close()

