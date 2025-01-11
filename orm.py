from sqlalchemy import select
from database import sync_engine, session_factory, Base
from models import InternsOrm, GradesOrm, ToolsOrm


class SyncOrm:

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_interns():
        intern_1 = InternsOrm(id='f1',
                              email='work.aubakirov@gmail.com', 
                              username='Miguel Aubakirov',
                              user_role='Python-программист',
                              internship='Кабинет Кловери',
                              start_date='2025-01-15',
                              end_date='2025-04-28')
        intern_2 = InternsOrm(id='f2',
                              email='work.aubakirov@gmail.com', 
                              username='Miguel Aubakirov',
                              user_role='Python-программист',
                              internship='MAIBO',
                              start_date='2025-01-15',
                              end_date='2025-04-28')
        intern_3 = InternsOrm(id='f3',
                              email='sample@gmail.com', 
                              username='Nombre Apellido',
                              user_role='Python-программист',
                              internship='Кабинет Кловери',
                              start_date='2025-01-15',
                              end_date='2025-04-28')
        intern_4 = InternsOrm(id='f4',
                              email='sample1@gmail.com', 
                              username='Jose Rodrigues',
                              user_role='QA-инженер',
                              internship='MAIBO',
                              start_date='2025-01-15',
                              end_date='2025-04-28')
        intern_5 = InternsOrm(id='f5',
                              email='sample2@gmail.com', 
                              username='Soledad Lorna',
                              user_role='UX/UI-дизайнер',
                              internship='Платформа для ВУЗов',
                              start_date='2025-01-15',
                              end_date='2025-02-28')
        with session_factory() as session:
            session.add_all([intern_1, intern_2, intern_3, intern_4, intern_5,])
            session.commit()

    @staticmethod
    def insert_grades():
        intern_1 = GradesOrm(id="g1",
                            intern_id='f1',
                            ai=4.4,
                            programming=4.2,
                            architecture=3.4,
                            project_management=4.0,
                            communication=5.4,
                            personnel_management=3.4,
                            information_management=5.4,
                            infrastructure=4.7,
                            data_management=3.4,
                            math=5.8,
                            data_analysis=4.0
                            )
        intern_2 = GradesOrm(id="g2",
                            intern_id='f2',
                            ai=3.4,
                            programming=4.0,
                            architecture=3.7,
                            project_management=4.1,
                            communication=5.8,
                            personnel_management=4.0,
                            information_management=4.7,
                            infrastructure=3.9,
                            data_management=4.4,
                            math=5.2,
                            data_analysis=4.6
                            )
        intern_3 = GradesOrm(id="g3",
                            intern_id='f3',
                            ai=5.4,
                            programming=4.3,
                            architecture=3.7,
                            project_management=4.1,
                            communication=5.2,
                            personnel_management=4.2,
                            information_management=5.7,
                            infrastructure=4.0,
                            data_management=4.2,
                            math=3.2,
                            data_analysis=3.6
                            )
        intern_4 = GradesOrm(id="g4",
                            intern_id='f4',
                            ai=5.4,
                            programming=4.3,
                            architecture=3.8,
                            project_management=4.2,
                            communication=5.2,
                            personnel_management=4.3,
                            information_management=5.7,
                            infrastructure=4.0,
                            data_management=5.2,
                            math=3.9,
                            data_analysis=4.6
                            )
        intern_5 = GradesOrm(id="g5",
                            intern_id='f5',
                            ai=5.9,
                            programming=3.3,
                            project_management=4.8,
                            communication=5.5,
                            personnel_management=5.0,
                            information_management=3.7,
                            infrastructure=4.3,
                            visual=5.8,
                            ux_ui=5.9,
                            seo=4.4,
                            typografy=4.5
                            )
        with session_factory() as session:
            session.add_all([intern_1, intern_2, intern_3, intern_4, intern_5,])
            session.commit()

    @staticmethod
    def insert_tools():
        row_1 = ToolsOrm(id="t1",
                            user_role='Python-программист',
                            internship='Кабинет Кловери',
                            git=True,
                            postgresql=True,
                            sqlalchemy=True,
                            docker=True,
                            django=True,
                            pycaret=True,
                            jira=True,
                            optuna=True
                            )
        row_2 = ToolsOrm(id="t2",
                            user_role='Python-программист',
                            internship='MAIBO',
                            git=True,
                            postgresql=True,
                            sqlalchemy=True,
                            docker=True,
                            django=True,
                            pycaret=True,
                            jira=True,
                            optuna=True
                            )
        row_3 = ToolsOrm(id="t3",
                            user_role='Python-программист',
                            internship='Платформа для ВУЗов',
                            git=True,
                            postgresql=True,
                            sqlalchemy=True,
                            docker=True,
                            django=True,
                            pycaret=True,
                            jira=True,
                            optuna=True
                            )
        row_4 = ToolsOrm(id="t4",
                            user_role='QA-инженер',
                            internship='Кабинет Кловери',
                            git=True,
                            jira=True,
                            docker=True,
                            simpletest=True,
                            nose=True,
                            allure=True,
                            selenium=True
                            )
        row_5 = ToolsOrm(id="t5",
                            user_role='QA-инженер',
                            internship='MAIBO',
                            git=True,
                            jira=True,
                            docker=True,
                            simpletest=True,
                            nose=True,
                            allure=True,
                            selenium=True
                            )
        row_6 = ToolsOrm(id="t6",
                            user_role='QA-инженер',
                            internship='Платформа для ВУЗов',
                            git=True,
                            jira=True,
                            docker=True,
                            simpletest=True,
                            nose=True,
                            allure=True,
                            selenium=True
                            )
        row_7 = ToolsOrm(id="t7",
                            user_role='UX/UI-дизайнер',
                            internship='Кабинет Кловери',
                            jira=True,
                            adobe_xd=True,
                            figma=True,
                            mockplus=True,
                            yandex_metrika=True,
                            google_analytics=True,
                            sketch=True,
                            fontjoy=True
                            )
        row_8 = ToolsOrm(id="t8",
                            user_role='UX/UI-дизайнер',
                            internship='MAIBO',
                            jira=True,
                            adobe_xd=True,
                            figma=True,
                            mockplus=True,
                            yandex_metrika=True,
                            google_analytics=True,
                            sketch=True,
                            fontjoy=True
                            )
        row_9 = ToolsOrm(id="t9",
                            user_role='UX/UI-дизайнер',
                            internship='Платформа для ВУЗов',
                            jira=True,
                            adobe_xd=True,
                            figma=True,
                            mockplus=True,
                            yandex_metrika=True,
                            google_analytics=True,
                            sketch=True,
                            fontjoy=True
                            )

        with session_factory() as session:
            session.add_all([row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9])
            session.commit()

    @staticmethod
    def select_interns():
        with session_factory() as session:
            query = select(InternsOrm)
            result = session.execute(query)
            interns = result.scalars().all()
            for model in interns:
                print(model)

    @staticmethod
    def select_interns_email(intern_email: str = 'work.aubakirov@gmail.com'):
        with session_factory() as session:
            query = select(InternsOrm)
            result = session.execute(query)
            #interns = result.all() # кортежи
            interns = result.scalars().all() # модели
            for model in result:
                print(model)    
    
    @staticmethod
    def update_interns(intern_id: str = 'f3', new_name: str = 'Ricardo Blanco'):
        with session_factory() as session:
            intern_update = session.get(InternsOrm, intern_id)
            intern_update.username = new_name
            session.commit()