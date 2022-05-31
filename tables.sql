CREATE TABLE TableActor(a_id int,name varchar(255),PRIMARY KEY (a_id));
CREATE TABLE TableProductionCompany(pc_id int,name varchar(255),address varchar(255),PRIMARY KEY (pc_id));
CREATE TABLE TableMovie(m_id int,name varchar(255),year int,imdbScore int,prod_company int,foreign key (prod_company) references TableProductionCompany(pc_id),PRIMARY KEY (m_id));
CREATE TABLE TableCasting(m_id int,a_id int,foreign key (m_id) references TableMovie(m_id),foreign key (a_id) references TableActor(a_id),PRIMARY KEY (m_id,a_id));




