create table items(
	id_item serial primary key,
	type_item varchar (50) not null,
	prix smallint not null
);
create table customers(
	id_customer serial primary key,
	first_name varchar (50) not null,
	last_name varchar (50) not null
);
insert into items(type_item, prix)
values 
	('Small Desk', 100),
	('Large Desk', 300),
	('fan', 80);

insert into customers(first_name, last_name)
values
	('Greg', 'Jones'),
	('Sandra', 'Jones'),
	('Scott', 'Scott'),
	('Trevor', 'Green'),
	('Melanie', 'Johnson');

select * from items;
select * from items
where prix<80;
select * from items
where prix<=300;
select * from customers
where last_name = 'Smith';
select * from customers
where last_name = 'Jones';
select * from customers
where first_name!= 'Scott';