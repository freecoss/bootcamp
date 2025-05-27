SELECT * FROM language;

SELECT f.title, f.description, l.name AS language
FROM film f
JOIN language l ON f.language_id = l.language_id;

SELECT f.title, f.description, l.name AS language
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name)
VALUES ('The Lost Island'), ('Sky Empire'), ('Robot Wars');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255),
    score INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
((SELECT id FROM new_film WHERE name = 'The Lost Island'), 1, 'Epic Adventure', 9, 'An amazing journey with stunning visuals.'),
((SELECT id FROM new_film WHERE name = 'Sky Empire'), 2, 'Sky-High Fun', 8, 'Great story and characters.');

DELETE FROM new_film WHERE name = 'Sky Empire';

SELECT * FROM customer_review;