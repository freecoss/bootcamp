CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

--afficher le tableau
SELECT * FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

-- adding two female actors
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Meryl', 'Streep', '1949-06-22', 3);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Viola', 'Davis', '1965-08-11', 1);

--adding 3 actors at one query
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES 
    ('Emma', 'Stone', '1988-11-06', 1),
    ('Leonardo', 'DiCaprio', '1974-11-11', 1),
    ('Zendaya', 'Coleman', '1996-09-01', 0);

--afficher le tableau
SELECT * FROM actors;

--Update the first name of Matt Damon to Maty
update actors set first_name='Maty' where first_name='Matt';

--Update the number of oscars of George Clooney to 4, and return the updated record
update actors set number_oscars=4 where first_name='George' and last_name='Clooney' returning first_name, last_name, age, number_oscars;

--Rename the age column by birthdate
alter table actors rename column age to birthdate;

--Delete one actor and return it
delete from actors where first_name in (select first_name from actors limit 1) returning first_name, last_name, birthdate, number_oscars;

select count(*) from actors;
-- impossible d'inserer un field vide car les field ont not null
-- INSERT INTO actors (first_name, last_name)
-- VALUES('Matt','Damon');










