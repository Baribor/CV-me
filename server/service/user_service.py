from models.base import Session
from models.user import User

class UserService:
    @staticmethod
    def view_profile(username):
        user = Session().query(User).filter_by(username=username).first()
        return user

    @staticmethod
    def edit_profile(user_id, new_data):
        session = Session() 
        user = session.query(User).get(user_id)
        if not user:
            return None
        for key, value in new_data.items():
            setattr(user, key, value)
        session.commit()

    @staticmethod
    def create_user(username, first_name, last_name, email, password):
        session = Session()
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        session = Session()
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

