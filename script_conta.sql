create database banco_digital;


use banco_digital;


create table if not exists contas(
	id int primary key auto_increment, 
	saldo float not null default 0.00,
	numero int not null,
	banco varchar(50) not null,
	agencia int not null,
	tipo_conta int check (tipo_conta in (1, 2)),
	cpf varchar(11) not null,
	rendimento float,
	limite float
);
