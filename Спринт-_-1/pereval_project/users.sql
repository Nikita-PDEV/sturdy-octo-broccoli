CREATE TABLE IF NOT EXISTS users (  
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор пользователя  
    username VARCHAR(50) UNIQUE NOT NULL, -- Имя пользователя  
    password_hash VARCHAR(255) NOT NULL, -- Хэш пароля  
    email VARCHAR(100) UNIQUE NOT NULL -- Электронная почта  
);