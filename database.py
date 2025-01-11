from typing import Annotated
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine
from config import settings

sync_engine = create_engine(
    url=settings.DATABES_URL_psycopg,
    echo=False,
    pool_size=3,
    max_overflow=2
)

session_factory = sessionmaker(sync_engine)

str_100 = Annotated[str, 100]
str_320 = Annotated[str, 320]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_100: String(100),
        str_320: String(320)
    }
