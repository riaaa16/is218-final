import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, PositiveInt, AnyHttpUrl, Field, field_validator
import uvicorn
from app.get_score import Number, Score
from app.models import Attack, Base

app = FastAPI() # Creating FastAPI instance

website = Jinja2Templates(directory="templates")

# Load the DATABASE_URL directly from the environment
# DATABSE_URL is created in docker-compose.yml
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the database engine using the DATABASE_URL
engine = create_engine(DATABASE_URL)

# Create tables in the database if they do not exist
Base.metadata.create_all(bind=engine)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to the endpoint function
    finally:
        db.close()  # Ensure the session is closed after the request

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
async def calculate_score(form_input: AttackRequest, db = Depends(get_db)):
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
        

        # Create attack to store in database
        attack = Attack(
            sender=form_input.sender,
            recipient=form_input.recipient,
            team=form_input.team,
            link=str(form_input.link),
            finish=form_input.finish,
            color=form_input.color,
            shading=form_input.shading,
            bg=form_input.bg,
            size=form_input.size,
            num_chars=form_input.num_chars,
            score=score
        )
        
        db.add(attack)
        db.commit()
        db.refresh(attack)

        # Return calculated score to index.html
        return AttackScore(score=score)
    except Exception as e:
        # Raise error
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)