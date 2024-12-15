'''Validates input for database'''
from pydantic import BaseModel, PositiveInt, AnyHttpUrl, Field
from app.get_score import Number

class Attack(BaseModel):
    '''
    Validates params that will be used to store each attack
    in the database.
    '''

    sender: str = Field(description="Sender's name")
    recipient: str = Field(description="Recipient's name")
    team: str = Field(description="Sender's team")
    link: AnyHttpUrl = Field(description="Attack's link")
    finish: Number = Field(description="Attack's finish")
    color: Number = Field(description="Attack's color")
    shading: Number = Field(description="Attack's shading")
    bg: Number = Field(description="Attack's background")
    size: Number = Field(description="Attack'size")
    num_chars: PositiveInt = Field(description="Attack's character count")
    score: Number = Field(description="Attack's score")