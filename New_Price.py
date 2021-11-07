import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

try:
    id = int(input('Enter Book id : '))
    curs.execute("Select Price from Books where Book_Id = %d" %id)
    data = curs.fetchall()
    if data:
        print('Price of Book is %.1f' %data[0][0])
        pr = float(input('Enter the new price of Book : '))
        curs.execute("update Books set Price = %.1f where Book_Id = %d" %(pr, id))
        con.commit()

        print()
        print('Price of Book is changed')

    else:
        print()
        print('Book does not exist')

except:
    print()
    print('Invalid input')

con.close()