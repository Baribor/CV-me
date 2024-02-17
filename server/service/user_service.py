from models.base import Session
from models.user import User

class UserService:
    @staticmethod
    def view_profile(user_id):
        user = Session().query(User).get(user_id)
        if not user:
            return None
        profile_data = {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password_hash': user.password_hash,
            'age': user.age,
            'sex': user.sex,
        }
        return profile_data

    @staticmethod
    def edit_profile(user_id, new_data):
        user = Session().query(User).get(user_id)
        if not user:
            return None
        for key, value in new_data.items():
            setattr(user, key, value)
        Session().commit()

    @staticmethod
    def create_user(id,username, first_name, last_name, email, password_hash, age, sex):
        user = User(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=password_hash,
            age=age,
            sex=sex
        )
        Session().add(user)
        Session().commit()
        return user
    
    @staticmethod
    def delete_user(user_id):
        user = Session().query(User).get(user_id)
        if user:
            Session().delete(user)
            Session().commit()
            return True
        return False
