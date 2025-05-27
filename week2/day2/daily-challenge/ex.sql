CREATE TABLE FirstTab (
     id INTEGER, 
     name VARCHAR(10)
);

INSERT INTO FirstTab VALUES
(5, 'Pawan'),
(6, 'Sharlee'),
(7, 'Krish'),
(NULL, 'Avtaar');


CREATE TABLE SecondTab (
    id INTEGER
);

INSERT INTO SecondTab VALUES
(5),
(NULL);


SELECT COUNT(*) AS Q1_Output
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL );



SELECT COUNT(*) AS Q2_Output
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 );


SELECT COUNT(*) AS Q3_Output
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab );

SELECT COUNT(*) AS Q4_Output
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL );

--Query	Expected Output
--Q1	0
--Q2	2
--Q3	0
--Q4	2