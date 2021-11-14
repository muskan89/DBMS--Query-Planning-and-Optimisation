import random
import string
N = 15

new_file = open("actordata.sql", 'w')
new_file.write("CREATE TABLE TableActor(a_id int,name varchar(255),PRIMARY KEY (a_id));")
new_file.write("\n")
t=300001

for i in range(1,t):
    a_id=i
    res = ''.join(random.choices(string.ascii_lowercase, k=N))
    name=str(res)
    new_file.write("INSERT INTO TableActor VALUES(")
    new_file.write(str(a_id))
    new_file.write(",'")
    new_file.write(name)
    new_file.write("');")
    new_file.write("\n")