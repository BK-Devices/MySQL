import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

au = input('Enter the Name of Author : ')
pu = input('Enter the Name of Publication : ')

if au == '' and pu == '':
    print("You don't enter anything")

else:
    curs.execute("select Book_Id, Book_Name, LOCATE('%s', Author), LOCATE('%s', Publication) from Books" %(au, pu))
    data = curs.fetchall()

    
    print()
    no = 0
    for rec in data:
        if rec[2] > 0 and rec[3] > 0:
            no += 1
            print('%d) %d - %s' %(no, rec[0], rec[1]))

    if no == 0:
        print('No Book having the combination of Author and Publication')

con.close()