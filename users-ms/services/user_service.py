from repositories.user_repository import UserRepository

class UserService:
    
    @staticmethod
    def create_user_service(data):

        name = data['name']
        last_name = data['last_name']
        email = data['email']
        role = data['role']
        is_active = data['is_active']

        return UserRepository.create_user_repository(name, last_name, email, role, is_active)