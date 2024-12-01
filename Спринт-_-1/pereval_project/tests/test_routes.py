import pytest  
from fastapi.testclient import TestClient  
from app.main import app  

client = TestClient(app)  

def test_submit_data():  
    response = client.post("/submitData/", json={  
        "beautyTitle": "Красивый перевал",  
        "title": "Перевал Гладкий",  
        "other_titles": ["Гладкий перевал"],  
        "connect": "Скалы на южном склоне",  
        "coord_id": 1,  
        "level_winter": "Трудный",  
        "level_spring": "Средний",  
        "level_summer": "Легкий",  
        "level_autumn": "Трудный"  
    })  
    assert response.status_code == 200  
    assert response.json() == {"message": "Pereval added successfully", "status": "new"}  

def test_submit_data_with_invalid_json():  
    response = client.post("/submitData/", json={})  
    assert response.status_code == 422  # Ошибка валидации