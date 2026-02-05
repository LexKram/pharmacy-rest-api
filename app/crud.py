from sqlalchemy.orm import Session
from app import models, schemas

def get_all_medicines(db: Session):
    return db.query(models.Medicine).all()

def get_medicine_by_id(db: Session, medicine_id: int):
    return db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()

def create_medicine(db: Session, medicine: schemas.MedicineCreate):
    db_medicine = models.Medicine(**medicine.dict())
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine

def update_medicine_put(db: Session, medicine_id: int, medicine: schemas.MedicineCreate):
    db_medicine = get_medicine_by_id(db, medicine_id)
    if not db_medicine:
        return None

    for field, value in medicine.dict().items():
        setattr(db_medicine, field, value)

    db.commit()
    db.refresh(db_medicine)
    return db_medicine

def update_medicine_patch(db: Session, medicine_id: int, medicine: schemas.MedicineUpdate):
    db_medicine = get_medicine_by_id(db, medicine_id)
    if not db_medicine:
        return None

    for field, value in medicine.dict(exclude_unset=True).items():
        setattr(db_medicine, field, value)

    db.commit()
    db.refresh(db_medicine)
    return db_medicine

def delete_medicine(db: Session, medicine_id: int):
    db_medicine = get_medicine_by_id(db, medicine_id)
    if not db_medicine:
        return False

    db.delete(db_medicine)
    db.commit()
    return True
