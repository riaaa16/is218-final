'''
Testing FastAPI post method '/score' defined in main.py
'''

def test_attack(client):
    response = client.post('/score', json={
                    'sender': "John",
                    'recipient': "Doe",
                    'team': "Cat",
                    'link': "https://www.youtube.com",
                    'finish': 10,
                    'color': 10,
                    'shading': 10,
                    'bg': 10,
                    'size': 1,
                    'num_chars': 1
                })
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

    assert response.json()['score'] == 40, f"Expected score 40, got {response.json()['score']}"