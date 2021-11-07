import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

curs.execute("Select Book_Id, Book_Name from Books")
data = curs.fetchall()

no = 0
for rec in data:
    no += 1
    print('%d) %d - %s' %(no, rec[0], rec[1]))

con.close()