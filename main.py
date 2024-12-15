from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, PositiveInt, AnyHttpUrl, Field, field_validator
import uvicorn
from app.get_score import Number, Score
from app.schemas import Attack

app = FastAPI() # Creating FastAPI instance

website = Jinja2Templates(directory="templates")

class AttackRequest(BaseModel):
    '''Pydantic model for attack request data'''
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

    @field_validator('num_chars')
    def validate_num_chars(cls, value):
        '''
        Validating num_chars as a positive int or float
        If float equivalent to int, convert to int
        '''
        if (
            not isinstance(value, (int, float))
            or value <= 0
            or (value % 1 != 0)
        ):
            raise ValueError(
                "Please use whole numbers for the character count. " +
                "The character count must be greater than 0."
                )
        # if Positive Whole Number, convert into an int
        value = int(value)
        return value

class AttackScore(BaseModel):
    '''Pydantic model for score calculation'''
    score: Number = Field(description="Attack's score")

class ErrorResponse(BaseModel):
    '''Pydantic model for error messages'''
    error: str = Field(description="Error message")

@app.get("/")
async def read_root(request : Request):
    '''Load index.html template'''
    return website.TemplateResponse("index.html", {"request" : request})

@app.post("/score", response_model=AttackScore, responses={400: {"model": ErrorResponse}})
async def calculate_score(form_input: AttackRequest):
    '''Gets score for form inputs'''
    try:
        # Calculate score
        score = Score(
            form_input.finish,
            form_input.color,
            form_input.shading,
            form_input.bg,
            form_input.size,
            form_input.num_chars
            ).calculate()
        '''
        # Create attack to store in database
        attack = Attack(
            form_input.sender,
            form_input.recipient,
            form_input.team,
            form_input.link,
            Score.finish,
            Score.color,
            Score.shading,
            Score.bg,
            Score.size,
            Score.num_chars,
            score
        )
        '''
        # Return calculated score to index.html
        return AttackScore(score=score)
    except Exception as e:
        # Raise error
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)