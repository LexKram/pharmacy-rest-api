from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
import time

from app import database, models, schemas, crud

app = FastAPI(
    title="Pharmacy REST API",
    description="CRUD API для управления лекарствами",
    version="1.0.0"
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    retries = 10
    delay = 2

    for i in range(retries):
        try:
            models.Base.metadata.create_all(bind=database.engine)
            print("Database connected and tables created")
            break
        except OperationalError:
            print(f"Database not ready, retry {i + 1}/{retries}")
            time.sleep(delay)
    else:
        raise RuntimeError("Database is not available")

@app.get("/medicines", response_model=list[schemas.MedicineResponse])
def get_medicines(db: Session = Depends(get_db)):
    return crud.get_all_medicines(db)

@app.get("/medicines/{medicine_id}", response_model=schemas.MedicineResponse)
def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = crud.get_medicine_by_id(db, medicine_id)
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine

@app.post("/medicines", response_model=schemas.MedicineResponse, status_code=201)
def create_medicine(medicine: schemas.MedicineCreate, db: Session = Depends(get_db)):
    return crud.create_medicine(db, medicine)

@app.put("/medicines/{medicine_id}", response_model=schemas.MedicineResponse)
def update_medicine_put(medicine_id: int, medicine: schemas.MedicineCreate, db: Session = Depends(get_db)):
    updated = crud.update_medicine_put(db, medicine_id, medicine)
    if not updated:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return updated

@app.patch("/medicines/{medicine_id}", response_model=schemas.MedicineResponse)
def update_medicine_patch(medicine_id: int, medicine: schemas.MedicineUpdate, db: Session = Depends(get_db)):
    updated = crud.update_medicine_patch(db, medicine_id, medicine)
    if not updated:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return updated

@app.delete("/medicines/{medicine_id}", status_code=204)
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_medicine(db, medicine_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Medicine not found")
