# Creating table in online database

import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

curs.execute("show tables LIKE 'Books'")
data = curs.fetchall()

if data:
    print('Table is already exists in database')

else:
    curs.execute("create table Books(Book_Id int primary key NOT NULL, Book_Name varchar(200) NOT NULL, Category varchar(75), Language varchar(50), Author varchar(50), Publication varchar(50), Publication_Date varchar(20), Pages int, Edition varchar(20) default 'First', Price float check(Price > 0), Rating float)")
    con.commit()
    print('Table has been created')

con.close()