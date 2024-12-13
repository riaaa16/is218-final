'''Validates input for database'''
from pydantic import BaseModel, PositiveInt, AnyHttpUrl
from app.get_score import Number

class Attack(BaseModel):
    '''
    Validates params that will be used to store each attack
    in the database.
    '''

    sender: str             # should be a string
    recipient: str          # should be a string
    team: str               # should be a string
    link: AnyHttpUrl        # should be https | https, TLD not required, host required
    finish: Number          # should be a int | float
    color: Number           # should be a int | float
    shading: Number         # should be a int | float
    bg: Number              # should be a int | float
    size: Number            # should be a int | float
    num_chars: PositiveInt  # should be a positive integer
    result: Number          # should be a int | float
