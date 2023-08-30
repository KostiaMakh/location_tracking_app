from sqlalchemy.orm import Session
from fastapi import (
    FastAPI,
    Depends,
)
from loactoin_tracking_app import (
    schemas,
    crud,
)
from loactoin_tracking_app.database import (
    get_session,
    init_db,
)

app = FastAPI()
init_db()


# MQLProspects
@app.get("/mql-prospects/", response_model=list[schemas.MQLProspects])
def read_mql_prospects(skip: int = 0, limit: int = 100, db: Session = Depends(get_session)):
    mqls = crud.get_mql_prospects(db, skip=skip, limit=limit)
    return mqls
