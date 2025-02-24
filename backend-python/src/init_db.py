from .database import SessionLocal, engine
from . import models

# Create tables
models.Base.metadata.create_all(bind=engine)

# Initial quotes
initial_quotes = [
    {
        "text": "Be the change you wish to see in the world.",
        "author": "Mahatma Gandhi"
    },
    {
        "text": "I have not failed. I've just found 10,000 ways that won't work.",
        "author": "Thomas A. Edison"
    },
    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs"
    },
    {
        "text": "In three words I can sum up everything I've learned about life: it goes on.",
        "author": "Robert Frost"
    }
]

def init_db():
    db = SessionLocal()
    try:
        # Check if we already have quotes
        existing_quotes = db.query(models.Quote).first()
        if not existing_quotes:
            for quote_data in initial_quotes:
                quote = models.Quote(**quote_data)
                db.add(quote)
            db.commit()
            print("Database initialized with sample quotes!")
        else:
            print("Database already contains quotes, skipping initialization.")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
