import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

try:
    id = int(input('Enter the "ISBN" id of book : '))
    nm = input('Enter Book name : ')
    ct = input('Enter the category of Book separated by "/": ')
    ln = input('Enter the language of Book : ')
    au = input('Enter the Author name of Book : ')
    pu = input('Enter publication of Book : ')
    pu_dt = input('Enter date of publication dd-mm-yyyy : ')
    pg = int(input('Enter the number of pages of Book : '))
    ed = input('Enter the edition of Book : ')
    pr = float(input('Enter the price of Book > 0 : '))
    rt = float(input('Enter ratings of Book out of 5 : '))
    re = input('Enter the Rewiew of Book : ')

    curs.execute("insert into Books values(%d, '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', %f, %f, '%s')" %(id, nm, ct, ln, au, pu, pu_dt, pg, ed, pr, rt, re))
    con.commit()

    print()
    print('Your Book is added into the database')

except:
    print()
    print('Invalid input')
    print("We can't add new book into database")

con.close()