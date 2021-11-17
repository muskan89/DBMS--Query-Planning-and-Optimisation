import random
import string
N = 10
N_dash=30

new_file = open("productiondata.sql", 'w')
t=80001

for i in range(1,t):
    pc_id=i
    res = ''.join(random.choices(string.ascii_lowercase , k=N))
    name=str(res)
    pes=''.join(random.choices(string.ascii_lowercase , k=N_dash))
    address=str(pes)
    new_file.write("INSERT INTO TableProductionCompany VALUES(")
    new_file.write(str(pc_id))
    new_file.write(",'")
    new_file.write(name)
    new_file.write("','")
    new_file.write(address)
    new_file.write("');")
    new_file.write("\n")