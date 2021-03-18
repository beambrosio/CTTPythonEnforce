CREATE DATABASE 'Imobiliaria'

CREATE TABLE Proprietarios (
	id_prop SERIAL PRIMARY KEY,
	nome_prop VARCHAR(255) NOT NULL,
    data_nasc_prop DATE NOT NULL,
    cpf_prop VARCHAR (50) UNIQUE NOT NULL,
    rg_prop INTEGER UNIQUE NOT NULL,
    est_civil_prop VARCHAR (100) NOT NULL, 
	tel_prop VARCHAR (11) NOT NULL,
	formacao VARCHAR (50) NOT NULL,
    temp_imovel VARCHAR (100) NOT NULL

);

CREATE TABLE Gastos (
    id_gastos SERIAL PRIMARY KEY,
    luz VARCHAR (10),
    agua VARCHAR (10),
    condominio VARCHAR (10)

);


CREATE TABLE Imoveis (
	id_imovel SERIAL PRIMARY KEY,
	rua VARCHAR(100) NOT NULL,
    num VARCHAR (10) NOT NULL,
    andar VARCHAR (10),
    bloco VARCHAR (10),
    cidade VARCHAR (150) NOT NULL, 
	cep VARCHAR (10) NOT NULL,
	estado VARCHAR (50) NOT NULL,
    preco_imo VARCHAR (100) NOT NULL,
    obs VARCHAR (500), 


    id_prop INT NOT NULL, 
    FOREIGN KEY (id_prop)
	    REFERENCES Proprietarios(id_prop)
		ON UPDATE CASCADE ON DELETE CASCADE, 

    id_gastos INT,
    FOREIGN KEY (id_gastos)
        REFERENCES Gastos(id_gastos)
        ON UPDATE CASCADE ON DELETE CASCADE

);

CREATE TABLE Clientes(
    id_cliente SERIAL PRIMARY KEY,
	nome_cliente VARCHAR(255) NOT NULL,
    data_nasc_cliente DATE NOT NULL,
    cpf_cliente VARCHAR (50) UNIQUE NOT NULL,
    rg_cliente INTEGER UNIQUE NOT NULL,
    est_civil_cliente VARCHAR (100) NOT NULL, 
	tel_cliente VARCHAR (11) NOT NULL,
	formacao_cliente VARCHAR (50) NOT NULL,
    rua VARCHAR(100) NOT NULL,
    num VARCHAR (10) NOT NULL,
    andar VARCHAR (10),
    bloco VARCHAR (10),
    cidade VARCHAR (150) NOT NULL, 
	cep VARCHAR (10) NOT NULL,
	estado VARCHAR (50) NOT NULL

);

CREATE TABLE Compras(
    id_compra SERIAL PRIMARY KEY,
    tipo_compra VARCHAR(100),
    banco_finan VARCHAR (10),
    preco VARCHAR (10),

    id_cliente INT NOT NULL, 
    FOREIGN KEY(id_cliente)
        REFERENCES Clientes(id_cliente)
        ON UPDATE CASCADE ON DELETE CASCADE,

    id_imovel INT NOT NULL,
    FOREIGN KEY (id_imovel)
        REFERENCES Imoveis(id_imovel)
        ON UPDATE CASCADE ON DELETE CASCADE
);

