from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserService:
    @staticmethod
    def view_profile(user_id):
        from models.user import User 
        user = User.query.get(user_id)
        if not user:
            return None  
        profile_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'age': user.age,
            'sex': user.sex,
        }
        return profile_data

    @staticmethod
    def edit_profile(user_id, new_data):
        from models.user import User
        user = User.query.get(user_id)
        if not user:
            return None
        for key, value in new_data.items():
            setattr(user, key, value)
        db.session.commit()

    @staticmethod
    def create_cv(user_id, cv_data):
        from models import CV
        from models.user import User
        user = User.query.get(user_id)
        if not user:
            return None
        cv = CV(title=cv_data.get('title', ''))
        user.cvs.append(cv)
        db.session.add(cv)
        db.session.commit()
        return cv

    @staticmethod
    def delete_cv(cv_id):
        cv = CV.query.get(cv_id)
        if cv:
            db.session.delete(cv)
            db.session.commit()
            return True 
        return False  

    @staticmethod
    def create_user(id, username, first_name, last_name,email,password_hash, age, sex):
        from models.user import User  # Import your User model
        user = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            age=age,
            sex=sex
        )
        db.session.add(user)
        db.session.commit()
        return user
