INSERT INTO dojos(id, name, created_at, updated_at)
VALUES	(1,' San Jose', sysdate(),sysdate()),
		(2, 'Alajuela', sysdate(),sysdate()),
        (3, 'Cartago', sysdate(),sysdate());

DELETE FROM dojos
WHERE id < 4;

INSERT INTO dojos(id, name, created_at, updated_at)
VALUES	(1, 'Limon', sysdate(),sysdate()),
		(2, 'Heredia', sysdate(),sysdate()),
        (3, 'Guanacaste', sysdate(),sysdate());

INSERT INTO ninjas(id,first_name,last_name,age,dojo_id,created_at,updated_at)
VALUES 	(1, 'Max', 'Rodriguez', 25, 1, sysdate(),sysdate()),
		(2, 'Javier', 'Baimason', 33, 1, sysdate(),sysdate()),
		(3, 'Valeria', 'Romero', 29, 1, sysdate(),sysdate()),
        (4, 'Johandro', 'Gonzalez', 21, 2, sysdate(),sysdate()),
		(5, 'Bryan', 'Cascante', 18, 2, sysdate(),sysdate()),
		(6, 'Jorge', 'Chavez', 25, 2, sysdate(),sysdate()),
        (7, 'Nikole', 'Porras', 26, 3, sysdate(),sysdate()),
		(8, 'Geraldine', 'Cachay', 35, 3, sysdate(),sysdate()),
		(9, 'Yorleny', 'Miranda', 22, 3, sysdate(),sysdate());


/*First attemp before consulting the answer*/
SELECT *
FROM ninjas
WHERE dojo_id =1;

/*Updated attemp after reviewing the answer*/
SELECT *
FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojo_id = 1;


/*First attemp before consulting the answer*/
SELECT *
FROM ninjas
WHERE dojo_id = 3;

/*Updated attemp after reviewing the answer*/
SELECT *
FROM ninjas
WHERE dojo_id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);


/*First attemp before consulting the answer*/
SELECT dojo_id
FROM ninjas
WHERE id = 9;

/*Updated attemp after reviewing the answer*/
SELECT *
FROM dojos
WHERE id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);
