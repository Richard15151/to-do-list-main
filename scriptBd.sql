DROP DATABASE IF EXISTS todolist;

CREATE DATABASE todolist;

USE todolist;

CREATE TABLE tarefas(
    id_tarefa INT PRIMARY KEY AUTO_INCREMENT,
    descricao TEXT NOT NULL,
    data DATE NOT NULL,
    status ENUM('Pendente', 'Concluída') DEFAULT 'Pendente'
);