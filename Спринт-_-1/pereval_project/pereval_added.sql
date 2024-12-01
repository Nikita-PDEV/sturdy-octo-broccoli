CREATE TABLE IF NOT EXISTS pereval_added (  
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор перевала  
    beautyTitle VARCHAR(255) NOT NULL, -- Красивое название перевала  
    title VARCHAR(255) NOT NULL, -- Обычное название перевала  
    other_titles TEXT[], -- Другие названия (массив текстов)  
    connect TEXT, -- Подробности о соединениях  
    coord_id INT, -- Идентификатор координат  
    status VARCHAR(50) NOT NULL DEFAULT 'new', -- Статус перевала  
    level_winter VARCHAR(50), -- Уровень сложности зимой  
    level_spring VARCHAR(50), -- Уровень сложности весной  
    level_summer VARCHAR(50), -- Уровень сложности летом  
    level_autumn VARCHAR(50) -- Уровень сложности осенью  
);