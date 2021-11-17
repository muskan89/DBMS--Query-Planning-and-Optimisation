--part a

explain analyze SELECT name FROM tablemovie WHERE imdbscore < 2;

explain analyze SELECT name FROM tablemovie WHERE imdbscore between 1.5 and 4.5;

explain analyze SELECT name FROM tablemovie WHERE year between 1900 and 1990;

explain analyze SELECT name FROM tablemovie WHERE year between 1990 and 1995;

explain analyze SELECT * FROM tablemovie WHERE prod_company < 50;

explain analyze SELECT * FROM tablemovie WHERE prod_company > 20000;







--part b


explain analyze
select tableactor.name,tablemovie.name from tableactor,tablemovie,tablecasting where tableactor.a_id<50 and tableactor.a_id=tablecasting.a_id and tablemovie.m_id=tablecasting.m_id;

explain analyze
select tableactor.name from tableactor,tablecasting where
tablecasting.m_id<50 and tableactor.a_id=tablecasting.a_id;


explain analyze
select tablemovie.name,TableProductionCompany.name from tablemovie,TableProductionCompany where tablemovie.imdbScore < 1.5 and
tablemovie.prod_company=TableProductionCompany.pc_id;

explain analyze
select tablemovie.name,TableProductionCompany.name from tablemovie,TableProductionCompany where (tablemovie.year between 1950 and 2000) and
tablemovie.prod_company=TableProductionCompany.pc_id;
