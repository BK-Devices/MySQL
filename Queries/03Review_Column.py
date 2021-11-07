import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

curs.execute("show columns from Books LIKE 'Review'")
data = curs.fetchall()
if data:
    print('Column is already exists in table')

else:
    curs.execute("ALTER TABLE Books ADD COLUMN Review varchar(500)")
    con.commit()
    print('Column is added to table')

con.close()