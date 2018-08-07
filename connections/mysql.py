"""
Tute: https://pypi.org/project/PyMySQL/
http://programmingforfinance.com/2017/10/connecting-python-to-a-mysql-database-with-pymysql/
"""

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='python_init_test_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('rashmika_test@nawa.org', 'very-secret-mypassword'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('rashmika_test@nawa.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()