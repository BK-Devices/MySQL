import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

try:
    id = int(input('Enter Book id : '))
    curs.execute("Select * from Books where Book_Id = %d" %id)
    data = curs.fetchall()
    if data:
        re = input('Enter Review for the Book : ')
        curs.execute("update Books set Review = '%s' where Book_Id = %d" %(re, id))
        con.commit()

        print()
        print('Book review is added')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()