from uuid import uuid4
from datetime import datetime, timedelta

from src.models.entities.User import User
from src.models.entities.Goal import Goal
from src.models.entities.GoalCompletion import GoalCompletion
from src.models.config.connection import db_connection_handler

import random


def create_seeds():
    with db_connection_handler as database:
        # Clean the tables
        database.session.query(GoalCompletion).delete()
        database.session.query(Goal).delete()
        database.session.query(User).delete()

        # Create users
        users = [
            User(
                id=str(uuid4()),
                name="João Silva",
                email="joao@exemplo.com",
                password="password",
            ),
            User(
                id=str(uuid4()),
                name="Maria Souza",
                email="maria@exemplo.com",
                password="password",
            ),
        ]
        database.session.add_all(users)
        database.session.commit()

        # Create goals
        goals = []
        for user in users:
            goals.extend(
                [
                    Goal(
                        id=str(uuid4()),
                        user_id=user.id,
                        title="Exercitar-se 3x na semana",
                        description="Realizar atividades físicas por pelo menos 30 minutos, 3 vezes na semana",
                        desiredWeekFrequency=3,
                    ),
                    Goal(
                        id=str(uuid4()),
                        user_id=user.id,
                        title="Ler 30 minutos por dia",
                        description="Dedicar 30 minutos diários à leitura de livros ou artigos educativos",
                        desiredWeekFrequency=7,
                    ),
                    Goal(
                        id=str(uuid4()),
                        user_id=user.id,
                        title="Meditar diariamente",
                        description="Praticar meditação por 10-15 minutos todas as manhãs",
                        desiredWeekFrequency=7,
                    ),
                ]
            )
        database.session.add_all(goals)
        database.session.commit()

        # Create goals completions

        completions = []
        for goal in goals:
            for day in range(14):
                if random.random() > 0.6:  # 40% de chance de ter completado
                    completions.append(
                        GoalCompletion(
                            id=str(uuid4()),
                            goal_id=goal.id,
                            completion_date=datetime.now() - timedelta(days=day),
                        )
                    )
        database.session.add_all(completions)
        database.session.commit()

        print("✅ Seeds executados com sucesso!")
