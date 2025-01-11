import datetime
from sqlalchemy import Boolean, Table, Column, Float, String, Date, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_100, str_320

# for using in ORM mod

class InternsOrm(Base):
    __tablename__ = "interns"
    __table_args__ = {"schema": "cloveri"}
    id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str_320]
    username: Mapped[str_100]
    user_role: Mapped[str_100]
    internship: Mapped[str_100]
    start_date: Mapped[datetime.datetime]
    end_date: Mapped[datetime.datetime]
    notes: Mapped[str | None]

    #grades: Mapped[list["GradesOrm"]] = relationship()

class GradesOrm(Base):
    __tablename__ = "grades"
    __table_args__ = {"schema": "cloveri"}
    intern_id: Mapped[str] = mapped_column(ForeignKey(InternsOrm.id, ondelete="CASCADE"))
    id: Mapped[str] = mapped_column(primary_key=True)
    ai: Mapped[float | None]
    programming: Mapped[float | None]
    architecture: Mapped[float | None]
    project_management: Mapped[float | None]
    communication: Mapped[float | None]
    personnel_management: Mapped[float | None]
    information_management: Mapped[float | None]
    infrastructure: Mapped[float | None]
    data_management: Mapped[float | None]
    math: Mapped[float | None]
    data_analysis: Mapped[float | None]
    visual: Mapped[float | None]
    ux_ui: Mapped[float | None]
    seo: Mapped[float | None]
    typografy: Mapped[float | None]
    skill18: Mapped[float | None]
    skill19: Mapped[float | None]
    skill20: Mapped[float | None]

    #username: Mapped["InternsOrm"] = relationship()

class ToolsOrm(Base):
    __tablename__ = "tools"
    __table_args__ = {"schema": "cloveri"}
    #skills_role: Mapped[str_100] = mapped_column(ForeignKey(InternsOrm.role, ondelete="CASCADE"))
    #skills_internship: Mapped[str_100] = mapped_column(ForeignKey(InternsOrm.internship, ondelete="CASCADE"))
    id: Mapped[str] = mapped_column(primary_key=True)
    user_role: Mapped[str_100]
    internship: Mapped[str_100]
    pycaret: Mapped[bool | None]
    random_forest: Mapped[bool | None]
    anomaly_detection: Mapped[bool | None]
    gradient_boosting: Mapped[bool | None]
    cluster_analysis: Mapped[bool | None]
    k_fold: Mapped[bool | None]
    optuna: Mapped[bool | None]
    shap: Mapped[bool | None]
    tsfresh: Mapped[bool | None]
    sklearn_feature_selection: Mapped[bool | None]
    imblearn: Mapped[bool | None]
    streamlit: Mapped[bool | None]
    selenium: Mapped[bool | None]
    allure: Mapped[bool | None]
    nose: Mapped[bool | None]
    simpletest: Mapped[bool | None]
    docker: Mapped[bool | None]
    jira: Mapped[bool | None]
    adobe_xd: Mapped[bool | None]
    figma : Mapped[bool | None]
    mockplus: Mapped[bool | None]
    yandex_metrika: Mapped[bool | None]
    google_analytics: Mapped[bool | None]
    sketch: Mapped[bool | None]
    fontjoy: Mapped[bool | None]
    sqlalchemy: Mapped[bool | None]
    postgresql: Mapped[bool | None]
    git: Mapped[bool | None]
    docker: Mapped[bool | None]
    django: Mapped[bool | None]
  

# for using in core mod

metadata_obj = MetaData()

interns_table = Table(
    "interns",
    metadata_obj,
    Column("id", String, primary_key=True),
    Column("email", String),
    Column("username", String),
    Column("user_role", String),
    Column("internship", String),
    Column("start_date", Date), 
    Column("end_date", Date),
    Column("notes", String),
    schema="cloveri"    
)

grades_table = Table(
    "grades",
    metadata_obj,
    Column("id", String, primary_key=True),
    Column("ai", Float),
    Column("programming", Float),
    Column("architecture", Float),
    Column("project_management", Float),
    Column("communication", Float),
    Column("personnel_management", Float),
    Column("information_management", Float),
    Column("infrastructure", Float),
    Column("data_management", Float),
    Column("visual", Float),
    Column("ux_ui", Float),
    Column("seo", Float),
    Column("typografy", Float),
    Column("skill18", Float),
    Column("skill19", Float),
    Column("skill20", Float),
    schema="cloveri"    
)

tools_table = Table(
    "tools",
    metadata_obj,
    Column("user_role", String, primary_key=True),
    Column("internship", String),
    Column("pycaret", Boolean),
    Column("random_forest", Boolean),
    Column("anomaly_detеction", Boolean),
    Column("gradient_boosting", Boolean),
    Column("cluster_analysis", Boolean),
    Column("k_fold", Boolean),
    Column("optuna", Boolean),
    Column("shap", Boolean),
    Column("tsfresh", Boolean),
    Column("sklearn_feature_selection", Boolean),
    Column("imblearn", Boolean),
    Column("streamlit", Boolean),
    Column("tool13", Boolean),
    Column("skill19", Boolean),
    Column("skill20", Boolean),
    Column("skill21", Boolean),
    Column("skill22", Boolean),
    Column("skill23", Boolean),
    Column("skill24", Boolean),
    Column("skill25", Boolean),
    Column("skill26", Boolean),
    Column("skill27", Boolean),
    Column("skill28", Boolean),
    Column("skill29", Boolean),
    Column("skill30", Boolean),
    schema="cloveri"    
)