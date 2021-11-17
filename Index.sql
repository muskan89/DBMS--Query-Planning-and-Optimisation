CREATE INDEX idx_actor_aid 
ON TableActor(a_id);


CREATE INDEX idx_movie_mid 
ON TableMovie(m_id);

CREATE INDEX idx_movie_imdbScore
ON TableMovie(imdbScore);


CREATE INDEX idx_movie_year
ON TableMovie(year);


CREATE INDEX idx_casting_mid
ON TableCasting(m_id);



CREATE INDEX idx_casting_aid
ON TableCasting(a_id);



CREATE INDEX idx_movie_pcid
ON TableMovie(prod_company);



