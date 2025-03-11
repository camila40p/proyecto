CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_personas;

CREATE TABLE `db_personas`.`estados` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);

INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Casad@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Solter@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Vioud@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Separados@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Lo que importa es que Diosito me quiere');