import sqlite3

try:
    connect=sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM main_product )







# try:
#     connect = sqlite3.connect('db.sqlite3')
#     cursor = connect.cursor()
#     cursor.execute('INSERT INTO main_category ("name") values ("student")')
#
#     print(cursor.fetchall())
#     cursor.close()
#     connect.commit()
# except sqlite3.Error as error:
#     print("Ошибка", error)
#
# finally:
#     print("Я выполняюсь всегда не зависимо от ошибка была или нет")
