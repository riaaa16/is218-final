'''Tests app.models by creating an attack in the database'''
from app.models import Attack

def test_create_attack(db_session):
    '''Creating an attack in the database'''
    attack = Attack(
        sender = "Mary",
        recipient = "Sue",
        team = "Cat",
        link = "https://www.youtube.com/",
        finish = 10,
        color = 10,
        shading = 10,
        bg = 10,
        size = 10,
        num_chars = 2,
        score = 800
    )

    db_session.add(attack)
    db_session.commit()
    db_session.refresh(attack)

    # Assert that the instance was added correctly
    assert attack.id is not None  # Check that the ID has been assigned
    assert attack.sender == "Mary"
    assert attack.recipient == "Sue"
    assert attack.team == "Cat"
    assert attack.link == "https://www.youtube.com/"
    assert attack.finish == 10
    assert attack.color == 10
    assert attack.shading == 10
    assert attack.bg == 10
    assert attack.size == 10
    assert attack.num_chars == 2
    assert attack.score == 800

    # Expected string representation
    expected_repr = (
        "sender = Mary\n"
        "recipient = Sue\n"
        "team = Cat\n"
        "link = https://www.youtube.com/\n"
        "finish = 10.0\n"
        "color = 10.0\n"
        "shading = 10.0\n"
        "bg = 10.0\n"
        "size = 10.0\n"
        "num_chars = 2\n"
        "score = 800.0"
    )

    # Assert that repr(attack) matches the expected string
    assert repr(attack) == expected_repr
