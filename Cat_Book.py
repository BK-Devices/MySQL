import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs = con.cursor()

ct1 = input('Enter first category : ')
ct2 = input('Enter second category if not then press "Enter" : ')

if ct2 != '':
        ct3 = input('Enter third category if not then press "Enter" : ')

curs.execute("select Book_Id, Book_Name, LOCATE('%s', Category), LOCATE('%s', Category), Locate('%s', Category) from Books" %(ct1, ct2, ct3))
data = curs.fetchall()

print()
no = 0
for rec in data:
    if rec[2] > 0 and rec[3] > 0 and rec[4] > 0:
        no += 1
        print('%d) %d - %s' %(no, rec[0], rec[1]))

if no == 0:
        print('No Book having these categories')

con.close()
