CREATE TABLE IF NOT EXISTS pereval_images (  
    id SERIAL PRIMARY KEY, -- Уникальный идентификатор изображения  
    pereval_id INT REFERENCES pereval_added(id) ON DELETE CASCADE, -- Связь с таблицей перевалов  
    image_url VARCHAR(255) NOT NULL, -- URL изображения  
    description TEXT -- Описание изображения  
);