import sqlite3
a = sqlite3.connect('data.db')
b = a.cursor()

b.execute("create table Flipkart(prod_id num, prod_name char)")
b.execute("insert into Flipkart values(1,'iphone')")
b.execute("insert into Flipkart values(2,'Oppo Reno7')")
b.execute("insert into Flipkart values(3,'Nokia')")
res = b.execute("Select * from Flipkart")
print(list(res))
res = b.execute("Select prod_id from Flipkart")
print(list(res))
res = b.execute("Select * from Flipkart where prod_id==1")
print(list(res))