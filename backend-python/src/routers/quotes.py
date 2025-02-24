from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import random
from ..database import get_db
from .. import models
from .. import schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.Quote])
def get_all_quotes(db: Session = Depends(get_db)):
    quotes = db.query(models.Quote).all()
    return quotes

@router.get("/random", response_model=schemas.Quote)
def get_random_quote(db: Session = Depends(get_db)):
    quotes = db.query(models.Quote).all()
    if not quotes:
        raise HTTPException(status_code=404, detail="No quotes found")
    return random.choice(quotes)

@router.post("/", response_model=schemas.Quote, status_code=201)
def create_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote

@router.put("/{quote_id}", response_model=schemas.Quote)
def update_quote(quote_id: int, quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    if not db_quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    
    for key, value in quote.dict().items():
        setattr(db_quote, key, value)
    
    db.commit()
    db.refresh(db_quote)
    return db_quote

@router.delete("/{quote_id}")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    db_quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    if not db_quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    
    db.delete(db_quote)
    db.commit()
    return {"message": "Quote deleted successfully"}
