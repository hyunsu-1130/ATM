import pymysql
import pandas as pd

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='k8339970!', db='atm', charset='utf8',
                       autocommit=True, cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()


# 특정 데이터 불러오기
sql = "SELECT * FROM `user info`"
cursor.execute(sql)

rows = cursor.fetchall()


# 결과 출력
for row in rows:
    print(row)

customers = pd.DataFrame(rows)
print(customers)



# 연결 종료
cursor.close()
conn.close()






