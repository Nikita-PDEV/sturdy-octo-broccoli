import psycopg2  
from psycopg2 import sql  
from .config import DATABASE_CONFIG  

class Database:  
    def __init__(self):  
        try:  
            self.connection = psycopg2.connect(**DATABASE_CONFIG)  
            self.cursor = self.connection.cursor()  
        except psycopg2.Error as e:  
            print(f"Ошибка при подключении к базе данных: {e}")  
            raise  

    def add_pereval(self, beautyTitle, title, other_titles, connect, coord_id,  
                    level_winter, level_spring, level_summer, level_autumn):  
        query = sql.SQL("""  
            INSERT INTO pereval_added (beautyTitle, title, other_titles, connect, coord_id, status, level_winter, level_spring, level_summer, level_autumn)  
            VALUES (%s, %s, %s, %s, %s, 'new', %s, %s, %s, %s)  
            RETURNING id;  -- Получаем ID вставленной записи  
        """)  
        try:  
            self.cursor.execute(query, (beautyTitle, title, other_titles, connect, coord_id,  
                                        level_winter, level_spring, level_summer, level_autumn))  
            self.connection.commit()  
            return self.cursor.fetchone()[0]  # Возвращает id вставленной записи  
        except psycopg2.Error as e:  
            print(f"Ошибка при добавлении записи: {e}")  
            self.connection.rollback()  # Откатить изменения в случае ошибки  

    def close(self):  
        if self.cursor:  
            self.cursor.close()  
        if self.connection:  
            self.connection.close()  

# Пример использования  
if __name__ == "__main__":  
    db = Database()  
    try:  
        new_id = db.add_pereval("Пример Красоты", "Пример Заголовка", "Другие Заголовки", "Соединение",   
                                12345, 1, 2, 3, 4)  
        print(f"Запись добавлена с ID: {new_id}")  
    except Exception as e:  
        print(f"Произошла ошибка: {e}")  
    finally:  
        db.close()