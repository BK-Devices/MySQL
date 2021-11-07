import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

try:
    id = int(input('Enter Book id : '))
    curs.execute("Select * from Books where Book_Id = %d" %id)
    data = curs.fetchall()
    if data:
        print()
        print('Book Id          : %d' %id)
        print('Book Name        : %s' %data[0][1])
        print('Category         : %s' %data[0][2])
        print('Language         : %s' %data[0][3])
        print('Author of Book   : %s' %data[0][4])
        print('Publication      : %s' %data[0][5])
        print('Publication Date : %s' %data[0][6])
        print('No of Pages      : %d' %data[0][7])
        print('Edition of Book  : %s' %data[0][8])
        print('Price of Book    : %.1f' %data[0][9])
        print('Rating of Book   : %.1f' %data[0][10])
        print('Review of Book   : %s' %data[0][11])
    else:
        print()
        print('Book not found')

except:
    print()
    print('Invalid input')

con.close()