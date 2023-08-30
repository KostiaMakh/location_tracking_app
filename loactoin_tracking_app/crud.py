from sqlalchemy.orm import Session

from loactoin_tracking_app import models


def get_mql_prospects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MQLProspects).offset(skip).limit(limit).all()
