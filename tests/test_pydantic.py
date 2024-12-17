'''Testing app.schemas Pydantic validation'''
from app.schemas import Attack

def test_pydantic_schema():
    '''Creating an attack with Pydantic model'''
    attack = Attack(
        sender="John",
        recipient="Doe",
        team="Red",
        link="https://example.com",
        finish=10,
        color=5.5,
        shading=8,
        bg=3.3,
        size=12,
        num_chars=20,
        score=95.5
    )

    assert attack.sender == "John"
    assert attack.recipient == "Doe"
    assert attack.team == "Red"
    assert str(attack.link) == "https://example.com/"
    assert attack.finish == 10
    assert attack.color == 5.5
    assert attack.shading == 8
    assert attack.bg == 3.3
    assert attack.size == 12
    assert attack.num_chars == 20
    assert attack.score == 95.5
