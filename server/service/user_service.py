from models.base import Session
from models.user import User

class UserService:
    @staticmethod
    def view_profile(user_id):
        user = Session().query(User).get(user_id)
        return user

    @staticmethod
    def edit_profile(user_id, new_data):
        user = Session().query(User).get(user_id)
        if not user:
            return None
        for key, value in new_data.items():
            setattr(user, key, value)
        Session().commit()

    @staticmethod
    def create_user(username, first_name, last_name, email, password_hash, age, sex):
        session = Session()  # Create a session object
        user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=password_hash,
        age=age,
        sex=sex
    )
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
