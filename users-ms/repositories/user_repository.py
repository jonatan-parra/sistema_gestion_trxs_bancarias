from models.user import User, db

class UserRepository:

    @staticmethod
    def create_user_repository(name, last_name, email, role, is_active):

        user = User(name=name, last_name=last_name, email=email, role=role, is_active=is_active)
        
        db.session.add(user)
        db.session.commit()

        return user