import random
import string
N = 10


new_file = open("moviedata.sql", 'w')
new_file.write("CREATE TABLE TableMovie(m_id int,name varchar(255),year int,imdbScore int,prod_company int,foreign key (prod_company) references TableProductionCompany(pc_id),PRIMARY KEY (m_id));")
new_file.write("\n")
t=1000001
#t=101

for i in range(1,t):
    m_id=i
    res = ''.join(random.choices(string.ascii_lowercase , k=N))
    name=str(res)
    year=random.randint(1900,2000)
    imdbScore=random.randint(1,5)
    prod_company=random.randint(1,80000)
    new_file.write("INSERT INTO TableMovie VALUES(")
    new_file.write(str(m_id))
    new_file.write(",'")
    new_file.write(name)
    new_file.write("',")
    new_file.write(str(year))
    new_file.write(",")
    new_file.write(str(imdbScore))
    new_file.write(",")
    new_file.write(str(prod_company))
    new_file.write(");")
    new_file.write("\n")