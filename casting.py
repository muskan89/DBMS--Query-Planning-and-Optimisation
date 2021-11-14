'''import random
import string



new_file = open("castingdata.sql", 'w')
new_file.write("CREATE TABLE TableCasting(m_id int,a_id int,foreign key (m_id) references TableMovie(m_id),foreign key (a_id) references TableActor(a_id),PRIMARY KEY (m_id,a_id));")
new_file.write("\n")
t=1000001
#t=101

for i in range(1,t):

    new_file.write("INSERT INTO TableCasting VALUES(")





    new_file.write(");")
    new_file.write("\n")'''
import random
import string
import sys

sys.stdout = open('castingdata.sql', 'a')
num = 10 ** 6
sin_comma = "'"
comma = ","
table_name = "TableCasting"
arr = []
for i in range(1, num + 1):
    s = set()
    while len(s) < 4:
        actor = random.randint(1, 300000)
        s.add(actor)

    for j in s:
        values = str(i) + comma + str(j)
        arr.append(f"INSERT INTO {table_name} VALUES({values});")
random.shuffle(arr)
print(*arr, sep="\n")

"""
truncate table Actor;
"""

"""
How to run;
python movie.py
"""