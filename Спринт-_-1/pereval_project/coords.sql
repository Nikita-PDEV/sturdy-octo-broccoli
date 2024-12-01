CREATE TABLE IF NOT EXISTS coords (  
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор координат  
    latitude FLOAT NOT NULL, -- Широта  
    longitude FLOAT NOT NULL -- Долгота  
);