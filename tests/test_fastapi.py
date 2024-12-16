'''
Testing FastAPI post method '/score' defined in main.py with a mocked version.
'''
from fastapi.testclient import TestClient
from main import app

def test_calculate_score_with_mock_db(mock_get_db):
    '''
    Testing sending input to 'score method
    in main.py
    '''
    attack_data = {
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
    }

    # Send a POST request to the /score endpoint
    client = TestClient(app)
    response = client.post("/score", json=attack_data)

    # Assert the response status code and the returned score
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['score'] == 40, f"Expected score 40, got {response.json()['score']}"

    # Assert that the mock session methods were called (simulating DB interaction)
    mock_get_db.add.assert_called_once()  # Ensure add was called once
    mock_get_db.commit.assert_called_once()  # Ensure commit was called once
    mock_get_db.refresh.assert_called_once()  # Ensure refresh was called once

    # Optionally, check the Attack instance that would have been created in the DB
    attack_instance = mock_get_db.add.call_args[0][0]  # The first argument passed to add()
    assert attack_instance.sender == "John"
    assert attack_instance.recipient == "Doe"
    assert attack_instance.score == 40  # Ensure the score calculated is correct
