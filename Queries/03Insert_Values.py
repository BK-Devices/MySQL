# Inserting values in Online database table
# This program is run only once

# Inserting values in Online database table

import mysql.connector as my

con = my.connect(host='bqltptwhptjkoscudwi2-mysql.services.clever-cloud.com', user='umlcfuqf0izu5gll', password='2phqaWmF5ZJtwkS510UY', database='bqltptwhptjkoscudwi2')
curs=con.cursor()

file = open("Book.csv", "r")

try:
    no = 0
    for rec in file:
        if no != 0:
            print('hello')
            sr_no = int(rec.split(',')[0])
            id = int(rec.split(',')[1])
            nm = rec.split(',')[2]
            ct = rec.split(',')[3]
            ln = rec.split(',')[4]
            au = rec.split(',')[5]
            pu = rec.split(',')[6]
            pu_dt = str(rec.split(',')[7])
            pg = int(rec.split(',')[8])
            ed = rec.split(',')[9]
            pr = float(rec.split(',')[10])
            rt = float(rec.split(',')[11])
            re = ''

            curs.execute("insert into Books values(%d, '%s', '%s', '%s', '%s', '%s', '%s', %d, '%s', %.1f, %.1f, '%s')" %(id, nm, ct, ln, au, pu, pu_dt, pg, ed, pr, rt, re))
            con.commit()

            print('Book %d is added to database' %sr_no)
        no += 1

except:
    print('These values are already added')

con.close()
